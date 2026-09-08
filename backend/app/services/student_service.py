from sqlalchemy.orm import Session
from app.models.student import Student


def create_student(db: Session, student_data: dict):
    student = Student(**student_data)

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)

    if student:
        db.delete(student)
        db.commit()

    return student