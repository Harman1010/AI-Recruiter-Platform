from core.embeddings_service import EmbeddingsService

class ProjectMatchingService():

    """A blueprint for selecting best project for each requirement for efficient allocation of project weightage"""

    def __init__(self):

        self.service = EmbeddingsService()

    def calculate_similarity(self,text1:str,text2:str) -> float:

        embedding1 = self.service.create_embedding(text1)

        embedding2 = self.service.create_embedding(text2)

        return float(embedding1 @ embedding2)

    def get_best_result(self,requirement:str,projects:list[str]):

        best_score = 0.0
        best_project = ""

        for project in projects:

            score = self.calculate_similarity(requirement,project.description)

            if score > best_score:

                best_score = score
                best_project = project

        return best_project,best_score

    def calculate_requirement_score(self,requirements: list[str],projects: list) -> float:

        if not requirements:
            return 1.0

        scores = []

        for r in requirements:

            _, best_score = self.get_best_result(r,projects)

            scores.append(best_score)

        return sum(scores) / len(scores)

        
    def calculate_project_score(self,responsibilities:list[str],required_skills:list[str],preferred_skills:list[str],projects
                                :list[str]) -> float:

        responsibility_score = self.calculate_requirement_score(responsibilities,projects)

        required_skills_score = self.calculate_requirement_score(required_skills,projects)

        preferred_skills_score = self.calculate_requirement_score(preferred_skills,projects)

        answer = responsibility_score * 0.60 + required_skills_score * 0.25 + preferred_skills_score * 0.15

        return answer * 40