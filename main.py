"""
MindfulWellness MVP - Main Entry Point
100% FREE VERSION using Groq
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

load_dotenv()

app = FastAPI(
    title="MindfulWellness API (FREE)",
    description="AI Mental Health + Financial Stress Relief - 100% Free",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "MindfulWellness API Running (100% FREE)",
        "status": "healthy",
        "version": "0.1.0",
        "powered_by": "Groq (Free API)",
        "cost": "$0",
        "endpoints": [
            "POST /api/mood-checkin",
            "POST /api/thought-reframe",
            "POST /api/financial-leaks"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

