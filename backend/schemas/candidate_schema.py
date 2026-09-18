from pydantic import BaseModel

class CandidateCreate(BaseModel):

    name : str

    resume_link : str