from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.job_model import Job
from backend.models.candidate import Candidate
from backend.models.matches import Match

from backend.services.jd_service import JDService
from backend.services.candidate_service import CandidateService
from backend.services.document_service import DocumentService

from core.candidate_scoring_service import CandidateScoringService

route = APIRouter()

jd_service = JDService()
candidate_service = CandidateService()
document_service = DocumentService()
scoring_service = CandidateScoringService()


@route.post("/matches/{job_id}/{candidate_id}")
def create_match(
    job_id: int,
    candidate_id: int,
    db: Session = Depends(get_db)
):
    job = db.get(Job, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    candidate = db.get(Candidate, candidate_id)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    jd = jd_service.extract_jd(job.description)

    resume_text = document_service.extract_text(
        candidate.resume_link
    )

    candidate_data = candidate_service.extract_candidate(
        resume_text
    )

    score = scoring_service.calculate_score(
        jd,
        candidate_data
    )

    match = Match(
        job_id=job_id,
        candidate_id=candidate_id,
        total_score=score["total_score"],
        required_skill_score=score["required_skill_score"],
        preferred_skill_score=score["preferred_skill_score"],
        project_score=score["project_score"],
        experience_score=score["experience_score"],
        certification_score=score["certification_score"]
    )

    db.add(match)
    db.commit()
    db.refresh(match)

    return match

@route.get("/matches/{match_id}")
def get_match_details(
    match_id: int,
    db: Session = Depends(get_db)
):
    match = db.get(Match, match_id)

    if not match:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    return {
        "match_id": match.id,
        "job_id": match.job_id,
        "candidate_id": match.candidate_id,
        "total_score": match.total_score,
        "required_skill_score": match.required_skill_score,
        "preferred_skill_score": match.preferred_skill_score,
        "project_score": match.project_score,
        "experience_score": match.experience_score,
        "certification_score": match.certification_score
    }