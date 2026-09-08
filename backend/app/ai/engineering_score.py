class EngineeringScore:

    @staticmethod
    def calculate(
        attendance,
        coding_speed,
        interview,
        case_study,
        skills
    ):

        if len(skills) == 0:
            avg_skill = 0
        else:
            avg_skill = sum(skills) / len(skills)

        score = (
            attendance * 0.20 +
            coding_speed * 0.20 +
            interview * 0.20 +
            case_study * 0.20 +
            avg_skill * 0.20
        )

        return round(score, 2)