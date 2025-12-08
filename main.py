"""
MindfulWellness API - Minimal Working Version
Uses Groq chat completions for 3 endpoints.
"""

import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from groq import Groq

# ========= Setup =========

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    logger.warning("⚠️ GROQ_API_KEY is NOT set")
client = Groq(api_key=GROQ_API_KEY)

app = FastAPI(
    title="MindfulWellness API (FREE)",
    description="AI Mental Health + Financial Stress Relief - 100% Free",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========= Models =========

class MoodCheckIn(BaseModel):
    mood: int
    thought: str

class ThoughtReframe(BaseModel):
    thought: str

class FinancialAnalysis(BaseModel):
    subscriptions: str

# ========= Helper =========

def groq_chat(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Groq API Error: {e}")
        raise HTTPException(status_code=500, detail=f"AI Error: {e}")

# ========= Routes =========

@app.get("/")
async def root():
    return {
        "message": "MindfulWellness API Running (100% FREE)",
        "status": "healthy",
        "version": "0.1.0",
        "endpoints": [
            "POST /api/mood-checkin",
            "POST /api/thought-reframe",
            "POST /api/financial-leaks",
        ],
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/mood-checkin")
async def mood_checkin(body: MoodCheckIn):
    if body.mood < 1 or body.mood > 10:
        raise HTTPException(status_code=400, detail="Mood must be between 1 and 10")

    prompt = f"""
You are a compassionate CBT coach.

User mood: {body.mood}/10
User thought: "{body.thought}"

1) Acknowledge their feeling.
2) Give one CBT insight.
3) Suggest one 2-minute action.

Keep it under 150 words.
"""
    coaching = groq_chat(prompt)
    return {
        "status": "success",
        "mood_score": body.mood,
        "user_thought": body.thought,
        "coaching_tip": coaching,
    }

@app.post("/api/thought-reframe")
async def thought_reframe(body: ThoughtReframe):
    prompt = f"""
You are a CBT therapist.

Negative thought: "{body.thought}"

Give EXACTLY 3 alternative thoughts, more balanced and realistic.
Format:

Alternative 1: ...
Alternative 2: ...
Alternative 3: ...
"""
    text = groq_chat(prompt)

    alternatives = []
    for line in text.split("\n"):
        line = line.strip()
        if "Alternative" in line and ":" in line:
            alt = line.split(":", 1)[1].strip()
            if alt:
                alternatives.append(alt)

    if len(alternatives) < 3:
        alternatives = [l.strip() for l in text.split("\n") if l.strip()][:3]

    return {
        "status": "success",
        "original_thought": body.thought,
        "reframes": alternatives[:3],
    }

@app.post("/api/financial-leaks")
async def financial_leaks(body: FinancialAnalysis):
    prompt = f"""
You are a friendly financial coach.

User subscriptions (name + price): {body.subscriptions}

1) Estimate TOTAL monthly cost.
2) List any possible money leaks.
3) Suggest 2–3 ways to save.

Format:

TOTAL: $X
LEAKS:
- item 1
- item 2

RECOMMENDATIONS:
- step 1
- step 2
"""
    analysis = groq_chat(prompt)
    return {
        "status": "success",
        "subscriptions": body.subscriptions,
        "analysis": analysis,
    }

# ========= Error handler =========

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code},
    )

# ========= Local run =========

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

      
