from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.skill import SkillCreate, SkillResponse
from app.services.skill_service import (
    create_skill,
    get_skills,
    get_skill,
    delete_skill
)

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.post("/", response_model=SkillResponse)
def add_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    return create_skill(db, skill.model_dump())


@router.get("/", response_model=list[SkillResponse])
def all_skills(db: Session = Depends(get_db)):
    return get_skills(db)


@router.get("/{skill_id}", response_model=SkillResponse)
def single_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = get_skill(db, skill_id)

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill Not Found"
        )

    return skill


@router.delete("/{skill_id}")
def remove_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = delete_skill(db, skill_id)

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill Not Found"
        )

    return {
        "message": "Skill Deleted Successfully"
    }