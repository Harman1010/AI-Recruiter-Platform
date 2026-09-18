from fastapi import APIRouter, Depends

from backend.schemas.job_schema import JobCreate

from backend.database import get_db

from backend.models.job_model import Job

job_route = APIRouter()

@job_route.post("/jobs")

def create_jobs(job : JobCreate,db = Depends(get_db)):

    new_job = Job(title=job.title,description=job.description)

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job