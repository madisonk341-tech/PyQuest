from datetime import datetime, timezone

from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


def now():
    return datetime.now(timezone.utc)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    display_name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(8), nullable=False, default="🦉")
    created_at = db.Column(db.DateTime, default=now)

    component_progress = db.relationship("ComponentProgress", backref="user", lazy="dynamic")
    quiz_results = db.relationship("ModuleQuizResult", backref="user", lazy="dynamic")
    attempts = db.relationship("PracticeAttempt", backref="user", lazy="dynamic")
    missed = db.relationship("MissedQuestion", backref="user", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_public(self):
        return {
            "id": self.id,
            "username": self.username,
            "displayName": self.display_name,
            "avatar": self.avatar,
        }


class ComponentProgress(db.Model):
    __tablename__ = "component_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    module_id = db.Column(db.String(16), nullable=False)
    component_id = db.Column(db.String(32), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, default=now)

    __table_args__ = (
        db.UniqueConstraint("user_id", "module_id", "component_id", name="uq_user_component"),
    )


class ModuleQuizResult(db.Model):
    __tablename__ = "module_quiz_results"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    module_id = db.Column(db.String(16), nullable=False)
    best_score = db.Column(db.Float, default=0.0)
    passed = db.Column(db.Boolean, default=False)
    attempts = db.Column(db.Integer, default=0)
    last_taken_at = db.Column(db.DateTime, default=now)

    __table_args__ = (
        db.UniqueConstraint("user_id", "module_id", name="uq_user_module_quiz"),
    )


class PracticeAttempt(db.Model):
    """An in-progress or completed practice/exam attempt.

    question_bank stores the server-side source of truth (question ids +
    correct answers) so the client never receives answer keys before
    submitting.
    """

    __tablename__ = "practice_attempts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    kind = db.Column(db.String(16), nullable=False)  # module_practice | exam1 | exam2 | weak
    scope = db.Column(db.String(255), nullable=False)  # comma separated module ids
    question_bank = db.Column(db.JSON, nullable=False)
    submitted = db.Column(db.Boolean, default=False)
    score = db.Column(db.Float, nullable=True)
    correct_count = db.Column(db.Integer, nullable=True)
    total_count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=now)
    submitted_at = db.Column(db.DateTime, nullable=True)


class MissedQuestion(db.Model):
    """Tracks wrong answers in the Learning tab to power the weak-areas exam."""

    __tablename__ = "missed_questions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    module_id = db.Column(db.String(16), nullable=False)
    times_missed = db.Column(db.Integer, default=1)
    last_missed_at = db.Column(db.DateTime, default=now)

    __table_args__ = (
        db.UniqueConstraint("user_id", "module_id", name="uq_user_module_missed"),
    )
