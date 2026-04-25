import numpy as np
from routing.embedder import get_embedding

PERSONAS = {
    "Bot_A": "AI, crypto, Elon Musk, optimism",
    "Bot_B": "anti-tech, privacy, capitalism critique",
    "Bot_C": "markets, trading, ROI, finance"
}

persona_embeddings = {k: get_embedding(v) for k, v in PERSONAS.items()}

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def route_post_to_bots(post_content: str, threshold: float = 0.75):
    post_emb = get_embedding(post_content)

    scores = []
    for bot, emb in persona_embeddings.items():
        sim = cosine_sim(post_emb, emb)
        scores.append((bot, sim))

    scores.sort(key=lambda x: x[1], reverse=True)

    # ✅ LOG SCORES
    print("\n[Routing Scores]")
    for bot, sim in scores:
        print(f"{bot}: {sim:.4f}")

    selected = [bot for bot, sim in scores if sim >= threshold]

    if not selected:
        return [scores[0][0]]

    return selected