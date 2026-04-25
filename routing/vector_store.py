import faiss
import numpy as np
from routing.embedder import get_embedding

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.vectors = []
        self.labels = []

    def add(self, text, label):
        emb = get_embedding(text)
        self.index.add(np.array([emb]))
        self.vectors.append(emb)
        self.labels.append(label)

    def search(self, text, k=3):
        emb = get_embedding(text)
        D, I = self.index.search(np.array([emb]), k)
        return [(self.labels[i], float(D[0][idx])) for idx, i in enumerate(I[0])]