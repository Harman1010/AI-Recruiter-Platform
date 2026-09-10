import fitz

from docx import Document

class DocumentProcessor():

    """A blueprint for processing different document type

    PDF - PyMuPDF

    DOCX - Python-docx"""

    def extract_text(self, file_path: str) -> str:
        """Extracts text based on the document type."""

        if file_path.endswith(".pdf"):
            return self.extract_pdf(file_path)

        elif file_path.endswith(".docx"):
            return self.extract_docx(file_path)

        else:
            return "Unsupported file format. Only PDF and DOCX are supported."


    def extract_pdf(self,file_path:str) -> str:

        """Extract and processes PDF"""

        doc = fitz.open(file_path)

        text = ""

        for page in doc:

            text += page.get_text() + "\n"

        doc.close()

        if not text.strip():

            return "Content could not be found."

        elif len(text) < 100 or len(text) > 10000:

            return "Content length is either too less or too much for processing"

        return text

    def extract_docx(self,file_path:str) -> str:

        """Extracts and processes docx"""

        doc = Document(file_path)

        text = ""

        for paragraph in doc.paragraphs:

            text += paragraph.text + "\n"

        if not text.strip():

            return "Content could not be found"

        if len(text) < 100 or len(text) > 10000:

            return "Content is either too short or too long"

        return text

