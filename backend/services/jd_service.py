from core.llm_service import LLMService


class JDService:

    def __init__(self):
        self.llm_service = LLMService()

    def extract_jd(self, description: str):
        return self.llm_service.extract_job_requirements(
            description
        )