class SkillTree:


    roadmap = {

        "Python": {
            "level": "Intermediate",
            "topics": [
                "OOP",
                "File Handling",
                "FastAPI",
                "Flask",
                "SQLAlchemy"
            ]
        },


        "React": {
            "level": "Intermediate",
            "topics": [
                "Hooks",
                "Redux",
                "Context API",
                "Next.js"
            ]
        },


        "FastAPI": {
            "level": "Advanced",
            "topics": [
                "JWT Authentication",
                "CRUD APIs",
                "Deployment",
                "Docker"
            ]
        },


        "Machine Learning": {
            "level": "Intermediate",
            "topics": [
                "NumPy",
                "Pandas",
                "Scikit-learn",
                "TensorFlow"
            ]
        },


        "Git": {
            "level": "Beginner",
            "topics": [
                "GitHub",
                "Branching",
                "Merge",
                "CI/CD"
            ]
        },


        "Deep Learning": {
            "level": "Advanced",
            "topics": [
                "Neural Networks",
                "CNN",
                "RNN",
                "Transformers"
            ]
        }

    }



    @staticmethod
    def generate(skills):

        result = []

        for skill in skills:

            if skill in SkillTree.roadmap:

                result.append({

                    "skill": skill,

                    "level": SkillTree.roadmap[skill]["level"],

                    "next_topics": SkillTree.roadmap[skill]["topics"]

                })


        return result



    @staticmethod
    def calculate_level(skills):

        levels = []


        for skill in skills:

            if skill in SkillTree.roadmap:

                levels.append(
                    SkillTree.roadmap[skill]["level"]
                )


        if "Advanced" in levels:
            return "Advanced"

        elif "Intermediate" in levels:
            return "Intermediate"

        else:
            return "Beginner"