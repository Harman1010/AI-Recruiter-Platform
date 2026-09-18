from fastapi import APIRouter, Depends, File, Form , UploadFile, HTTPException

from backend.models.candidate import Candidate

from backend.database import get_db

from pathlib import Path

from uuid import uuid4

candidate_route = APIRouter()

UPLOAD_DIR = Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf",".docx"}

@candidate_route.post("/candidates")

async def create_candidate(name : str = Form(...), resume : UploadFile = File(...), db = Depends(get_db)):

    file_extension = Path(resume.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(status_code=400,detail="Only PDF and DOCX resumes are supported.")

    unique_filename = f"{uuid4()}{file_extension}"

    file_path = UPLOAD_DIR / unique_filename

    file_content = await resume.read()

    with open(file_path, "wb") as file:

        file.write(file_content)

    new_candidate = Candidate(name=name, resume_link=str(file_path))

    db.add(new_candidate)

    db.commit()

    db.refresh(new_candidate)

    return new_candidate

