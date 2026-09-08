from pydantic import BaseModel
from typing import List


class EngineeringLevelResponse(BaseModel):

    student_id: int

    engineering_level: str

    engineering_score: float

    strengths: List[str]

    weaknesses: List[str]

    recommended_role: str

    next_focus: str