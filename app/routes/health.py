import socket
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/", methods=["GET"])
def health():
    hostname = socket.gethostname()
    return jsonify({
        "status": "DONEEEE , 18 ---- Feb",
        "instance": hostname
        "ok beii"
    }), 200
