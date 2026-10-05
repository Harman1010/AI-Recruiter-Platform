from sentence_transformers import SentenceTransformer

class EmbeddingsService():

    """A blueprint for initializing and creating embeddings"""

    def __init__(self):

        self.model = None

    def create_embedding(self,text):

        if self.model is None:
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            
        return self.model.encode(text,normalize_embeddings=True)