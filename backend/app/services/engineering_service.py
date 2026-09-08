from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.student_skill import StudentSkill
from app.models.skill import Skill



def calculate_engineering_level(
        db: Session,
        student_id: int
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )


    if not student:
        return None



    records = (
        db.query(StudentSkill)
        .filter(
            StudentSkill.student_id == student_id
        )
        .all()
    )


    total_score = 0

    skills = []


    for item in records:

        total_score += item.score


        skill = (
            db.query(Skill)
            .filter(Skill.id == item.skill_id)
            .first()
        )


        if skill:
            skills.append(
                skill.name
            )


    if records:

        engineering_score = round(
            total_score / len(records),
            2
        )

    else:

        engineering_score = 0



    if engineering_score >= 80:

        level = "Advanced"

        role = "AI Engineer"

        focus = "Deep Learning"

    elif engineering_score >= 50:

        level = "Intermediate"

        role = "Software Engineer"

        focus = "Machine Learning"

    else:

        level = "Beginner"

        role = "Python Developer"

        focus = "Programming Fundamentals"



    weaknesses = []


    if engineering_score < 80:

        weaknesses.append(
            "Improve technical skills"
        )


    return {

        "student_id": student.id,

        "engineering_level": level,

        "engineering_score": engineering_score,

        "strengths": skills,

        "weaknesses": weaknesses,

        "recommended_role": role,

        "next_focus": focus

    }