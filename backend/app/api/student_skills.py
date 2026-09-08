from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.student_skill import (
    StudentSkillCreate,
    StudentSkillResponse
)
from app.services.student_skill_service import (
    assign_skill,
    get_all_student_skills,
    get_student_skills,
    delete_student_skill
)

router = APIRouter(
    prefix="/student-skills",
    tags=["Student Skills"]
)


@router.post("/", response_model=StudentSkillResponse)
def add_student_skill(
    skill: StudentSkillCreate,
    db: Session = Depends(get_db)
):
    return assign_skill(db, skill.model_dump())


@router.get("/", response_model=list[StudentSkillResponse])
def all_student_skills(db: Session = Depends(get_db)):
    return get_all_student_skills(db)


@router.get("/{student_id}", response_model=list[StudentSkillResponse])
def student_skills(student_id: int, db: Session = Depends(get_db)):
    return get_student_skills(db, student_id)


@router.delete("/{record_id}")
def remove_student_skill(record_id: int, db: Session = Depends(get_db)):
    record = delete_student_skill(db, record_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record Not Found")

    return {"message": "Student Skill Deleted Successfully"}