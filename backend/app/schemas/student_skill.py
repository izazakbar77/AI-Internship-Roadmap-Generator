from pydantic import BaseModel


class StudentSkillCreate(BaseModel):
    student_id: int
    skill_id: int
    level: str
    score: int


class StudentSkillResponse(StudentSkillCreate):
    id: int

    class Config:
        from_attributes = True