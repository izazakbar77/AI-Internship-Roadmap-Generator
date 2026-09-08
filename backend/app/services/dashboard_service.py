from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.user import User
from app.models.skill import Skill
from app.models.case_study import CaseStudy
from app.models.student_skill import StudentSkill


# =========================================================
# REQUIRED AI / ENGINEERING SKILLS
# =========================================================

REQUIRED_SKILLS = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Large Language Models",
    "FastAPI",
    "Docker",
    "MLOps",
    "Git",
    "React",
    "SQL",
    "CI/CD",
]


# =========================================================
# HELPER: STUDENT ENGINEERING SCORE
# =========================================================

def get_student_engineering_score(
    db: Session,
    student_id: int
) -> float:

    records = (
        db.query(StudentSkill)
        .filter(
            StudentSkill.student_id == student_id
        )
        .all()
    )

    if not records:
        return 0.0

    total_score = sum(
        record.score or 0
        for record in records
    )

    return round(
        total_score / len(records),
        2
    )


# =========================================================
# OVERALL DASHBOARD
# =========================================================

def dashboard_statistics(db: Session):

    total_students = db.query(Student).count()

    total_skills = db.query(Skill).count()

    total_case_studies = db.query(CaseStudy).count()

    total_student_skills = db.query(StudentSkill).count()

    # ---------------------------------------------------------
    # Calculate average engineering score PER STUDENT
    # ---------------------------------------------------------

    student_averages = []

    students = db.query(Student).all()

    for student in students:

        score = get_student_engineering_score(
            db,
            student.id
        )

        if score > 0:
            student_averages.append(score)

    if student_averages:

        engineering_score = round(
            sum(student_averages) /
            len(student_averages),
            2
        )

    else:

        engineering_score = 0.0

    # ---------------------------------------------------------
    # Job Ready Students
    # ---------------------------------------------------------

    job_ready_students = sum(
        1
        for score in student_averages
        if score >= 80
    )

    # ---------------------------------------------------------
    # AI Growth
    # ---------------------------------------------------------

    ai_skill_scores = []

    for required_skill in REQUIRED_SKILLS:

        skill = (
            db.query(Skill)
            .filter(
                Skill.name.ilike(required_skill)
            )
            .first()
        )

        if not skill:
            continue

        records = (
            db.query(StudentSkill)
            .filter(
                StudentSkill.skill_id == skill.id
            )
            .all()
        )

        for record in records:

            if record.score is not None:

                ai_skill_scores.append(
                    record.score
                )

    if ai_skill_scores:

        ai_growth = round(
            sum(ai_skill_scores) /
            len(ai_skill_scores),
            2
        )

    else:

        ai_growth = 0.0

    # ---------------------------------------------------------
    # Final Dashboard Statistics
    # ---------------------------------------------------------

    return {

        "total_students":
            total_students,

        "total_skills":
            total_skills,

        "total_case_studies":
            total_case_studies,

        "total_student_skills":
            total_student_skills,

        "average_engineering_score":
            engineering_score,

        "job_ready_students":
            job_ready_students,

        "ai_growth":
            ai_growth
    }


# =========================================================
# STUDENT AI DASHBOARD
# =========================================================

