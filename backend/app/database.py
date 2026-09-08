from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./ai_roadmap.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    # Import all models before creating tables
    from app.models.user import User
    from app.models.student import Student
    from app.models.skill import Skill
    from app.models.student_skill import StudentSkill
    from app.models.case_study import CaseStudy

    Base.metadata.create_all(bind=engine)