from core.document_processor import DocumentProcessor

from core.llm_service import LLMService

def main():

    file_path = "data/Resumes (43).pdf"

    processor = DocumentProcessor()

    text = processor.extract_text(file_path)

    llmService = LLMService()

    response = llmService.extract_resume_details(text)

    print(response)

if __name__ == "__main__":

    main()