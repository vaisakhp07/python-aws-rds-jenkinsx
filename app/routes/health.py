import socket
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/", methods=["GET"])
def health():
    hostname = socket.gethostname()
    return jsonify({
        "status": "DONEEEE , 20 Feb 12:00",
        "instance": hostname
    }), 200
