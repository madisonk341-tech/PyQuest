from datetime import datetime, timezone

from flask import Blueprint, jsonify, request

from auth import current_user
from content_data import MODULE_CONTENT, MODULES_META, MODULES_WITH_CONTENT, get_module_meta
from extensions import db
from models import ComponentProgress, MissedQuestion, ModuleQuizResult

content_bp = Blueprint("content", __name__, url_prefix="/api")


def _module_progress_map(user):
    """Return {module_id: {completedComponents: set, quizPassed: bool, quizBest: float}}"""
    result = {}
    if not user:
        return result
    for cp in ComponentProgress.query.filter_by(user_id=user.id, completed=True):
        result.setdefault(cp.module_id, {"completed": set(), "quizPassed": False, "quizBest": 0.0})
        result[cp.module_id]["completed"].add(cp.component_id)
    for qr in ModuleQuizResult.query.filter_by(user_id=user.id):
        result.setdefault(qr.module_id, {"completed": set(), "quizPassed": False, "quizBest": 0.0})
        result[qr.module_id]["quizPassed"] = qr.passed
        result[qr.module_id]["quizBest"] = qr.best_score
    return result


def _percent_for(module_id, prog):
    meta = MODULE_CONTENT.get(module_id)
    if not meta:
        return 0
    total_steps = len(meta["components"]) + 1  # +1 for the quiz
    done_steps = len(prog.get("completed", set())) + (1 if prog.get("quizPassed") else 0)
    return round(100 * done_steps / total_steps)


@content_bp.get("/modules")
def list_modules():
    user = current_user()
    prog_map = _module_progress_map(user)
    modules = []
    for meta in MODULES_META:
        prog = prog_map.get(meta["id"], {"completed": set(), "quizPassed": False, "quizBest": 0.0})
        modules.append({
            **meta,
            "hasContent": meta["id"] in MODULES_WITH_CONTENT,
            "percentComplete": _percent_for(meta["id"], prog) if meta["id"] in MODULES_WITH_CONTENT else 0,
            "quizPassed": prog.get("quizPassed", False),
        })
    return jsonify({"modules": modules})


@content_bp.get("/modules/<module_id>")
def get_module(module_id):
    meta = get_module_meta(module_id)
    if not meta:
        return jsonify({"error": "Module not found."}), 404
    content = MODULE_CONTENT.get(module_id)
    if not content:
        return jsonify({"error": "This module's content isn't published yet.", "meta": meta}), 404

    user = current_user()
    prog_map = _module_progress_map(user)
    prog = prog_map.get(module_id, {"completed": set(), "quizPassed": False, "quizBest": 0.0})

    components = []
    for comp in content["components"]:
        components.append({**comp, "completed": comp["id"] in prog.get("completed", set())})

    return jsonify({
        "id": content["id"],
        "title": content["title"],
        "intro": content["intro"],
        "components": components,
        "quiz": [{k: v for k, v in q.items() if k != "answer" and k != "explanation"} for q in content["quiz"]],
        "quizPassed": prog.get("quizPassed", False),
        "quizBest": prog.get("quizBest", 0.0),
        "percentComplete": _percent_for(module_id, prog),
    })


@content_bp.post("/modules/<module_id>/components/<component_id>/complete")
def complete_component(module_id, component_id):
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    row = ComponentProgress.query.filter_by(
        user_id=user.id, module_id=module_id, component_id=component_id
    ).first()
    if not row:
        row = ComponentProgress(user_id=user.id, module_id=module_id, component_id=component_id)
        db.session.add(row)
    row.completed = True
    row.completed_at = datetime.now(timezone.utc)
    db.session.commit()
    return jsonify({"ok": True})


@content_bp.post("/modules/<module_id>/practice-answer")
def log_practice_answer(module_id):
    """Called after each in-lesson practice question so we can power the weak-areas exam."""
    user = current_user()
    if not user:
        return jsonify({"ok": True})  # anonymous practice still "works", just isn't tracked

    data = request.get_json(silent=True) or {}
    correct = bool(data.get("correct"))
    if not correct:
        _record_miss(user.id, module_id)
        db.session.commit()
    return jsonify({"ok": True})


def _record_miss(user_id, module_id):
    row = MissedQuestion.query.filter_by(user_id=user_id, module_id=module_id).first()
    if not row:
        row = MissedQuestion(user_id=user_id, module_id=module_id, times_missed=0)
        db.session.add(row)
    row.times_missed += 1
    row.last_missed_at = datetime.now(timezone.utc)


@content_bp.post("/modules/<module_id>/quiz/submit")
def submit_module_quiz(module_id):
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    content = MODULE_CONTENT.get(module_id)
    if not content:
        return jsonify({"error": "Module not found."}), 404

    data = request.get_json(silent=True) or {}
    answers = data.get("answers") or {}  # {question_id: choice_index}

    total = len(content["quiz"])
    correct = 0
    results = []
    for q in content["quiz"]:
        chosen = answers.get(q["id"])
        is_correct = chosen == q["answer"]
        if is_correct:
            correct += 1
        else:
            _record_miss(user.id, module_id)
        results.append({
            "id": q["id"],
            "correct": is_correct,
            "correctAnswer": q["answer"],
            "explanation": q["explanation"],
        })

    score = round(100 * correct / total) if total else 0
    passed = score >= 70

    row = ModuleQuizResult.query.filter_by(user_id=user.id, module_id=module_id).first()
    if not row:
        row = ModuleQuizResult(user_id=user.id, module_id=module_id, best_score=0, attempts=0)
        db.session.add(row)
    row.attempts += 1
    row.best_score = max(row.best_score, score)
    row.passed = row.passed or passed
    row.last_taken_at = datetime.now(timezone.utc)

    db.session.commit()

    return jsonify({"score": score, "correct": correct, "total": total, "passed": passed, "results": results})


@content_bp.get("/progress/summary")
def progress_summary():
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401

    prog_map = _module_progress_map(user)
    modules = []
    for meta in MODULES_META:
        if meta["id"] not in MODULES_WITH_CONTENT:
            continue
        prog = prog_map.get(meta["id"], {"completed": set(), "quizPassed": False, "quizBest": 0.0})
        modules.append({
            "id": meta["id"],
            "title": meta["title"],
            "percentComplete": _percent_for(meta["id"], prog),
            "quizPassed": prog.get("quizPassed", False),
        })

    weak = [
        {"moduleId": m.module_id, "timesMissed": m.times_missed}
        for m in MissedQuestion.query.filter_by(user_id=user.id).order_by(MissedQuestion.times_missed.desc())
    ]

    overall = round(sum(m["percentComplete"] for m in modules) / len(modules)) if modules else 0

    return jsonify({"modules": modules, "weakModules": weak, "overallPercent": overall})
