from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.job_model import Job
from backend.models.candidate import Candidate
from backend.models.matches import Match


ranking_route = APIRouter()


@ranking_route.get("/jobs/{job_id}/candidates")
def get_ranked_candidates(
    job_id: int,
    db: Session = Depends(get_db)
):
    job = db.get(Job, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    statement = (
        select(Match, Candidate)
        .join(
            Candidate,
            Match.candidate_id == Candidate.id
        )
        .where(Match.job_id == job_id)
        .order_by(Match.total_score.desc())
    )

    results = db.execute(statement).all()

    return [
        {
            "rank": rank,
            "candidate_id": candidate.id,
            "candidate_name": candidate.name,
            "resume_link": candidate.resume_link,
            "score": match.total_score
        }
        for rank, (match, candidate) in enumerate(results, start=1)
    ]