from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db import SessionLocal
from schemas.user import UserLogin, Token
from crud.user import get_user_by_username, create_user
from utils.auth import verify_password, create_access_token

auth_router = APIRouter(tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token({"sub": db_user["username"]})
    return {"access_token": access_token}

@auth_router.post("/signup")
def signup(user: UserLogin, db: Session = Depends(get_db)):
    created_user = create_user(db, user.username, user.password)
    if created_user:
        return {"msg": "Usuario creado correctamente", "user": created_user}
    raise HTTPException(status_code=400, detail="No se pudo crear el usuario")
