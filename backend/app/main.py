from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_tables

# APIs
from app.api.auth import router as auth_router
from app.api.students import router as student_router
from app.api.skills import router as skill_router
from app.api.student_skills import router as student_skill_router
from app.api.case_studies import router as case_study_router
from app.api.recommendations import router as recommendation_router
from app.api.skill_tree import router as skill_tree_router
from app.api.roadmap import router as roadmap_router
from app.api.dashboard import router as dashboard_router
from app.api.engineering import router as engineering_router


# Create database tables
create_tables()


# FastAPI application
app = FastAPI(
    title="AI Internship Roadmap Generator",
    version="1.0.0",
    description="AI Powered Dynamic Skill Tree & Internship Roadmap Engine"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CORS configured for Vercel frontend


# Include API routers
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(skill_router)
app.include_router(student_skill_router)
app.include_router(case_study_router)
app.include_router(recommendation_router)
app.include_router(skill_tree_router)
app.include_router(roadmap_router)
app.include_router(dashboard_router)
app.include_router(engineering_router)


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Internship Roadmap Generator",
        "status": "Running Successfully"
    }