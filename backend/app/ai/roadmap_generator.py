class RoadmapGenerator:


    @staticmethod
    def generate(
        level,
        missing_skills,
        target_role="AI Engineer",
        duration=3
    ):


        roadmap = []

        weekly_goals = []

        monthly_goals = []



        # Missing skills based roadmap

        if missing_skills:


            for skill in missing_skills:


                roadmap.append(
                    f"Learn {skill}"
                )


                weekly_goals.append(
                    f"Complete {skill} Basics and Practice"
                )


                monthly_goals.append(
                    f"Build one project using {skill}"
                )


        else:


            weekly_goals.extend(
                [
                    "Practice AI Programming",
                    "Improve Problem Solving",
                    "Complete Coding Tasks"
                ]
            )


            monthly_goals.extend(
                [
                    "Build AI Based Project",
                    "Create Portfolio",
                    "Prepare Internship Applications"
                ]
            )



        # Engineering Level Based Roadmap


        if level == "Starter":


            recommended_case = (
                "Python Fundamentals"
            )


            recommended_projects = [

                "Python Automation Tool",

                "Basic AI Assistant"

            ]


            technology_dependencies = [

                "Python",

                "Git",

                "Programming Fundamentals"

            ]


            roadmap.extend(

                [

                    "Python Programming",

                    "Programming Logic",

                    "Basic AI Concepts"

                ]

            )



        elif level == "Beginner":


            recommended_case = (
                "REST API Development"
            )


            recommended_projects = [

                "FastAPI Backend Project",

                "Database Management System"

            ]


            technology_dependencies = [

                "Python",

                "FastAPI",

                "SQL",

                "GitHub"

            ]


            roadmap.extend(

                [

                    "Python Advanced Concepts",

                    "FastAPI Development",

                    "Database Integration"

                ]

            )



        elif level == "Intermediate":


            recommended_case = (
                "AI Recommendation Engine"
            )


            recommended_projects = [

                "Machine Learning Prediction Model",

                "AI Dashboard",

                "Recommendation System"

            ]


            technology_dependencies = [

                "Python",

                "Pandas",

                "Scikit-learn",

                "FastAPI"

            ]


            roadmap.extend(

                [

                    "Machine Learning",

                    "Data Processing",

                    "AI Model Integration"

                ]

            )



        elif level == "Advanced":


            recommended_case = (
                "Workflow Automation System"
            )


            recommended_projects = [

                "LLM Based AI Assistant",

                "RAG Document Intelligence System",

                "AI Workflow Automation Platform"

            ]


            technology_dependencies = [

                "Python",

                "FastAPI",

                "LangChain",

                "Vector Database",

                "Cloud Deployment"

            ]


            roadmap.extend(

                [

                    "LLM Application Development",

                    "RAG Systems",

                    "AI Deployment"

                ]

            )



        else:


            recommended_case = (
                "Enterprise AI Project"
            )


            recommended_projects = [

                "Enterprise AI Solution"

            ]


            technology_dependencies = [

                "Python",

                "AI Architecture"

            ]


            roadmap.append(

                "Enterprise Level AI Architecture"

            )




        return {


            "target_role": target_role,


            "engineering_level": level,


            "weekly_goals": weekly_goals,


            "monthly_goals": monthly_goals,


            "recommended_projects": recommended_projects,


            "recommended_case_study": recommended_case,


            "technology_dependencies": technology_dependencies,


            "missing_skills": missing_skills,


            "estimated_graduation": f"{duration} Months",


            "roadmap": roadmap

        }