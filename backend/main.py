from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Zenith AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sugoie4.github.io"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Accept"],
)

class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None

@app.get("/")
def home():
    return {
        "name": "Zenith AI",
        "status": "online",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    if not request.message.strip():
        return {"error": "Message cannot be empty"}

    return {
        "reply": "Zenith AI backend received your message. AI engine integration is our next task.",
        "conversation_id": request.conversation_id
    }
