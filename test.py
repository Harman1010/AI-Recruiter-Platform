from core.document_processor import DocumentProcessor

from core.llm_service import JobRequirements

def main():

    query = "What is Machine Learning?"

    service = JobRequirements()

    response = service.generate(query)

    print(response)

if __name__ == "__main__":

    main()