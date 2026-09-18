from fastapi import APIRouter, Depends

from backend.schemas.candidate_schema import CandidateCreate

from backend.models.candidate import Candidate

from backend.database import get_db

candidate_route = APIRouter()

@candidate_route.post("/candidates")

def create_candidate(candidate : CandidateCreate, db = Depends(get_db)):

    new_candidate = Candidate(name = candidate.name,resume_link=candidate.resume_link)

    db.add(new_candidate)

    db.commit()

    db.refresh(new_candidate)

    return new_candidate

