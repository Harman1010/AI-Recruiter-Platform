from core.document_processor import DocumentProcessor

from core.llm_service import LLMService

from core.embeddings_service import EmbeddingsService


def main():

    service = EmbeddingsService()

    text = "Built a RAG application using Python and LangChain."

    embedding = service.create_embedding(text)

    print("Embedding type:", type(embedding))
    print("Embedding shape:", embedding.shape)
    print("First 5 values:", embedding[:5])


if __name__ == "__main__":
    main()