from core.candidate_scoring_service import CandidateScoringService

class RankingService():

    "A blueprint for ranking multiple candidates against a JD"

    def __init__(self):
        
        self.scoring_service = CandidateScoringService()

    def rank_candidates(self,jd,candidates:list) -> list:

        ranked_candidates = []

        for candidate in candidates:

            score = self.scoring_service.calculate_score(jd,candidate)

            ranked_candidates.append({
                "candidate" : candidate,
                "score" : score
                })

        ranked_candidates.sort(key=lambda x:x["score"],reverse=True)
        return ranked_candidates

        