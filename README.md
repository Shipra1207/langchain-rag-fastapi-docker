# LangChain RAG FastAPI Docker

A Retrieval-Augmented Generation (RAG) application built using LangChain, FAISS, Ollama, FastAPI, and Docker. The system enables users to upload PDF documents, generate vector embeddings, perform semantic retrieval, and answer questions using a locally hosted LLM.

## Key Features

* PDF document ingestion and processing
* Semantic search using FAISS vector store
* Local LLM inference using Ollama (Llama 3.2)
* REST APIs built with FastAPI
* Dynamic document upload and re-indexing
* Dockerized deployment
* Fully local execution with no external LLM API dependency

## Architecture

PDF Document
→ Text Extraction
→ Chunking
→ Embedding Generation
→ FAISS Vector Store
→ Semantic Retrieval
→ Ollama (Llama 3.2)
→ Response Generation

## Current Limitations

* Retrieval is primarily text-based
* Charts and graphs are not interpreted
* Images are not directly embedded into the vector store
* True multimodal retrieval is planned as a future enhancement
