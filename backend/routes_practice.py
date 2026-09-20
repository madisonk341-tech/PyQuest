import random
from datetime import datetime, timezone

from flask import Blueprint, jsonify, request

from auth import current_user
from content_data import MODULES_META, PRACTICE_POOLS
from extensions import db
from models import MissedQuestion, PracticeAttempt

practice_bp = Blueprint("practice", __name__, url_prefix="/api/practice")


def _pool_for_modules(module_ids):
    pool = []
    for mid in module_ids:
        pool.extend(PRACTICE_POOLS.get(mid, []))
    return pool


def _build_attempt(user, kind, module_ids, count):
    pool = _pool_for_modules(module_ids)
    if not pool:
        return None, "No practice questions are available yet for the selected module(s)."

    count = min(count, len(pool))
    questions = random.sample(pool, count)

    attempt = PracticeAttempt(
        user_id=user.id,
        kind=kind,
        scope=",".join(module_ids),
        question_bank=questions,
        total_count=len(questions),
    )
    db.session.add(attempt)
    db.session.commit()

    client_questions = [
        {"id": q["id"], "question": q["question"], "choices": q["choices"]} for q in questions
    ]
    return {"attemptId": attempt.id, "kind": kind, "questions": client_questions}, None


@practice_bp.get("/quiz")
def module_quiz():
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    modules_param = request.args.get("modules", "")
    module_ids = [m.strip() for m in modules_param.split(",") if m.strip()]
    if not module_ids:
        return jsonify({"error": "Provide at least one module id."}), 400

    count = int(request.args.get("count", 10))
    payload, error = _build_attempt(user, "practice", module_ids, count)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(payload)


@practice_bp.get("/exam/<exam_id>")
def exam(exam_id):
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401
    if exam_id not in ("exam1", "exam2"):
        return jsonify({"error": "Unknown exam."}), 404

    module_ids = [m["id"] for m in MODULES_META if m["exam"] == exam_id]
    count = int(request.args.get("count", 20))
    payload, error = _build_attempt(user, exam_id, module_ids, count)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(payload)


@practice_bp.get("/weak")
def weak_areas():
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    missed = MissedQuestion.query.filter_by(user_id=user.id).all()
    module_ids = [m.module_id for m in missed if m.module_id in PRACTICE_POOLS]
    if not module_ids:
        return jsonify({"error": "No struggling topics found yet — keep learning and we'll track this for you!"}), 404

    count = int(request.args.get("count", 10))
    payload, error = _build_attempt(user, "weak", module_ids, count)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(payload)


@practice_bp.post("/attempts/<int:attempt_id>/submit")
def submit_attempt(attempt_id):
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    attempt = PracticeAttempt.query.filter_by(id=attempt_id, user_id=user.id).first()
    if not attempt:
        return jsonify({"error": "Attempt not found."}), 404
    if attempt.submitted:
        return jsonify({"error": "This attempt was already submitted."}), 400

    data = request.get_json(silent=True) or {}
    answers = data.get("answers") or {}

    correct = 0
    results = []
    for q in attempt.question_bank:
        chosen = answers.get(q["id"])
        is_correct = chosen == q["answer"]
        if is_correct:
            correct += 1
        else:
            _record_miss(user.id, q["id"])
        results.append({
            "id": q["id"],
            "question": q["question"],
            "choices": q["choices"],
            "chosen": chosen,
            "correct": is_correct,
            "correctAnswer": q["answer"],
            "explanation": q["explanation"],
        })

    score = round(100 * correct / attempt.total_count) if attempt.total_count else 0
    attempt.submitted = True
    attempt.score = score
    attempt.correct_count = correct
    attempt.submitted_at = datetime.now(timezone.utc)
    db.session.commit()

    return jsonify({"score": score, "correct": correct, "total": attempt.total_count, "results": results})


def _record_miss(user_id, question_id):
    module_id = question_id.split(".")[0]
    row = MissedQuestion.query.filter_by(user_id=user_id, module_id=module_id).first()
    if not row:
        row = MissedQuestion(user_id=user_id, module_id=module_id, times_missed=0)
        db.session.add(row)
    row.times_missed += 1
    row.last_missed_at = datetime.now(timezone.utc)
