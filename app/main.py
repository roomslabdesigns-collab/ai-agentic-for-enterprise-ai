from fastapi import FastAPI

from app.models import ChatRequest
from app.rag.rag_pipeline import ask_question

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