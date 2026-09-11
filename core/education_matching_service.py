from core.embeddings_service import EmbeddingsService


class EducationMatchingService:

    """A blueprint for matching candidate education with JD requirements."""

    def __init__(self):

        self.embedding_service = EmbeddingsService()

    def calculate_education_score(self,education_requirement: str | None,candidate_education: list) -> float:

        if education_requirement is None or not candidate_education:
            return 0.0

        best_score = 0.0

        for education in candidate_education:

            candidate_text = (
                f"{education.degree} "
                f"{education.field}"
            )

            score = self._calculate_similarity(
                education_requirement,
                candidate_text
            )

            if score > best_score:
                best_score = score

        return best_score * 10

    def _calculate_similarity(self,text1: str,text2: str) -> float:

        embedding1 = self.embedding_service.create_embedding(text1)

        embedding2 = self.embedding_service.create_embedding(text2)

        return float(embedding1 @ embedding2)