from sqlalchemy.orm import Session
from app.models.student_skill import StudentSkill


def assign_skill(db: Session, data: dict):
    student_skill = StudentSkill(**data)
    db.add(student_skill)
    db.commit()
    db.refresh(student_skill)
    return student_skill


def get_all_student_skills(db: Session):
    return db.query(StudentSkill).all()


def get_student_skills(db: Session, student_id: int):
    return db.query(StudentSkill).filter(
        StudentSkill.student_id == student_id
    ).all()


def delete_student_skill(db: Session, record_id: int):
    record = db.query(StudentSkill).filter(
        StudentSkill.id == record_id
    ).first()

    if record:
        db.delete(record)
        db.commit()

    return record