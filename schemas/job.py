from pydantic import BaseModel

class JobSchema(BaseModel):

    """A schema for Job requirements"""

    required_skills : list[str]

    preferred_skills : list[str]

    responsibilities : list[str]

    minimum_experience : float | None = None


