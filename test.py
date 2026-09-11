from core.document_processor import DocumentProcessor

from core.llm_service import LLMService

from core.embeddings_service import EmbeddingsService


from core.document_processor import DocumentProcessor
from core.llm_service import LLMService
from core.candidate_scoring_service import CandidateScoringService


def main():

    processor = DocumentProcessor()
    llm_service = LLMService()
    scoring_service = CandidateScoringService()

    # Extract JD
    jd_text = processor.extract_text("data/sample_jd_ai_engineer.pdf")
    jd = llm_service.extract_job_requirements(jd_text)

    # Extract Resume
    resume_text = processor.extract_text("data/Resumes (43).pdf")
    candidate = llm_service.extract_resume_details(resume_text)

    # Calculate final score
    score = scoring_service.calculate_score(
        jd,
        candidate
    )

    print("Final Candidate Score:", score)


if __name__ == "__main__":
    main()