from core.document_processor import DocumentProcessor

def main():

    file_path = "data/Resumes (43).pdf"

    processor = DocumentProcessor()

    text = processor.extract_text(file_path)

    print(text[:500])

    print("Characters:", len(text))

if __name__ == "__main__":

    main()