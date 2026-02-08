from flask import Blueprint, request, jsonify
from app.services.user_service import create_user

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    try:
        user = create_user(data.get("email"))
        return jsonify({"id": user.id, "email": user.email}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
