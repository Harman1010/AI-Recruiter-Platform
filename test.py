from core.document_processor import DocumentProcessor
from core.llm_service import LLMService
from core.candidate_scoring_service import CandidateScoringService


def main():

    document_processor = DocumentProcessor()
    llm_service = LLMService()
    scoring_service = CandidateScoringService()

    # -------------------------
    # Extract JD
    # -------------------------

    jd_text = document_processor.extract_text("data/sample_jd_ai_engineer.pdf")
    jd = llm_service.extract_job_requirements(jd_text)

    print("\n========== JOB DESCRIPTION ==========")
    print(jd)

    # -------------------------
    # Extract Candidate Resume
    # -------------------------

    resume_text = document_processor.extract_text("data/Resumes (43).pdf")
    candidate = llm_service.extract_resume_details(resume_text)

    print("\n========== CANDIDATE ==========")
    print(candidate)

    # -------------------------
    # Calculate individual scores
    # -------------------------

    skill_score = scoring_service.skill_service.calculate_skill_score(
        jd.required_skills,
        candidate.skills
    )

    project_score = scoring_service.project_service.calculate_project_score(
        jd.responsibilities,
        jd.required_skills,
        jd.preferred_skills,
        candidate.projects
    )

    experience_score = scoring_service.experience_service.calculate_experience_score(
        jd.minimum_experience_years,
        candidate.experience
    )

    certification_score = scoring_service.certification_service.calculate_certification_score(
        jd.certifications,
        candidate.certifications
    )

    # -------------------------
    # Print scores
    # -------------------------

    print("\n========== SCORING ==========")

    print(f"Required Skills Score : {skill_score:.2f} / 25")
    print(f"Project Score         : {project_score:.2f} / 40")
    print(f"Experience Score      : {experience_score:.2f} / 15")
    print(f"Certification Score   : {certification_score:.2f} / 5")

    total_score = (
        skill_score
        + project_score
        + experience_score
        + certification_score
    )

    print("--------------------------------")
    print(f"Current Score         : {total_score:.2f}")


if __name__ == "__main__":
    main()