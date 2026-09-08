def generate_recommendation(data):

    # ============================================================
    # INPUT DATA
    # ============================================================

    skills = data.skills or []
    scores = data.skill_scores or []

    attendance = float(data.attendance or 0)
    coding_speed = float(data.coding_speed or 0)
    interview_score = float(data.interview_score or 0)
    case_study_score = float(data.case_study_score or 0)

    # Normalize lengths
    skill_count = min(len(skills), len(scores))

    skill_data = []

    for i in range(skill_count):

        skill_name = str(skills[i]).strip()
        skill_score = float(scores[i] or 0)

        skill_data.append({
            "name": skill_name,
            "score": skill_score
        })


    # ============================================================
    # SKILL SCORE
    # ============================================================

    if skill_data:

        skill_average = sum(
            item["score"]
            for item in skill_data
        ) / len(skill_data)

    else:

        skill_average = 0


    # ============================================================
    # OVERALL ENGINEERING SCORE
    # ============================================================
    #
    # 40% Technical Skills
    # 15% Attendance
    # 15% Coding Speed
    # 15% Interview
    # 15% Case Study
    #
    # This makes the score reflect the complete student profile.
    # ============================================================

    engineering_score = round(

        (
            skill_average * 0.40
            +
            attendance * 0.15
            +
            coding_speed * 0.15
            +
            interview_score * 0.15
            +
            case_study_score * 0.15
        ),

        2

    )


    # ============================================================
    # ENGINEERING LEVEL
    # ============================================================

    if engineering_score >= 80:

        engineering_level = "Advanced"

    elif engineering_score >= 65:

        engineering_level = "Intermediate"

    else:

        engineering_level = "Beginner"


    # ============================================================
    # JOB READINESS
    # ============================================================

    if engineering_score >= 80:

        job_readiness = "Ready"

    elif engineering_score >= 65:

        job_readiness = "Almost Ready"

    elif engineering_score >= 50:

        job_readiness = "Need Practice"

    else:

        job_readiness = "Learning Phase"


    # ============================================================
    # PROMOTION READINESS
    # ============================================================

    if engineering_score >= 85:

        promotion_readiness = "Ready"

    elif engineering_score >= 70:

        promotion_readiness = "Almost Ready"

    elif engineering_score >= 55:

        promotion_readiness = "Developing"

    else:

        promotion_readiness = "Not Ready"


    # ============================================================
    # NORMALIZE SKILL NAMES
    # ============================================================

    normalized_skills = {}

    for item in skill_data:

        name = item["name"].lower().strip()

        normalized_skills[name] = item["score"]


    # ============================================================
    # SKILL ALIASES
    # ============================================================

    aliases = {

        "programming languages":
            ["python", "programming languages"],

        "data structures & algorithms":
            [
                "data structures",
                "data structures & algorithms",
                "dsa"
            ],

        "github":
            ["github", "git"],

        "technology development":
            [
                "technology development",
                "software development"
            ],

        "software projects":
            ["software projects"],

        "machine learning":
            ["machine learning", "ml"],

        "fastapi":
            ["fastapi"],

        "sql":
            ["sql", "database"],

        "deep learning":
            ["deep learning"],

        "large language models":
            [
                "large language models",
                "llm",
                "llms"
            ],

        "docker":
            ["docker"],

        "react":
            ["react"],

        "ci/cd":
            ["ci/cd", "cicd"],

        "mlops":
            ["mlops"]

    }


    # ============================================================
    # GET SKILL SCORE
    # ============================================================

    def get_skill_score(skill_name):

        possible_names = aliases.get(
            skill_name.lower(),
            [skill_name.lower()]
        )

        for name in possible_names:

            if name in normalized_skills:

                return normalized_skills[name]

        return None


    # ============================================================
    # REQUIRED SKILLS
    # ============================================================

    required_skills = [

        "Python",
        "Data Structures & Algorithms",
        "Git",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "FastAPI",
        "Large Language Models",
        "Docker",
        "MLOps",
        "React",
        "CI/CD"

    ]


    # ============================================================
    # MISSING / WEAK SKILLS
    # ============================================================

    missing_skills = []

    weak_skills = []


    for skill in required_skills:

        score = get_skill_score(skill)

        # Completely missing
        if score is None:

            missing_skills.append(skill)

        # Present but weak
        elif score < 60:

            weak_skills.append(skill)


    # ============================================================
    # COMBINE MISSING + WEAK
    # ============================================================

    learning_priority = []


    for skill in missing_skills:

        if skill not in learning_priority:

            learning_priority.append(skill)


    for skill in weak_skills:

        if skill not in learning_priority:

            learning_priority.append(skill)


    # ============================================================
    # PRIORITY ORDER
    # ============================================================

    priority_order = [

        "Python",
        "Data Structures & Algorithms",
        "Git",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "FastAPI",
        "Large Language Models",
        "Docker",
        "MLOps",
        "React",
        "CI/CD"

    ]


    learning_priority = sorted(

        learning_priority,

        key=lambda x:
        priority_order.index(x)
        if x in priority_order
        else 999

    )


    # ============================================================
    # RECOMMENDED ROLE
    # ============================================================

    ml_score = get_skill_score("Machine Learning") or 0
    dl_score = get_skill_score("Deep Learning") or 0
    python_score = get_skill_score("Python") or 0
    fastapi_score = get_skill_score("FastAPI") or 0
    llm_score = get_skill_score("Large Language Models") or 0
    react_score = get_skill_score("React") or 0


    if (

        engineering_score >= 80
        and
        python_score >= 75
        and
        ml_score >= 75
        and
        llm_score >= 70

    ):

        recommended_role = "AI Engineer"


    elif (

        ml_score >= 70
        and
        python_score >= 70

    ):

        recommended_role = "Machine Learning Engineer"


    elif (

        python_score >= 65
        and
        fastapi_score >= 65

    ):

        recommended_role = "AI Backend Engineer"


    elif (

        react_score >= 70
        and
        python_score >= 60

    ):

        recommended_role = "AI Full Stack Developer"


    elif engineering_score >= 65:

        recommended_role = "AI Engineer Intern"


    else:

        recommended_role = "AI/ML Beginner Intern"


    # ============================================================
    # RECOMMENDED PROJECTS
    # ============================================================

    recommended_projects = []


    if ml_score >= 60:

        recommended_projects.append(
            "Machine Learning Prediction System"
        )


    if llm_score >= 60:

        recommended_projects.append(
            "LLM Based AI Assistant"
        )

    else:

        recommended_projects.append(
            "AI Chatbot"
        )


    if fastapi_score >= 60:

        recommended_projects.append(
            "AI REST API with FastAPI"
        )


    if engineering_score >= 65:

        recommended_projects.append(
            "RAG Based Question Answering System"
        )


    if not recommended_projects:

        recommended_projects = [

            "Python AI Starter Project",

            "Machine Learning Prediction System",

            "Data Analysis Dashboard"

        ]


    # Remove duplicates
    recommended_projects = list(
        dict.fromkeys(recommended_projects)
    )


    # Keep maximum 4
    recommended_projects = recommended_projects[:4]


    # ============================================================
    # FINAL RESPONSE
    # ============================================================

    return {

        "engineering_score":
            engineering_score,

        "engineering_level":
            engineering_level,

        "job_readiness":
            job_readiness,

        "promotion_readiness":
            promotion_readiness,

        "missing_skills":
            learning_priority,

        "recommended_role":
            recommended_role,

        "recommended_projects":
            recommended_projects,

        "learning_priority":
            learning_priority[:6]

    }