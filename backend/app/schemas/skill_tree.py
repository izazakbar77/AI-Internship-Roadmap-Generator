from pydantic import BaseModel
from typing import List



class SkillTreeRequest(BaseModel):

    skills: List[str]

    target_role: str = "AI Engineer"



class SkillNode(BaseModel):

    skill: str

    level: str

    next_topics: List[str]



class SkillTreeResponse(BaseModel):

    target_role: str

    current_level: str

    roadmap: List[SkillNode]