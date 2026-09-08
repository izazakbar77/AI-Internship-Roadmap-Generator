from pathlib import Path
import math
import pandas as pd

from app.database import SessionLocal, create_tables
from app.models.user import User
from app.models.student import Student
from app.models.skill import Skill
from app.models.student_skill import StudentSkill


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "Studentdata .csv"

# Test-only password for the generated dataset accounts.
TEST_PASSWORD = "Dataset@123"


def score_level(value):
    value = str(value).strip().lower()
    return {
        "easy": 35,
        "medium": 65,
        "hard": 90,
    }.get(value, 0)


def yes_no_score(value):
    return 90 if str(value).strip().lower() == "yes" else 20


def year_to_semester(value):
    return {
        "first": 1,
        "second": 3,
        "third": 5,
    }.get(str(value).strip().lower(), 1)


def percentage_score(value):
    value = str(value).strip().lower()
    if ">= 90" in value or ">=90" in value:
        return 95
    if ">=80" in value:
        return 85
    if ">=70" in value:
        return 75
    if ">=60" in value:
        return 65
    if "<60" in value:
        return 50
    return 0


def language_score(value):
    value = str(value).strip().lower()
    return {
        "1": 25,
        "2-3": 50,
        "4-5": 75,
        "more than 5": 95,
    }.get(value, 0)


def hackathon_score(value):
    value = str(value).strip().lower()
    if "won" in value:
        return 100
    if value == "participated":
        return 75
    return 20


def community_score(value):
    value = str(value).strip().lower()
    return {
        "active member": 90,
        "moderately active": 65,
        "inactive member": 35,
    }.get(value, 20)


def technology_score(value):
    value = str(value).strip().lower()
    if not value or value == "none":
        return 15

    score = 20
    if "development" in value:
        score += 25
    if "research" in value:
        score += 20
    if "designing" in value:
        score += 15
    if "competitive coding" in value:
        score += 20

    return min(score, 100)


def level_from_score(score):
    if score >= 80:
        return "Advanced"
    if score >= 50:
        return "Intermediate"
    return "Beginner"


def add_skill(db, name, category, difficulty, description):
    skill = db.query(Skill).filter(Skill.name == name).first()

    if not skill:
        skill = Skill(
            name=name,
            category=category,
            difficulty=difficulty,
            description=description,
        )
        db.add(skill)
        db.flush()

    return skill


