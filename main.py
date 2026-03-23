from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from search import search_images
from explanation import generate_explanation
from logger import logger

import uuid
from datetime import datetime
import time
import json
import os

app = FastAPI(title="Visual Search System")


# 🔹 Request schema
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


# 🔹 Serve images
@app.get("/image")
def get_image(path: str):
    return FileResponse(path)


# 🔹 Search API (POST)
@app.post("/search")
def search(request: SearchRequest):

    query = request.query
    top_k = request.top_k

    request_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        results = search_images(query, top_k)

        structured_results = []

        for rank, item in enumerate(results, start=1):
            image_path = item["image_path"]
            image_id = os.path.basename(image_path)

            image_url = f"http://127.0.0.1:8000/image?path={image_path}"

            explanation = generate_explanation(
                query, image_id, item["score"]
            )

            structured_results.append({
                "image": {
                    "id": image_id,
                    "url": image_url
                },
                "relevance": {
                    "score": item["score"],
                    "rank": rank
                },
                "explanation": explanation
            })

        latency = round(time.time() - start_time, 3)

        response_payload = {
            "request": {
                "id": request_id,
                "timestamp": timestamp,
                "query": query,
                "top_k": top_k,
                "latency": latency
            },
            "results": structured_results
        }

        # 🔥 Full structured logging
        logger.info(json.dumps(response_payload))

        return response_payload

    except Exception as e:
        error_payload = {
            "request": {"id": request_id},
            "error": str(e)
        }

        logger.error(json.dumps(error_payload))
        return error_payload