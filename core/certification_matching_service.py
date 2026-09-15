from core.embeddings_service import EmbeddingsService

class CertificationMatchingService:

    """A blueprint for matching candidate certifications with JD requirements."""

    def __init__(self):

        self.embedding_service = EmbeddingsService()

    def calculate_similarity(self,text1: str,text2: str) -> float:

        embedding1 = self.embedding_service.create_embedding(text1)
        embedding2 = self.embedding_service.create_embedding(text2)

        return float(embedding1 @ embedding2)

    def get_best_result(self,requirement: str,certifications: list):

        best_score = 0.0
        best_certification = None

        for certification in certifications:

            candidate_certification = (
                f"{certification.name} "
                f"{certification.issuer}"
            )

            score = self.calculate_similarity(
                requirement,
                candidate_certification
            )

            if score > best_score:

                best_score = score
                best_certification = certification

        return best_certification, best_score

    def calculate_certification_score(self, requirements: list[str], certifications: list) -> float:

        if not requirements:
            return 5.0

        scores = []

        for requirement in requirements:

            _, best_score = self.get_best_result(
                requirement,
                certifications
            )

            scores.append(best_score)

        average_score = sum(scores) / len(scores)

        return average_score * 5
