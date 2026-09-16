from fastapi import APIRouter, Depends

from backend.database import get_db

route = APIRouter()

@route.post("/jobs")

def create_jobs(db = Depends(get_db)):