def add_student_skill(db, student_id, skill_id, score):
    existing = (
        db.query(StudentSkill)
        .filter(
            StudentSkill.student_id == student_id,
            StudentSkill.skill_id == skill_id,
        )
        .first()
    )

    if existing:
        existing.score = int(score)
        existing.level = level_from_score(int(score))
    else:
        db.add(
            StudentSkill(
                student_id=student_id,
                skill_id=skill_id,
                score=int(score),
                level=level_from_score(int(score)),
            )
        )


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"CSV not found:\n{CSV_PATH}\n\n"
            "Make sure Studentdata .csv is inside backend/data/"
        )

    print("Creating/checking database tables...")
    create_tables()

    df = pd.read_csv(CSV_PATH)

    print(f"CSV loaded: {len(df)} students, {len(df.columns)} columns")

    db = SessionLocal()

    try:
        # Core skills used by the roadmap engine.
        skill_defs = {
            "Programming Languages": (
                "Programming",
                "Intermediate",
                "Number of programming languages known",
            ),
            "Data Structures & Algorithms": (
                "Computer Science",
                "Advanced",
                "Exposure to data structures and algorithms",
            ),
            "GitHub": (
                "Development",
                "Intermediate",
                "GitHub exposure and practical usage",
            ),
            "Technology Development": (
                "Technology",
                "Intermediate",
                "Hands-on involvement in development technologies",
            ),
            "Research": (
                "AI/Research",
                "Advanced",
                "Involvement in research activities",
            ),
            "Design": (
                "Design",
                "Intermediate",
                "Involvement in designing activities",
            ),
            "Competitive Coding": (
                "Programming",
                "Advanced",
                "Participation in competitive coding",
            ),
            "Developer Community": (
                "Professional",
                "Intermediate",
                "Participation in developer communities",
            ),
            "Hackathons": (
                "Professional",
                "Advanced",
                "Hackathon and competition participation",
            ),
            "Software Projects": (
                "Projects",
                "Intermediate",
                "Experience building software projects",
            ),
            "Hardware Projects": (
                "Projects",
                "Intermediate",
                "Experience building hardware projects",
            ),
            "Idea Pitching": (
                "Entrepreneurship",
                "Intermediate",
                "Experience pitching ideas",
            ),
            "Academic Performance": (
                "Academic",
                "Intermediate",
                "Academic performance based on school percentages",
            ),
            "Photography": (
                "Additional",
                "Beginner",
                "Photography as an additional skill",
            ),
            "Video Editing": (
                "Additional",
                "Intermediate",
                "Video editing as an additional skill",
            ),
            "Sports": (
                "Additional",
                "Beginner",
                "Sports as an additional skill",
            ),
            "Cultural Activities": (
                "Additional",
                "Beginner",
                "Participation in cultural activities",
            ),
        }

        skills = {}
        for name, (category, difficulty, description) in skill_defs.items():
            skills[name] = add_skill(
                db, name, category, difficulty, description
            )

        db.commit()

        created_users = 0
        created_students = 0
        created_student_skills = 0

        for index, row in df.iterrows():
            number = index + 1

            username = f"kaggle_student_{number:03d}"
            email = f"kaggle.student.{number:03d}@example.com"
            full_name = f"Kaggle Student {number:03d}"

            # User
            user = db.query(User).filter(User.username == username).first()

            if not user:
                user = User(
                    full_name=full_name,
                    username=username,
                    email=email,
                    password=TEST_PASSWORD,
                    role="Student",
                    is_active=True,
                )
                db.add(user)
                db.flush()
                created_users += 1

            # Student
            student = db.query(Student).filter(Student.user_id == user.id).first()

            branch = str(row.get("4. Branch", "Computer Science"))
            year = str(row.get("3. Year of Study", "First"))

            academic_10 = percentage_score(row.get("2. Percentage in Class 10th?", ""))
            academic_12 = percentage_score(row.get("5. Percentage in Class 12th?", ""))
            academic_score = round((academic_10 + academic_12) / 2)

            dsa_score = score_level(row.get("3. Exposure to Data structure and algorithms?", ""))
            github_score = score_level(row.get("4. Exposure to GitHub ?", ""))
            languages = language_score(row.get("1. How many programming languages do you know? ", ""))

            technology = str(
                row.get("2.  Actively involved in Specific technology?", "")
            )
            tech_score = technology_score(technology)

            community = str(row.get("6. Active in developer Communities", ""))
            community_score_value = community_score(community)

            hackathon = str(
                row.get("7. Participating in Hackathons and other competitions?", "")
            )
            hackathon_score_value = hackathon_score(hackathon)

            software_score = yes_no_score(
                row.get("8. Have you made any Software based projects?", "No")
            )
            hardware_score = yes_no_score(
                row.get(
                    "9. Have you made any Hardware based project (Arduino, Raspberry Pi, Robots or any other)?",
                    "No",
                )
            )
            pitch_score = yes_no_score(
                row.get("10. Have you ever pitched any idea?", "No")
            )

            coding_speed = round((languages + dsa_score) / 2)

            if dsa_score >= 80 or languages >= 75:
                engineering_level = "Advanced"
            elif dsa_score >= 50 or languages >= 50:
                engineering_level = "Intermediate"
            else:
                engineering_level = "Beginner"

            tech_lower = technology.lower()
            if "research" in tech_lower:
                internship_goal = "AI / Research Internship"
            elif "designing" in tech_lower:
                internship_goal = "Software / Product Internship"
            elif "competitive coding" in tech_lower:
                internship_goal = "Software Engineering Internship"
            else:
                internship_goal = "Software Development Internship"

            if not student:
                student = Student(
                    user_id=user.id,
                    university="Kaggle Student Dataset",
                    degree=branch,
                    semester=year_to_semester(year),
                    engineering_level=engineering_level,
                    coding_speed=coding_speed,
                    attendance_percentage=0,
                    internship_goal=internship_goal,
                )
                db.add(student)
                db.flush()
                created_students += 1
            else:
                student.university = "Kaggle Student Dataset"
                student.degree = branch
                student.semester = year_to_semester(year)
                student.engineering_level = engineering_level
                student.coding_speed = coding_speed
                student.internship_goal = internship_goal

            # Main skill scores
            skill_scores = {
                "Programming Languages": languages,
                "Data Structures & Algorithms": dsa_score,
                "GitHub": github_score,
                "Technology Development": tech_score,
                "Developer Community": community_score_value,
                "Hackathons": hackathon_score_value,
                "Software Projects": software_score,
                "Hardware Projects": hardware_score,
                "Idea Pitching": pitch_score,
                "Academic Performance": academic_score,
            }

            # Technology-specific skills
            if "development" in tech_lower:
                skill_scores["Technology Development"] = max(
                    skill_scores["Technology Development"], 80
                )
            if "research" in tech_lower:
                skill_scores["Research"] = 80
            if "designing" in tech_lower:
                skill_scores["Design"] = 80
            if "competitive coding" in tech_lower:
                skill_scores["Competitive Coding"] = 80

            # Additional skills from the CSV
            additional = str(
                row.get("11. Do you have any additional skills?", "")
            )

            for extra_skill, skill_name in [
                ("photography", "Photography"),
                ("video editing", "Video Editing"),
                ("sports", "Sports"),
                ("cultural activities", "Cultural Activities"),
            ]:
                if extra_skill in additional.lower():
                    skill_scores[skill_name] = 80

            for skill_name, score in skill_scores.items():
                add_student_skill(
                    db,
                    student.id,
                    skills[skill_name].id,
                    score,
                )
                created_student_skills += 1

            # Commit every 25 students so a large import is safer.
            if number % 25 == 0:
                db.commit()
                print(f"Imported {number}/{len(df)} students...")

        db.commit()

        print("\n======================================")
        print("DATASET IMPORT COMPLETE")
        print("======================================")
        print(f"CSV students:       {len(df)}")
        print(f"Users created:      {created_users}")
        print(f"Students created:   {created_students}")
        print(f"Skill links handled: {created_student_skills}")
        print(f"Database:            {BASE_DIR / 'ai_roadmap.db'}")
        print("======================================")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()