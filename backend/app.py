import os

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from extensions import db

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIST = os.path.join(BASE_DIR, "..", "frontend", "dist")


def create_app():
    app = Flask(__name__, static_folder=FRONTEND_DIST, static_url_path="")

    app.config["SECRET_KEY"] = os.environ.get("PYQUEST_SECRET_KEY", "dev-secret-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "instance", "app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)

    db.init_app(app)

    # Allow the Vite dev server to call the API with cookies during development.
    CORS(app, supports_credentials=True, origins=[
        "http://localhost:5173", "http://127.0.0.1:5173",
    ])

    from auth import auth_bp
    from routes_content import content_bp
    from routes_practice import practice_bp
    from routes_sandbox import sandbox_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(practice_bp)
    app.register_blueprint(sandbox_bp)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def spa_fallback(e):
        # If the built frontend exists, serve index.html for any unknown
        # (non-/api) route so client-side routing works on refresh.
        index_path = os.path.join(app.static_folder, "index.html")
        if os.path.exists(index_path):
            return send_from_directory(app.static_folder, "index.html")
        return jsonify({"error": "Not found. (Frontend not built yet — run `npm run build` in /frontend.)"}), 404

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
