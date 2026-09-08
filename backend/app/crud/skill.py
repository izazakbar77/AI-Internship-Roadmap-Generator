from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.schemas.skill import SkillCreate


def get_skills(db: Session):
    return db.query(Skill).all()


def get_skill(db: Session, skill_id: int):
    return (
        db.query(Skill)
        .filter(Skill.id == skill_id)
        .first()
    )


def create_skill(db: Session, skill: SkillCreate):

    new_skill = Skill(
        name=skill.name,
        category=skill.category,
        difficulty=skill.difficulty,
        description=skill.description
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill


def delete_skill(db: Session, skill_id: int):

    skill = (
        db.query(Skill)
        .filter(Skill.id == skill_id)
        .first()
    )

    if skill:
        db.delete(skill)
        db.commit()

    return skill