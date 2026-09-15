from core.document_processor import DocumentProcessor
from core.llm_service import LLMService
from core.candidate_ranking_service import RankingService


def main():

    document_processor = DocumentProcessor()
    llm_service = LLMService()
    ranking_service = RankingService()

    # -------------------------------
    # Extract Job Description
    # -------------------------------

    jd_text = document_processor.extract_text(
        "data/sample_jd_ai_engineer.pdf"
    )

    jd = llm_service.extract_job_requirements(jd_text)

    print("\n========== JOB DESCRIPTION ==========")
    print(jd)

    # -------------------------------
    # Extract Candidates
    # -------------------------------

    resume_paths = [
        "data/Resumes (43).pdf",
        "data/Harman_Nordon.pdf",
        "data/Harman_USP.pdf"
    ]

    candidates = []

    for resume_path in resume_paths:

        resume_text = document_processor.extract_text(
            resume_path
        )

        candidate = llm_service.extract_resume_details(
            resume_text
        )

        candidates.append(candidate)

    # -------------------------------
    # Rank Candidates
    # -------------------------------

    ranked_candidates = ranking_service.rank_candidates(
        jd,
        candidates
    )

    # -------------------------------
    # Display Ranking
    # -------------------------------

    print("\n========== CANDIDATE RANKING ==========")

    for rank, result in enumerate(ranked_candidates, start=1):

        print(
            f"Rank {rank} "
            f"→ Score: {result['score']:.2f}"
        )


if __name__ == "__main__":
    main()