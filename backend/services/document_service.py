from core.document_processor import DocumentProcessor


class DocumentService:

    def __init__(self):
        self.document_processor = DocumentProcessor()

    def extract_text(self, file_path: str):
        return self.document_processor.extract_text(file_path)