from app.models.user import User
from app.utils.db import db

def create_user(email):
    if not email:
        raise ValueError("Email is required")

    existing = User.query.filter_by(email=email).first()
    if existing:
        raise ValueError("User already exists")

    user = User(email=email)
    db.session.add(user)
    db.session.commit()

    return user
