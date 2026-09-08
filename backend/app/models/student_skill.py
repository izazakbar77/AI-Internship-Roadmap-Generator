from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class StudentSkill(Base):
    __tablename__ = "student_skills"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    level = Column(String, default="Beginner")

    score = Column(Integer, default=0)