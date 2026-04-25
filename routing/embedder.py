from sentence_transformers import SentenceTransformer
from config.settings import Settings

model = SentenceTransformer(Settings.EMBEDDING_MODEL)

def get_embedding(text: str):
    return model.encode(text)