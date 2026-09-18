from fastapi import APIRouter, Depends, Form, UploadFile, File, HTTPException

from backend.database import get_db

from backend.models.job_model import Job

from backend.services.document_service import DocumentService

from pathlib import Path

from uuid import uuid4

job_route = APIRouter()

UPLOAD_DIR = Path("uploads/jds")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx"}

document_service = DocumentService()


@job_route.post("/jobs")
async def create_job(
    title: str = Form(...),
    description: str | None = Form(None),
    jd_file: UploadFile | None = File(None),
    db = Depends(get_db)
):

    if not description and not jd_file:
        raise HTTPException(
            status_code=400,
            detail="Provide either JD description or upload a JD file."
        )

    if description and jd_file:
        raise HTTPException(
            status_code=400,
            detail="Provide either JD description or upload a JD file, not both."
        )

    jd_file_path = None

    if jd_file:

        file_extension = Path(jd_file.filename).suffix.lower()

        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX JD files are supported."
            )

        unique_filename = f"{uuid4()}{file_extension}"

        file_path = UPLOAD_DIR / unique_filename

        file_content = await jd_file.read()

        with open(file_path, "wb") as file:
            file.write(file_content)

        description = document_service.extract_text(
            str(file_path)
        )

        jd_file_path = str(file_path)

    new_job = Job(
        title=title,
        description=description,
        jd_file_path=jd_file_path
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job