from sqlalchemy.orm import Session
from app.models.case_study import CaseStudy


def create_case_study(db: Session, data: dict):
    case = CaseStudy(**data)
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def get_case_studies(db: Session):
    return db.query(CaseStudy).all()


def get_case_study(db: Session, case_id: int):
    return db.query(CaseStudy).filter(
        CaseStudy.id == case_id
    ).first()


def delete_case_study(db: Session, case_id: int):
    case = get_case_study(db, case_id)

    if case:
        db.delete(case)
        db.commit()

    return case