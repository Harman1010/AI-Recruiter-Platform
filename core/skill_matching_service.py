from core.normalization_service import NormalizationService

class SkillMatchingService():

    """A blueprint for matching candidate skills with JD skills"""

    @staticmethod

    def find_matches(jd_skills:list[str],resume_skills:list[str]) -> list[str]:

        normalized_candidate_skills = {

            NormalizationService.normalize_skill(skill) 

            for skill in resume_skills

        }

        matches = []

        for skill in jd_skills:

            normalized_jd_skill = NormalizationService.normalize_skill(skill)

            if normalized_jd_skill in normalized_candidate_skills:

                matches.append(normalized_jd_skill)

        return matches

    def calculate_skill_score(jd_skills: list[str],resume_skills: list[str]) -> float:

        if not jd_skills:
            return 25.0

        matches = SkillMatchingService.find_matches(
            jd_skills,
            resume_skills
        )

        match_ratio = len(matches) / len(jd_skills)

        return match_ratio * 25



