class ExperienceMatchingService:

    """A blueprint that matches experience of candidate with the JD"""

    def calculate_total_experience(self, experiences: list) -> float:

        total_experience = 0.0

        for experience in experiences:

            if experience.years is not None:
                total_experience += experience.years

        return total_experience

    def calculate_experience_score(
        self,
        required_experience: float | None,
        experiences: list
    ) -> float:

        if required_experience is None or required_experience == 0:
            return 15.0

        candidate_experience = self.calculate_total_experience(
            experiences
        )

        score = (
            candidate_experience / required_experience
        ) * 15

        return min(score, 15.0)