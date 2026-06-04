import os

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.models import ChatRequest
from app.rag.rag_pipeline import ask_question

from app.database.db import get_db
from app.database.crud import save_chat

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
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    answer = ask_question(
        request.question
    )

    save_chat(
        db,
        request.question,
        answer
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
from app.database.crud import (
    save_chat,
    get_chat_history
)

@app.get("/history")
def history(
    db: Session = Depends(get_db)
):

    chats = get_chat_history(db)

    return chats