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

    skill_score = scoring_service.skill_service.calculate_skill_score(jd.required_skills,candidate.skills,25)
    preferred_skill_score = scoring_service.skill_service.calculate_skill_score(jd.preferred_skills,candidate.skills,15)

    project_score = scoring_service.project_service.calculate_project_score(jd.responsibilities,candidate.projects)

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
    print(f"Preferred Skills Score : {preferred_skill_score:.2f} / 15")
    print(f"Project Score         : {project_score:.2f} / 40")
    print(f"Experience Score      : {experience_score:.2f} / 15")
    print(f"Certification Score   : {certification_score:.2f} / 5")

    total_score = (
        skill_score + preferred_skill_score
        + project_score
        + experience_score
        + certification_score
    )

    print("--------------------------------")
    print(f"Current Score         : {total_score:.2f}")

    print("\n========== PREFERRED SKILL SIMILARITY ==========")

    for jd_skill in jd.preferred_skills:

        best_score = 0.0
        best_resume_skill = None

        for resume_skill in candidate.skills:

            score = scoring_service.skill_service.calculate_similarity(
                jd_skill,
                resume_skill
            )

            if score > best_score:
                best_score = score
                best_resume_skill = resume_skill

        print(
            f"{jd_skill} "
            f"<-> {best_resume_skill} "
            f"= {best_score:.4f}"
        )


if __name__ == "__main__":
    main()