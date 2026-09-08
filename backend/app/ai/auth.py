from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



# Register User

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):


    existing_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )


    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )



    new_user = User(

        full_name=user.full_name,

        username=user.username,

        email=user.email,

        password=user.password,

        role="Student"

    )



    db.add(new_user)

    db.commit()

    db.refresh(new_user)



    return new_user





# Current User Test

@router.get(
    "/me",
    response_model=UserResponse
)
def current_user(
    db: Session = Depends(get_db)
):


    user = (
        db.query(User)
        .first()
    )


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    return user