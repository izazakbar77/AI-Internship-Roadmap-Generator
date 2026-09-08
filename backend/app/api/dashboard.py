from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.dashboard import (
    DashboardResponse,
    StudentDashboardResponse
)

from app.services.dashboard_service import (
    dashboard_statistics,
    student_dashboard
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


# Overall Dashboard

@router.get(
    "/",
    response_model=DashboardResponse
)
def dashboard(
    db: Session = Depends(get_db)
):

    return dashboard_statistics(db)



# Student Dashboard

@router.get(
    "/student/{student_id}",
    response_model=StudentDashboardResponse
)
def get_student_dashboard(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = student_dashboard(
        db,
        student_id
    )


    if not result:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return result