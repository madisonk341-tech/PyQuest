from flask import Blueprint, jsonify, request

from content_data import SANDBOX_PROMPTS

sandbox_bp = Blueprint("sandbox", __name__, url_prefix="/api/sandbox")


@sandbox_bp.get("/prompts")
def list_prompts():
    search = (request.args.get("search") or "").strip().lower()
    module_id = request.args.get("module")

    prompts = SANDBOX_PROMPTS
    if module_id:
        prompts = [p for p in prompts if p["module_id"] == module_id]
    if search:
        prompts = [
            p for p in prompts
            if search in p["title"].lower() or search in p["prompt"].lower()
        ]
    return jsonify({"prompts": prompts})
