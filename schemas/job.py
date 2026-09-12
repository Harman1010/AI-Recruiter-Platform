from pydantic import BaseModel

class JobSchema(BaseModel):

    """A schema for Job requirements"""

    required_skills : list[str]

    preferred_skills : list[str]

    responsibilities : list[str]

    #education: list[str]

    certifications: list[str]

    minimum_experience_years : float | None = None


