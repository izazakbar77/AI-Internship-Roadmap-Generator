from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.engineering import EngineeringLevelResponse

from app.services.engineering_service import calculate_engineering_level



router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)



@router.get(
    "/engineering-level/{student_id}",
    response_model=EngineeringLevelResponse
)
def engineering_level(
    student_id:int,
    db:Session = Depends(get_db)
):

    result = calculate_engineering_level(
        db,
        student_id
    )


    if not result:
        return {
            "detail":"Student not found"
        }


    return result