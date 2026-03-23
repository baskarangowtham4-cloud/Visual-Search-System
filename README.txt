**Visual Search System (CLIP + FAISS + FastAPI)**
An enterprise-grade visual search system that enables users to search images using natural language queries with AI-powered explanations, 
structured API responses, and full observability (logging).

🚀 Features
🔍 Semantic Image Search using CLIP
⚡ Fast Retrieval with FAISS
🧠 AI-based Explanation Generation
🌐 FastAPI REST API (POST-based)
🖼️ Image Serving via API
📊 Structured JSON Responses
🧾 Full Request-Response Logging
🐳 Dockerized for Deployment

**Architecture Overview**
User Query → CLIP Text Embedding
                     ↓
Images → CLIP Image Embedding → FAISS Index
                     ↓
         Similarity Search (Top-K)
                     ↓
        API Response + Explanation + Logs

**Project Structure**
case_study/
│── main.py              # FastAPI app
│── search.py            # FAISS search logic
│── embed.py             # Generate embeddings
│── explanation.py       # Explanation generator
│── logger.py            # Logging setup
│── requirements.txt     # Dependencies
│── Dockerfile           # Container setup
│── embeddings.npy       # Saved embeddings
│── image_paths.json     # Image mapping
│── images/              # Image dataset

**Installation**
pip install -r requirements.txt
python embed.py
uvicorn main:app --reload

**API Endpoint**
http://127.0.0.1:8000/search

**Sample Input Payload**
{
  "query": "dog",
  "top_k": 5
}

**Sample Response**
{
    "request": {
        "id": "4d808f6e-f0ea-45eb-804c-7a74eb899aa3",
        "timestamp": "2026-03-23T19:24:28.277678",
        "query": "dog",
        "top_k": 5,
        "latency": 0.146
    },
    "results": [
        {
            "image": {
                "id": "6932.jpg",
                "url": "http://127.0.0.1:8000/image?path=images\\6932.jpg"
            },
            "relevance": {
                "score": 0.412,
                "rank": 1
            },
            "explanation": "The image '6932.jpg' is relevant to the query 'dog' with a similarity score of 0.412. It likely contains visual elements or scenes associated with 'dog'."
        },
        {
            "image": {
                "id": "6970.jpg",
                "url": "http://127.0.0.1:8000/image?path=images\\6970.jpg"
            },
            "relevance": {
                "score": 0.4104,
                "rank": 2
            },
            "explanation": "The image '6970.jpg' is relevant to the query 'dog' with a similarity score of 0.4104. It likely contains visual elements or scenes associated with 'dog'."
        },
        {
            "image": {
                "id": "0328.jpg",
                "url": "http://127.0.0.1:8000/image?path=images\\0328.jpg"
            },
            "relevance": {
                "score": 0.4104,
                "rank": 3
            },
            "explanation": "The image '0328.jpg' is relevant to the query 'dog' with a similarity score of 0.4104. It likely contains visual elements or scenes associated with 'dog'."
        },
        {
            "image": {
                "id": "0369.jpg",
                "url": "http://127.0.0.1:8000/image?path=images\\0369.jpg"
            },
            "relevance": {
                "score": 0.4096,
                "rank": 4
            },
            "explanation": "The image '0369.jpg' is relevant to the query 'dog' with a similarity score of 0.4096. It likely contains visual elements or scenes associated with 'dog'."
        },
        {
            "image": {
                "id": "0616.jpg",
                "url": "http://127.0.0.1:8000/image?path=images\\0616.jpg"
            },
            "relevance": {
                "score": 0.4093,
                "rank": 5
            },
            "explanation": "The image '0616.jpg' is relevant to the query 'dog' with a similarity score of 0.4093. It likely contains visual elements or scenes associated with 'dog'."
        }
    ]
}
