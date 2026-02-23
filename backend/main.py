from routes.idea_validator import router as idea_validator_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="AI Startup Validator API",
    description="Validate your startup ideas with AI",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok", "message": "AI Startup Validator API is running"}

@app.get("/health")
async def health():
    groq_key_set = bool(os.getenv("GROQ_API_KEY"))
    return {
        "status": "healthy",
        "groq_api_key_configured": groq_key_set
    }

app.include_router(idea_validator_router)