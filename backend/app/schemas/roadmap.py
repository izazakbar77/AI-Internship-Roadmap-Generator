from pydantic import BaseModel
from typing import List



class RoadmapRequest(BaseModel):

    engineering_level: str

    missing_skills: List[str]

    target_role: str = "AI Engineer"

    internship_duration: int = 3



class RoadmapResponse(BaseModel):

    target_role: str

    engineering_level: str

    weekly_goals: List[str]

    monthly_goals: List[str]

    recommended_projects: List[str]

    recommended_case_study: str

    technology_dependencies: List[str]

    missing_skills: List[str]

    estimated_graduation: str

    roadmap: List[str]