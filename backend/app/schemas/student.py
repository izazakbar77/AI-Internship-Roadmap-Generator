from pydantic import BaseModel, Field
from typing import Optional


# ==========================================================
# STUDENT CREATE
# ==========================================================

class StudentCreate(BaseModel):

    user_id: int

    university: str

    degree: str

    semester: int

    github_url: Optional[str] = None

    linkedin_url: Optional[str] = None

    engineering_level: Optional[str] = "Beginner"

    coding_speed: Optional[int] = Field(
        default=0,
        ge=0,
        le=100
    )

    attendance_percentage: Optional[float] = Field(
        default=0,
        ge=0,
        le=100
    )

    # ======================================================
    # EVALUATION METRICS
    # ======================================================

    interview_score: Optional[float] = Field(
        default=0,
        ge=0,
        le=100
    )

    case_study_score: Optional[float] = Field(
        default=0,
        ge=0,
        le=100
    )

    # ======================================================
    # INTERNSHIP
    # ======================================================

    internship_goal: Optional[str] = None


# ==========================================================
# STUDENT RESPONSE
# ==========================================================

class StudentResponse(StudentCreate):

    id: int

    class Config:
        from_attributes = True