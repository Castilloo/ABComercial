from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import users

def get_user_by_username(db: Session, username: str):
    user = db.execute(select(users).where(users.c.username == username)).mappings().first()
    if user:
        return dict(user)
    return None

def create_user(db: Session, username: str, password: str):
    from utils.auth import get_password_hash
    hashed_password = get_password_hash(password)
    result = db.execute(
        users.insert()
        .values(username=username, password=hashed_password)
        .returning(users)
    )
    db.commit()
    row = result.fetchone()
    if row:
        return dict(row._mapping) 
    return {}
