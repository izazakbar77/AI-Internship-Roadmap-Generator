from pydantic import BaseModel
from typing import Optional


class SkillCreate(BaseModel):
    name: str
    category: str
    difficulty: str
    description: Optional[str] = None


class SkillResponse(SkillCreate):
    id: int

    class Config:
        from_attributes = True