"""
MindfulWellness API Routes - 100% FREE with Groq
FIXED: Better error handling + flexible inputs
"""

import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from groq import Groq
import logging

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    logger.warning("⚠️ GROQ_API_KEY not found in environment!")

client = Groq(api_key=GROQ_API_KEY)

# ==================== PYDANTIC MODELS ====================

class MoodCheckIn(BaseModel):
    mood: int
    thought: str

class ThoughtReframe(BaseModel):
    thought: str

class FinancialAnalysis(BaseModel):
    subscriptions: str

# ==================== MOOD TRACKING ====================

@router.post("/api/mood-checkin")
async def mood_checkin(request: MoodCheckIn):
    """Track mood and get AI coaching"""
    try:
        # Validate input
        if not request.thought or not request.thought.strip():
            raise HTTPException(status_code=400, detail="Thought is required")
        
        if request.mood < 1 or request.mood > 10:
            raise HTTPException(status_code=400, detail="Mood must be 1-10")
        
        logger.info(f"Processing mood checkin: {request.mood}/10")
        
        # Call Groq API
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=256,
            messages=[{
                "role": "user",
                "content": f"""You are a compassionate mental health coach. 

User's mood: {request.mood}/10
User's thought: "{request.thought}"

Provide a brief, supportive response using CBT techniques. Be warm and encouraging. Keep it under 150 words.

Include:
1. Acknowledgment of their feeling
2. One CBT insight
3. One small action they can take"""
            }]
        )
        
        coaching_response = chat_completion.choices[0].message.content
        
        return {
            "status": "success",
            "mood_score": request.mood,
            "user_thought": request.thought,
            "coaching_tip": coaching_response,
            "message": "Mood tracked successfully! ✅"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Mood checkin error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"API Error: {str(e)}")

# ==================== THOUGHT REFRAMING ====================

@router.post("/api/thought-reframe")
async def thought_reframe(request: ThoughtReframe):
    """Reframe negative thoughts using CBT"""
    try:
        if not request.thought or not request.thought.strip():
            raise HTTPException(status_code=400, detail="Thought is required")
        
        logger.info(f"Processing thought reframe: {request.thought}")
        
        # Call Groq API
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"""You are a cognitive behavioral therapist.

Client's negative thought: "{request.thought}"

Please provide EXACTLY 3 realistic alternative thoughts that:
1. Challenge the negative thought
2. Are believable and grounded in reality  
3. Are more balanced and helpful

Format your response EXACTLY like this:
Alternative 1: [realistic positive thought]
Alternative 2: [realistic positive thought]
Alternative 3: [realistic positive thought]"""
            }]
        )
        
        response_text = chat_completion.choices[0].message.content
        
        # Parse alternatives
        alternatives = []
        for line in response_text.split('\n'):
            line = line.strip()
            if 'Alternative' in line and ':' in line:
                alt = line.split(':', 1)[-1].strip()
                if alt:
                    alternatives.append(alt)
        
        # Ensure we have 3
        if len(alternatives) < 3:
            alternatives = [line.strip() for line in response_text.split('\n') if line.strip()][:3]
        
        return {
            "status": "success",
            "original_thought": request.thought,
            "reframes": alternatives[:3] if alternatives else ["Alternative perspective 1", "Alternative perspective 2", "Alternative perspective 3"],
            "message": "Thought reframed successfully! ✅"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Thought reframe error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"API Error: {str(e)}")

# ==================== FINANCIAL ANALYSIS ====================

@router.post("/api/financial-leaks")
async def financial_leaks(request: FinancialAnalysis):
    """Analyze subscriptions and find spending leaks"""
    try:
        if not request.subscriptions or not request.subscriptions.strip():
            raise HTTPException(status_code=400, detail="Subscriptions required")
        
        logger.info(f"Processing financial analysis")
        
        # Call Groq API
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"""You are a financial wellness advisor.

Client's subscriptions: {request.subscriptions}

Please:
1. Calculate TOTAL monthly spending (just the number)
2. Identify subscriptions that might be unused/expensive
3. Suggest 2-3 ways to reduce spending

Format:
TOTAL: $X
LEAKS: [list the subscription name and amount]
RECOMMENDATIONS: [list 2-3 actionable ways to save]"""
            }]
        )
        
        analysis = chat_completion.choices[0].message.content
        
        return {
            "status": "success",
            "subscriptions": request.subscriptions,
            "analysis": analysis,
            "message": "Financial analysis complete! ✅"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Financial analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"API Error: {str(e)}")

# ==================== HEALTH & ROOT ====================

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "api": "online"}

@router.get("/")
async def root():
    """Root endpoint with API info"""
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

