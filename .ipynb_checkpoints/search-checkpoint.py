import faiss
import numpy as np
import json
import torch
import clip

model, _ = clip.load("ViT-B/32")

embeddings = np.load("embeddings.npy")
index = faiss.IndexFlatL2(512)
index.add(embeddings)

with open("image_paths.json") as f:
    paths = json.load(f)

def search_images(query, top_k=5):
    text = clip.tokenize([query])

    with torch.no_grad():
        text_emb = model.encode_text(text)
        text_emb = text_emb / text_emb.norm()

    D, I = index.search(text_emb.numpy(), top_k)

    results = []
    for dist, idx in zip(D[0], I[0]):
        similarity = float(1 / (1 + dist))  # convert distance → score

        results.append({
            "image_path": paths[idx],
            "score": round(similarity, 4)
        })

    return results