from pydantic import BaseModel
from typing import List


# ================= Overall Dashboard =================

class DashboardResponse(BaseModel):

    total_students: int

    total_skills: int

    total_case_studies: int

    total_student_skills: int

    average_engineering_score: float

    job_ready_students: int

    ai_growth: float


# ================= Student Skills =================

class StudentSkillDashboard(BaseModel):

    name: str

    score: float


# ================= AI Career Prediction =================

class CareerPrediction(BaseModel):

    role: str

    confidence: float


# ================= Roadmap =================

class RoadmapItem(BaseModel):

    week: str

    title: str


# ================= Case Studies =================

class CaseStudyDashboard(BaseModel):

    id: int

    title: str

    technology: str | None = None

    difficulty: str | None = None

    status: str | None = None

    score: float


# ================= Student AI Dashboard =================

class StudentDashboardResponse(BaseModel):

    student_id: int

    name: str

    email: str

    engineering_score: float

    level: str

    job_readiness: str

    skills: List[StudentSkillDashboard]

    skill_count: int

    roadmap_available: bool

    career_prediction: CareerPrediction

    learning_focus: List[str]

    missing_skills: List[str]

    case_studies: List[CaseStudyDashboard]

    roadmap: List[RoadmapItem]

    # Actual student evaluation metrics

    attendance: float

    coding_speed: float

    interview_score: float

    case_study_score: float


# ================= Engineering Level =================

class EngineeringLevelResponse(BaseModel):

    student_id: int

    engineering_score: float

    level: str

    message: str