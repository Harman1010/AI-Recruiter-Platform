from fastapi import APIRouter, Depends

from backend.schemas.match_schema import Match

from backend.database import get_db

from backend.models import matches

match_route = APIRouter()

@match_route.post("/matches")

def create_match(match : Match, db = Depends(get_db)):

    new_match = Match(
        job_id=match.job_id,
        candidate_id=match.candidate_id,
        total_score=match.total_score,
        required_skill_score=match.required_skill_score,
        preferred_skill_score=match.preferred_skill_score,
        project_score=match.project_score,
        experience_score=match.experience_score,
        certification_score=match.certification_score
    )

    db.add(new_match)

    db.commit()

    db.refresh(new_match)

    return new_match

