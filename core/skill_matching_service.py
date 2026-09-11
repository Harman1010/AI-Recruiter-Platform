from core.normalization_service import NormalizationService

class SkillMatchinService():

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



