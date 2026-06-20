from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import UploadFile, File
import shutil
import os
from services.rag_service import RAGService
rag_service = RAGService()
app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API Running"}

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    upload_path = f"data/{file.filename}"
    os.makedirs("data",exist_ok=True)
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunks = rag_service.ingest_pdf(upload_path)

    return {
        "message": "PDF uploaded successfully",
        "chunks_created": chunks
    }

@app.post("/ask")
def ask_question(request: QueryRequest):

    answer = rag_service.ask(
    request.question
)

    return {
        "question": request.question,
        "answer": answer
    }