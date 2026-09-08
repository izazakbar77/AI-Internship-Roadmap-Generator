from typing import List
from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
    attendance: float = Field(ge=0, le=100)
    coding_speed: int = Field(ge=0, le=100)
    interview_score: int = Field(ge=0, le=100)
    case_study_score: int = Field(ge=0, le=100)

    skills: List[str] = []
    skill_scores: List[int] = []


class RecommendationResponse(BaseModel):

    engineering_score: float

    engineering_level: str

    job_readiness: str

    promotion_readiness: str

    missing_skills: List[str]

    recommended_role: str

    recommended_projects: List[str]

    learning_priority: List[str]