from fastapi import APIRouter

from app.schemas.roadmap import (
    RoadmapRequest,
    RoadmapResponse
)

from app.ai.roadmap_generator import RoadmapGenerator

router = APIRouter(
    prefix="/roadmap",
    tags=["AI Roadmap"]
)


@router.post("/", response_model=RoadmapResponse)
def generate(data: RoadmapRequest):

    result = RoadmapGenerator.generate(
        data.engineering_level,
        data.missing_skills
    )

    return RoadmapResponse(**result)