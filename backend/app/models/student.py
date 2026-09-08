from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base


class Student(Base):

    __tablename__ = "students"

    # ==========================================================
    # PRIMARY KEY
    # ==========================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ==========================================================
    # USER RELATIONSHIP
    # ==========================================================

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    # ==========================================================
    # ACADEMIC INFORMATION
    # ==========================================================

    university = Column(
        String,
        nullable=False,
    )

    degree = Column(
        String,
        nullable=False,
    )

    semester = Column(
        Integer,
        nullable=False,
    )

    # ==========================================================
    # PROFESSIONAL PROFILES
    # ==========================================================

    github_url = Column(
        String,
        nullable=True,
    )

    linkedin_url = Column(
        String,
        nullable=True,
    )

    # ==========================================================
    # ENGINEERING INFORMATION
    # ==========================================================

    engineering_level = Column(
        String,
        default="Beginner",
    )

    coding_speed = Column(
        Integer,
        default=0,
    )

    attendance_percentage = Column(
        Float,
        default=0,
    )

    # ==========================================================
    # EVALUATION METRICS
    # ==========================================================

    interview_score = Column(
        Float,
        default=0,
    )

    case_study_score = Column(
        Float,
        default=0,
    )

    # ==========================================================
    # INTERNSHIP GOAL
    # ==========================================================

    internship_goal = Column(
        String,
        nullable=True,
    )

    # ==========================================================
    # CREATED DATE
    # ==========================================================

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    # ==========================================================
    # USER RELATIONSHIP
    # ==========================================================

    user = relationship(
        "User",
        back_populates="student",
    )