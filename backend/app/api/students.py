from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import (
    create_student,
    get_students,
    get_student,
    delete_student
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student.model_dump())


@router.get("/", response_model=list[StudentResponse])
def all_students(db: Session = Depends(get_db)):
    return get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def single_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return student


@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    student = delete_student(db, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return {"message": "Student Deleted Successfully"}