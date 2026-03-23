# Visual Search System (CLIP + FAISS + FastAPI)

An enterprise-grade visual search system that enables users to search images using natural language queries with AI-powered explanations, structured API responses, and full observability (logging).

---

## Features

- Semantic Image Search using CLIP  
- Fast Retrieval with FAISS  
- AI-based Explanation Generation  
- FastAPI REST API (POST-based)  
- Image Serving via API  
- Structured JSON Responses  
- Full Request-Response Logging  
- Dockerized for Deployment  

---

## Architecture Overview
User Query → CLIP Text Embedding
↓
Images → CLIP Image Embedding → FAISS Index
↓
Similarity Search (Top-K)
↓
API Response + Explanation + Logs

## Project Structure

case_study/
│── main.py # FastAPI app
│── search.py # FAISS search logic
│── embed.py # Generate embeddings
│── explanation.py # Explanation generator
│── logger.py # Logging setup
│── requirements.txt # Dependencies
│── Dockerfile # Container setup
│── embeddings.npy # Saved embeddings
│── image_paths.json # Image mapping
│── images/ # Image dataset

## Installation
pip install -r requirements.txt
python embed.py
uvicorn main:app --reload

docker build -t my-fastapi-app .
docker run -d -p 8000:8000 my-fastapi-app

## API Endpoint
http://127.0.0.1:8000/search

## Sample Input Payload
{
  "query": "dog",
  "top_k": 5
}
