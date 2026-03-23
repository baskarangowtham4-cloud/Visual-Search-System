import os
import json
import numpy as np
import torch
import clip
from PIL import Image

model, preprocess = clip.load("ViT-B/32")

image_folder = "images"
embeddings = []
paths = []

for file in os.listdir(image_folder):
    if not file.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    path = os.path.join(image_folder, file)

    try:
        image = preprocess(Image.open(path).convert("RGB")).unsqueeze(0)

        with torch.no_grad():
            emb = model.encode_image(image)
            emb = emb / emb.norm()

        embeddings.append(emb.numpy()[0])
        paths.append(path)

    except Exception as e:
        print(f"Skipping {file}: {e}")

np.save("embeddings.npy", np.array(embeddings))

with open("image_paths.json", "w") as f:
    json.dump(paths, f)

print("✅ Embeddings generated successfully")