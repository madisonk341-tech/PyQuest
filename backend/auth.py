import re

from flask import Blueprint, jsonify, request, session

from extensions import db
from models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
AVATARS = ["🦉", "🐢", "🦊", "🐙", "🦁", "🐼", "🦉", "🐧", "🦄", "🐝"]


def current_user():
    uid = session.get("user_id")
    if not uid:
        return None
    return User.query.get(uid)


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""
    display_name = (data.get("displayName") or username).strip()

    if not USERNAME_RE.match(username):
        return jsonify({"error": "Username must be 3-20 characters: letters, numbers, underscore."}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters."}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "That username is already taken."}), 409

    user = User(username=username, display_name=display_name or username)
    user.avatar = AVATARS[User.query.count() % len(AVATARS)]
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id
    return jsonify({"user": user.to_public()}), 201


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Incorrect username or password."}), 401

    session["user_id"] = user.id
    return jsonify({"user": user.to_public()})


@auth_bp.post("/logout")
def logout():
    session.pop("user_id", None)
    return jsonify({"ok": True})


@auth_bp.get("/me")
def me():
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in."}), 401
    return jsonify({"user": user.to_public()})
