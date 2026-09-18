from backend.database import Base, engine

from backend.models.job_model import Job
from backend.models.candidate import Candidate
from backend.models.matches import Match


Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")