from pydantic import BaseModel

class Experience(BaseModel):

    company : str

    role : str

    years : float | None = None

class Project(BaseModel):

    name : str

    description : str

class Education(BaseModel):

    degree : str

    field : str

class Certification(BaseModel):

    name : str

    issuer : str | None = None

class CandidateSchema(BaseModel):

    """A schema of the candidate's information extracted from its resume"""

    skills : list[str]

    experience : list[Experience]

    projects : list[Project]

    certifications : list[Certification]

    education : list[Education]


