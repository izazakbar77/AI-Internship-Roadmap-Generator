from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.case_study import (
    CaseStudyCreate,
    CaseStudyResponse
)
from app.services.case_study_service import (
    create_case_study,
    get_case_studies,
    get_case_study,
    delete_case_study
)

router = APIRouter(
    prefix="/case-studies",
    tags=["Case Studies"]
)


@router.post("/", response_model=CaseStudyResponse)
def add_case_study(case: CaseStudyCreate, db: Session = Depends(get_db)):
    return create_case_study(db, case.model_dump())


@router.get("/", response_model=list[CaseStudyResponse])
def all_case_studies(db: Session = Depends(get_db)):
    return get_case_studies(db)


@router.get("/{case_id}", response_model=CaseStudyResponse)
def single_case_study(case_id: int, db: Session = Depends(get_db)):
    case = get_case_study(db, case_id)

    if not case:
        raise HTTPException(status_code=404, detail="Case Study Not Found")

    return case


@router.delete("/{case_id}")
def remove_case_study(case_id: int, db: Session = Depends(get_db)):
    case = delete_case_study(db, case_id)

    if not case:
        raise HTTPException(status_code=404, detail="Case Study Not Found")

    return {"message": "Case Study Deleted Successfully"}