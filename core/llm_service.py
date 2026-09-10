from google import genai

from utils.config import settings

from utils.prompts import JD_PROMPT,RESUME_PROMPT

from schemas.job import JobSchema

from schemas.candidate import CandidateSchema

class LLMService():

    """A blueprint for extracting job requirements from job description"""

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(self,prompt:str)->str:

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    def extract_job_requirements(self,jd_text:str) -> JobSchema:

        prompt = JD_PROMPT.format(jd_text=jd_text)

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt,
            config = {
                "response_mime_type" : "application/json",
                "response_schema" : JobSchema
            }
        )

        return JobSchema.model_validate_json(response.text)

    def extract_resume_details(self,resume_text:str) -> CandidateSchema:

        prompt = RESUME_PROMPT.replace("{resume_text}",resume_text)

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt,
            config = {
                "response_mime_type" : "application/json",
                "response_schema" : CandidateSchema
            }
        )

        return CandidateSchema.model_validate_json(response.text)