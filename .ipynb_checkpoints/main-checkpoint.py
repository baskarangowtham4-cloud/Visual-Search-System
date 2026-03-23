from fastapi import FastAPI, Query
from search import search_images
from explanation import generate_explanation

app = FastAPI(title="Visual Search System")

@app.get("/")
def home():
    return {"message": "Visual Search API is running"}

@app.get("/search")
def search(query: str, top_k: int = Query(5, ge=1, le=50)):
    results = search_images(query, top_k)

    final_results = []
    for item in results:
        explanation = generate_explanation(
            query, item["image_path"], item["score"]
        )

        final_results.append({
            "image_path": item["image_path"],
            "score": item["score"],
            "explanation": explanation
        })

    return {
        "query": query,
        "top_k": top_k,
        "results": final_results
    }