from core.normalization_service import NormalizationService

from core.embeddings_service import EmbeddingsService

class SkillMatchingService():

    """A blueprint for matching candidate skills with JD skills"""

    def __init__(self):

        self.embedding_service = EmbeddingsService()

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

    def calculate_similarity(self,text1:str,text2:str) -> float:

        embedding1 = self.embedding_service.create_embedding(text1)

        embedding2 = self.embedding_service.create_embedding(text2)

        return float(embedding1 @ embedding2)

    def find_semantic_matches(self,jd_skills:list[str],resume_skills:list[str],threshold:float = 0.50) -> list[str]:

        semantic_matches = []

        for jd_skill in jd_skills:

            best_score = 0

            for resume_skill in resume_skills:

                score = self.calculate_similarity(jd_skill,resume_skill)

                if score > best_score:

                    best_score = score

            if best_score >= threshold:

                semantic_matches.append(jd_skill)

        return semantic_matches

    def calculate_skill_score(self,jd_skills: list[str],resume_skills: list[str],weight: float) -> float:

        if not jd_skills:
            return weight

        matched_count = 0

        normalized_candidate_skills = {
            NormalizationService.normalize_skill(skill)
            for skill in resume_skills
        }

        for jd_skill in jd_skills:

            normalized_jd_skill = NormalizationService.normalize_skill(jd_skill)

            if normalized_jd_skill in normalized_candidate_skills:
                matched_count += 1
                continue

            best_score = 0.0

            for resume_skill in resume_skills:

                score = self.calculate_similarity(jd_skill,resume_skill)

                if score > best_score:
                    best_score = score

            if best_score >= 0.50:
                matched_count += 1

        match_ratio = matched_count / len(jd_skills)

        return match_ratio * weight