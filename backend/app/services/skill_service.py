from sqlalchemy.orm import Session
from app.models.skill import Skill


def create_skill(db: Session, skill_data: dict):
    skill = Skill(**skill_data)

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill


def get_skills(db: Session):
    return db.query(Skill).all()


def get_skill(db: Session, skill_id: int):
    return db.query(Skill).filter(
        Skill.id == skill_id
    ).first()


def delete_skill(db: Session, skill_id: int):
    skill = get_skill(db, skill_id)

    if skill:
        db.delete(skill)
        db.commit()

    return skill