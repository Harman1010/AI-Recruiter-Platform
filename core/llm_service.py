from google import genai

from utils.config import settings

class JobRequirements():

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





class ResumeRequirements():

    """"""