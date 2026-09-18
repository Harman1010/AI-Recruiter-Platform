from core.llm_service import LLMService


class CandidateService:

    def __init__(self):
        self.llm_service = LLMService()

    def extract_candidate(self, resume_text: str):
        return self.llm_service.extract_resume_details(
            resume_text
        )