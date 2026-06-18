# LangChain RAG FastAPI Docker

A Retrieval-Augmented Generation (RAG) application built using LangChain, FAISS, Ollama, FastAPI, and Docker. The system enables users to upload PDF documents, generate embeddings, perform semantic retrieval, and answer questions using a locally hosted LLM.

## Features

* PDF document ingestion
* Semantic search using FAISS vector database
* Question answering using Retrieval-Augmented Generation (RAG)
* Local LLM inference using Ollama (Llama 3.2)
* FastAPI REST endpoints
* Dynamic document upload and re-indexing
* Dockerized deployment

---

## Architecture

PDF Document
↓
Text Extraction
↓
Chunking
↓
Embeddings (Sentence Transformers)
↓
FAISS Vector Store
↓
Retriever
↓
Ollama (Llama 3.2)
↓
Generated Answer

## Tech Stack

* Python
* LangChain
* FAISS
* Ollama
* FastAPI
* Docker
* Sentence Transformers

---

## Project Structure

langchain-rag-fastapi-docker/

├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
│
├── services/
│   └── rag_service.py
│
├── data/
├── faiss_index/
└── images/

## API Endpoints

### Health Check

GET /

Response:

{
  "message": "Multimodal RAG API Running"
}

### Upload PDF

POST /upload

Uploads a PDF document and refreshes the vector store.

### Ask Question

POST /ask

Request:

{
  "question": "What is ECG?"
}

Response:

{
  "question": "What is ECG?",
  "answer": "..."
}

---

## Prerequisites

Before running the project, install:

* Python 3.11+
* Docker Desktop
* Ollama

Install Ollama:

https://ollama.com

Pull the model:

ollama pull llama3.2

Start Ollama:

ollama serve

---

## Running Locally

Clone the repository:

git clone https://github.com/Shipra1207/langchain-rag-fastapi-docker.git

Move into the project directory:

cd langchain-rag-fastapi-docker

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn app:app --reload

Open Swagger UI:

http://localhost:8000/docs

---

## Running with Docker

Build image:

docker build -t rag-api .

Run container:

docker run -p 8000:8000 rag-api

Open API documentation:

http://localhost:8000/docs

---

## Current Limitations

* Retrieval is primarily text-based
* Chart and graph interpretation is limited
* Images are not directly embedded into the vector store
* True multimodal retrieval is not implemented

---

## Future Enhancements

* Multimodal RAG
* Chart and graph understanding
* LangGraph-based agent workflow
* Cloud deployment using AWS
* Automated CI/CD pipeline

---

## Learning Outcomes

This project helped demonstrate:

* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* LangChain pipelines
* FastAPI development
* Docker containerization
* Git and GitHub workflows
* Local LLM deployment using Ollama