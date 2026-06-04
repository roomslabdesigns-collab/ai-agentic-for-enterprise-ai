import os
from fastapi import FastAPI

from app.models import ChatRequest
from app.rag.rag_pipeline import ask_question


from fastapi import UploadFile
from fastapi import File

app = FastAPI(
    title="Enterprise AI Copilot",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Enterprise AI Copilot Running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }
@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        content = await file.read()

        buffer.write(content)

    return {
        "message": "Upload successful",
        "filename": file.filename
    }    