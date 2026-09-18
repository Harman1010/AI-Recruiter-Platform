from pydantic import BaseModel

class Match(BaseModel):

    job_id: int

    candidate_id : int

    total_score : float

    required_skill_score : float

    preferred_skill_score : float

    project_score : float

    experience_score : float

    certification_score : float

