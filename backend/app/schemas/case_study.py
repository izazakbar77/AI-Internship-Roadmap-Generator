from pydantic import BaseModel
from typing import Optional


class CaseStudyCreate(BaseModel):
    student_id: int
    title: str
    technology: Optional[str] = None
    difficulty: Optional[str] = "Easy"
    status: Optional[str] = "Pending"
    score: Optional[int] = 0


class CaseStudyResponse(CaseStudyCreate):
    id: int

    class Config:
        from_attributes = True