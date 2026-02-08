from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask
from app.utils.db import db
from app.config import DevelopmentConfig, ProductionConfig

def create_app():
    flask_app = Flask(__name__)  # <-- IMPORTANT: not named "app"

    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        flask_app.config.from_object(ProductionConfig)
    else:
        flask_app.config.from_object(DevelopmentConfig)

    db.init_app(flask_app)

    from app.routes.user_routes import user_bp
    from app.routes.health import health_bp

    flask_app.register_blueprint(user_bp)
    flask_app.register_blueprint(health_bp)

    with flask_app.app_context():
        db.create_all()

    return flask_app
