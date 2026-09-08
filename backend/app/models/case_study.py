from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class CaseStudy(Base):
    __tablename__ = "case_studies"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))

    title = Column(String, nullable=False)

    technology = Column(String)

    difficulty = Column(String)

    status = Column(String, default="Pending")

    score = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)