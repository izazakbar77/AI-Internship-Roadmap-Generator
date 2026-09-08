from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "Student"


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    username: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True