def student_dashboard(
    db: Session,
    student_id: int
):

    # ---------------------------------------------------------
    # Find Student
    # ---------------------------------------------------------

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if not student:
        return None

    # ---------------------------------------------------------
    # Find User
    # ---------------------------------------------------------

    user = (
        db.query(User)
        .filter(
            User.id == student.user_id
        )
        .first()
    )

    # ---------------------------------------------------------
    # Student Skills
    # ---------------------------------------------------------

    records = (
        db.query(StudentSkill)
        .filter(
            StudentSkill.student_id == student_id
        )
        .all()
    )

    skills = []

    for item in records:

        skill = (
            db.query(Skill)
            .filter(
                Skill.id == item.skill_id
            )
            .first()
        )

        if skill:

            skills.append({

                "name": skill.name,

                "score": float(
                    item.score or 0
                )

            })

    # ---------------------------------------------------------
    # Engineering Score
    # ---------------------------------------------------------

    if skills:

        total_score = sum(
            item["score"]
            for item in skills
        )

        engineering_score = round(
            total_score / len(skills),
            2
        )

    else:

        engineering_score = 0.0

    # ---------------------------------------------------------
    # Engineering Level
    # ---------------------------------------------------------

    if engineering_score >= 90:

        level = "Expert"

    elif engineering_score >= 80:

        level = "Advanced"

    elif engineering_score >= 70:

        level = "Intermediate"

    elif engineering_score >= 50:

        level = "Beginner"

    else:

        level = "Starter"

    # ---------------------------------------------------------
    # Job Readiness
    # ---------------------------------------------------------

    if engineering_score >= 90:

        readiness = "Job Ready"

    elif engineering_score >= 80:

        readiness = "Ready"

    elif engineering_score >= 70:

        readiness = "Almost Ready"

    elif engineering_score >= 50:

        readiness = "Learning"

    else:

        readiness = "Beginner"

    # ---------------------------------------------------------
    # AI Career Prediction
    # ---------------------------------------------------------

    current_skill_names = [
        item["name"].lower()
        for item in skills
    ]

    if (
        "machine learning" in current_skill_names
        and
        "python" in current_skill_names
    ):

        role = "Machine Learning Engineer"

    elif (
        "fastapi" in current_skill_names
        and
        "python" in current_skill_names
    ):

        role = "AI Backend Engineer"

    elif "react" in current_skill_names:

        role = "AI Full Stack Developer"

    elif "deep learning" in current_skill_names:

        role = "Deep Learning Engineer"

    elif "python" in current_skill_names:

        role = "Python AI Developer"

    else:

        role = "AI Engineer Intern"

    confidence = min(
        round(
            engineering_score + 5,
            2
        ),
        99
    )

    # ---------------------------------------------------------
    # Missing Skills
    # ---------------------------------------------------------

    missing_skills = []

    for required_skill in REQUIRED_SKILLS:

        exists = any(

            item["name"].lower()
            == required_skill.lower()

            for item in skills

        )

        if not exists:

            missing_skills.append(
                required_skill
            )

    # ---------------------------------------------------------
    # Learning Focus
    # ---------------------------------------------------------

    learning_focus = missing_skills[:5]

    if not learning_focus:

        learning_focus = [

            "Advanced Machine Learning",

            "Large Language Models",

            "MLOps",

            "Cloud Deployment",

            "AI System Design"

        ]

    # ---------------------------------------------------------
    # Case Studies
    # ---------------------------------------------------------

    case_records = (
        db.query(CaseStudy)
        .filter(
            CaseStudy.student_id == student_id
        )
        .all()
    )

    case_studies = []

    for case in case_records:

        case_studies.append({

            "id": case.id,

            "title": case.title,

            "technology":
                case.technology,

            "difficulty":
                case.difficulty,

            "status":
                case.status,

            "score":
                float(case.score or 0)

        })

    # ---------------------------------------------------------
    # Dynamic Internship Roadmap
    # ---------------------------------------------------------

    roadmap_topics = missing_skills[:8]

    if not roadmap_topics:

        roadmap_topics = [

            "Advanced Machine Learning",

            "Deep Learning",

            "LLM + RAG",

            "FastAPI",

            "React",

            "Docker",

            "Cloud Deployment",

            "AI Portfolio"

        ]

    roadmap = []

    for index, topic in enumerate(
        roadmap_topics,
        start=1
    ):

        roadmap.append({

            "week":
                f"Week {index}",

            "title":
                f"Learn {topic}"

        })

    # =========================================================
    # ACTUAL STUDENT EVALUATION METRICS
    # =========================================================

    attendance = float(
        student.attendance_percentage or 0
    )

    coding_speed = float(
        student.coding_speed or 0
    )

    interview_score = float(
        student.interview_score or 0
    )

    case_study_score = float(
        student.case_study_score or 0
    )

    # ---------------------------------------------------------
    # Final Student Dashboard
    # ---------------------------------------------------------

    return {

        "student_id":
            student.id,

        "name": (

            user.full_name

            if user

            else
            f"Student {student.id}"

        ),

        "email": (

            user.email

            if user

            else
            "Not Available"

        ),

        "engineering_score":
            engineering_score,

        "level":
            level,

        "job_readiness":
            readiness,

        "skills":
            skills,

        "skill_count":
            len(skills),

        "roadmap_available":
            True,

        # Actual evaluation data

        "attendance":
            attendance,

        "coding_speed":
            coding_speed,

        "interview_score":
            interview_score,

        "case_study_score":
            case_study_score,

        "career_prediction": {

            "role":
                role,

            "confidence":
                confidence

        },

        "learning_focus":
            learning_focus,

        "missing_skills":
            missing_skills,

        "case_studies":
            case_studies,

        "roadmap":
            roadmap

    }