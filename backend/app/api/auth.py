from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.auth_service import hash_password, verify_password
from app.crud.user import (
    get_user_by_username,
    get_user_by_email,
    create_user
)
from app.dependencies import get_current_user
from app.core.security import create_access_token
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user_data = user.model_dump()

    user_data["password"] = hash_password(user.password)

    new_user = create_user(db, user_data)

    return new_user


@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):

    user = get_user_by_username(db, credentials.username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or Password")

    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid Username or Password")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserResponse)
def current_user(current_user: User = Depends(get_current_user)):
    return current_user