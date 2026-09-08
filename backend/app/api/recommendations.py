from fastapi import APIRouter

from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

from app.ai.recommendation_engine import RecommendationEngine



router = APIRouter(
    prefix="/recommendations",
    tags=["AI Recommendation"]
)



@router.post(
    "/",
    response_model=RecommendationResponse
)
def generate(data: RecommendationRequest):


    # Calculate Engineering Score

    score = RecommendationEngine.calculate_engineering_score(
        attendance=data.attendance,
        coding_speed=data.coding_speed,
        interview_score=data.interview_score,
        case_study_score=data.case_study_score,
        skills=data.skill_scores
    )



    # Engineering Level

    level = RecommendationEngine.engineering_level(
        score
    )



    # Job Readiness

    readiness = RecommendationEngine.job_readiness(
        score
    )



    # Promotion Readiness

    promotion = RecommendationEngine.promotion_readiness(
        score
    )



    # Missing Skills

    missing = RecommendationEngine.missing_skills(
        data.skills
    )



    # AI Recommendation

    if score >= 80:

        role = "AI Engineer Intern"

        projects = [
            "AI Chatbot",
            "RAG Based Question Answering System",
            "Computer Vision Project"
        ]



    elif score >= 50:

        role = "Machine Learning Intern"

        projects = [
            "Machine Learning Prediction System",
            "Data Analysis Dashboard",
            "Recommendation System"
        ]



    else:

        role = "AI Beginner Intern"

        projects = [
            "Python Automation Project",
            "Basic ML Model",
            "Data Processing Project"
        ]



    # Learning Priority

    priority = missing[:3]



    return RecommendationResponse(

        engineering_score=score,

        engineering_level=level,

        job_readiness=readiness,

        promotion_readiness=promotion,

        missing_skills=missing,

        recommended_role=role,

        recommended_projects=projects,

        learning_priority=priority

    )