class JobReadiness:

    @staticmethod
    def level(score):

        if score >= 90:
            return "Job Ready"

        elif score >= 80:
            return "Almost Ready"

        elif score >= 70:
            return "Need Practice"

        elif score >= 50:
            return "Learning"

        return "Beginner"