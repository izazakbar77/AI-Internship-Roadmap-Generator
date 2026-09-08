from typing import List


class RecommendationEngine:

    # ==========================================================
    # ENGINEERING SCORE
    # ==========================================================

    @staticmethod
    def calculate_engineering_score(
        attendance: float,
        coding_speed: int,
        interview_score: int,
        case_study_score: int,
        skills: List[int],
    ):

        skill_score = (
            sum(skills) / len(skills)
            if skills
            else 0
        )

        engineering_score = (
            attendance * 0.20
            + coding_speed * 0.20
            + interview_score * 0.20
            + case_study_score * 0.20
            + skill_score * 0.20
        )

        return round(engineering_score, 2)

    # ==========================================================
    # ENGINEERING LEVEL
    # ==========================================================

    @staticmethod
    def engineering_level(score: float):

        if score >= 90:
            return "Expert"

        if score >= 80:
            return "Advanced"

        if score >= 70:
            return "Intermediate"

        if score >= 50:
            return "Beginner"

        return "Starter"

    # ==========================================================
    # JOB READINESS
    # ==========================================================

    @staticmethod
    def job_readiness(score: float):

        if score >= 90:
            return "Job Ready"

        if score >= 80:
            return "Almost Ready"

        if score >= 70:
            return "Need Practice"

        return "Learning Phase"

    # ==========================================================
    # PROMOTION READINESS
    # ==========================================================

    @staticmethod
    def promotion_readiness(score: float):

        if score >= 85:
            return "Ready"

        if score >= 70:
            return "Almost Ready"

        return "Not Ready"

    # ==========================================================
    # NORMALIZE SKILL NAME
    # ==========================================================

    @staticmethod
    def normalize_skill(skill: str):

        skill = skill.strip().lower()

        aliases = {

            "programming languages": "python",
            "programming language": "python",

            "github": "git",

            "data structures & algorithms":
                "data structures",

            "data structures and algorithms":
                "data structures",

            "technology development":
                "software development",

            "software projects":
                "software development",

            "machine learning":
                "machine learning",

            "deep learning":
                "deep learning",

            "large language models":
                "llm",

            "large language model":
                "llm",

            "rag":
                "rag",

            "mlops":
                "mlops",

            "ci/cd":
                "ci/cd",

            "sql":
                "sql",

            "fastapi":
                "fastapi",

            "docker":
                "docker",

            "react":
                "react",

            "python":
                "python",
        }

        return aliases.get(skill, skill)

    # ==========================================================
    # MISSING SKILLS
    # ==========================================================

    @staticmethod
    def missing_skills(skills: List[str]):

        required = [

            "Python",
            "Machine Learning",
            "Deep Learning",
            "FastAPI",
            "SQL",
            "Git",
            "Docker",
            "React",
            "Large Language Models",
            "RAG",
            "MLOps",
            "CI/CD",
        ]

        student_skills = {
            RecommendationEngine.normalize_skill(skill)
            for skill in skills
        }

        missing = []

        for required_skill in required:

            normalized = (
                RecommendationEngine
                .normalize_skill(required_skill)
            )

            if normalized not in student_skills:
                missing.append(required_skill)

        return missing

    # ==========================================================
    # RECOMMENDED ROLE
    # ==========================================================

    @staticmethod
    def recommended_role(
        score: float,
        skills: List[str],
    ):

        normalized = {
            RecommendationEngine.normalize_skill(skill)
            for skill in skills
        }

        if (
            score >= 85
            and "machine learning" in normalized
            and "python" in normalized
        ):
            return "AI Engineer Intern"

        if (
            score >= 75
            and "machine learning" in normalized
        ):
            return "Machine Learning Engineer Intern"

        if (
            score >= 65
            and "python" in normalized
        ):
            return "Machine Learning Intern"

        if score >= 50:
            return "AI Developer Intern"

        return "AI Beginner Intern"

    # ==========================================================
    # PROJECT RECOMMENDATIONS
    # ==========================================================

    @staticmethod
    def recommended_projects(
        score: float,
        missing_skills: List[str],
    ):

        projects = []

        missing = {
            skill.lower()
            for skill in missing_skills
        }

        if "machine learning" in missing:

            projects.append(
                "Machine Learning Prediction System"
            )

        if "large language models" in missing:

            projects.append(
                "AI Chatbot with LLM"
            )

        if "rag" in missing:

            projects.append(
                "RAG Based Question Answering System"
            )

        if "fastapi" in missing:

            projects.append(
                "AI FastAPI Backend"
            )

        if "docker" in missing:

            projects.append(
                "Dockerized AI Application"
            )

        if not projects:

            projects = [

                "AI Workflow Automation Platform",

                "RAG Document Intelligence System",

                "AI Career Assistant",
            ]

        return projects[:3]

    # ==========================================================
    # LEARNING PRIORITY
    # ==========================================================

    @staticmethod
    def learning_priority(
        missing_skills: List[str],
    ):

        priority_order = [

            "Machine Learning",
            "Deep Learning",
            "FastAPI",
            "SQL",
            "Git",
            "Docker",
            "Large Language Models",
            "RAG",
            "MLOps",
            "CI/CD",
            "React",
        ]

        missing_set = {
            skill.lower()
            for skill in missing_skills
        }

        priority = []

        for skill in priority_order:

            if skill.lower() in missing_set:

                priority.append(skill)

        return priority[:5]