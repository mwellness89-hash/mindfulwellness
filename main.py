"""
MindfulWellness MVP - Main Entry Point
100% FREE VERSION using Groq
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI
app = FastAPI(
    title="MindfulWellness API (FREE)",
    description="AI Mental Health + Financial Stress Relief - 100% Free",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== DATA MODELS ====================

class MoodCheckIn(BaseModel):
    mood: int  # 1-10
    thought: str

class ThoughtReframe(BaseModel):
    thought: str

class FinancialAnalysis(BaseModel):
    subscriptions: str

# ==================== HELPER FUNCTIONS ====================

def get_groq_response(prompt: str) -> str:
    """Get response from Groq API"""
    try:
        from groq import Groq
        
        client = Groq(api_key=GROQ_API_KEY)
        
        message = client.messages.create(
            model="mixtral-8x7b-32768",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        logger.error(f"Groq API Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

# ==================== ROUTES ====================

@app.get("/")
async def root():
    """Root endpoint"""
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
    """Health check endpoint"""
    return {"status": "ok", "api": "online"}

# ==================== MOOD TRACKING ====================

@app.post("/api/mood-checkin")
async def mood_checkin(data: MoodCheckIn):
    """
    Track mood and get AI coaching
    
    Example:
    {
        "mood": 5,
        "thought": "I'm stressed about finances"
    }
    """
    try:
        if not data.thought:
            raise HTTPException(status_code=400, detail="Thought is required")
        
        if data.mood < 1 or data.mood > 10:
            raise HTTPException(status_code=400, detail="Mood must be 1-10")
        
        # Create prompt for Groq
        prompt = f"""You are a compassionate mental health coach. A user reported their mood as {data.mood}/10 and said: "{data.thought}"

Provide a brief, supportive, evidence-based response using CBT techniques. Be warm and encouraging. Keep it under 150 words."""
        
        # Get AI response
        coaching_response = get_groq_response(prompt)
        
        return {
            "status": "success",
            "mood_score": data.mood,
            "user_thought": data.thought,
            "coaching_tip": coaching_response,
            "message": "Mood tracked successfully"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Mood check-in error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# ==================== THOUGHT REFRAMING ====================

@app.post("/api/thought-reframe")
async def thought_reframe(data: ThoughtReframe):
    """
    Reframe negative thoughts using CBT
    
    Example:
    {
        "thought": "I'll never escape my debt"
    }
    """
    try:
        if not data.thought:
            raise HTTPException(status_code=400, detail="Thought is required")
        
        # Create prompt for Groq
        prompt = f"""You are a cognitive behavioral therapist. A client shared this negative automatic thought: "{data.thought}"

Please provide EXACTLY 3 realistic alternative thoughts that:
1. Challenge the negative thought
2. Are believable and grounded in reality
3. Are more balanced and helpful

Format your response as:
Alternative 1: [thought]
Alternative 2: [thought]
Alternative 3: [thought]"""
        
        # Get AI response
        reframe_response = get_groq_response(prompt)
        
        # Parse the response into alternatives
        alternatives = []
        for line in reframe_response.split('\n'):
            if line.strip().startswith('Alternative'):
                alt = line.split(':', 1)[-1].strip()
                if alt:
                    alternatives.append(alt)
        
        return {
            "status": "success",
            "original_thought": data.thought,
            "reframes": alternatives if alternatives else [reframe_response],
            "message": "Thought reframed successfully"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Thought reframe error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# ==================== FINANCIAL ANALYSIS ====================

@app.post("/api/financial-leaks")
async def financial_leaks(data: FinancialAnalysis):
    """
    Analyze subscriptions and find spending leaks
    
    Example:
    {
        "subscriptions": "Netflix $12, Gym $50, Spotify $10"
    }
    """
    try:
        if not data.subscriptions:
            raise HTTPException(status_code=400, detail="Subscriptions required")
        
        # Create prompt for Groq
        prompt = f"""You are a financial wellness advisor. A client listed their monthly subscriptions: "{data.subscriptions}"

1. Calculate total monthly spending
2. Identify any subscriptions that might be unused or unnecessary
3. Suggest 2-3 actionable ways to reduce spending
4. Be encouraging and non-judgmental

Format your response clearly with:
Total: $X
Potential leaks: [list]
Recommendations: [list]"""
        
        # Get AI response
        analysis_response = get_groq_response(prompt)
        
        # Try to extract total
        total_spending = "calculating..."
        if "Total:" in analysis_response:
            try:
                total_line = [l for l in analysis_response.split('\n') if 'Total:' in l][0]
                total_spending = total_line.split('$')[-1].split('\n')[0].strip()
            except:
                pass
        
        return {
            "status": "success",
            "subscriptions": data.subscriptions,
            "total_spending": total_spending,
            "analysis": analysis_response,
            "message": "Financial analysis complete"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Financial analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# ==================== ERROR HANDLERS ====================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

