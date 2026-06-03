from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Copilot",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Enterprise AI Copilot Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }