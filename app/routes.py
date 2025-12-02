"""
MindfulWellness API Routes - 100% FREE with Groq (CORRECT API)
"""

import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from groq import Groq
from app.schemas import (
    MoodCheckInRequest,
    MoodCheckInResponse,
    ThoughtReframeRequest,
    ThoughtReframeResponse,
    FinancialLeakRequest,
    FinancialLeakResponse,
    UserProfileRequest,
    FindMatchResponse,
    SendMessageRequest,
    SendMessageResponse
)

load_dotenv()

router = APIRouter()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@router.post("/api/mood-checkin", response_model=MoodCheckInResponse)
async def mood_checkin(request: MoodCheckInRequest):
    try:
        if not 1 <= request.mood_score <= 10:
            raise HTTPException(status_code=400, detail="Mood score must be 1-10")
        
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=256,
            messages=[{
                "role": "user",
                "content": f"""
                User mood: {request.mood_score}/10
                Stress: {request.stress_reason}
                
                Respond with:
                1. Acknowledge their stress (2 sentences)
                2. CBT insight (1 sentence)
                3. Micro-action (1 step, 2 min max)
                Plain text only.
                """
            }]
        )
        
        ai_response = chat_completion.choices[0].message.content
        
        return MoodCheckInResponse(
            user_id=request.user_id,
            mood_score=request.mood_score,
            ai_response=ai_response,
            next_step="Join accountability group",
            mood_logged=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.post("/api/thought-reframe", response_model=ThoughtReframeResponse)
async def reframe_thought(request: ThoughtReframeRequest):
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=200,
            messages=[{
                "role": "user",
                "content": f'Negative thought: "{request.negative_thought}"\n\nGenerate EXACTLY 3 CBT alternatives:\n1. Challenge it\n2. Evidence against\n3. Compassionate reframe\nFormat: 1. [thought]\n2. [thought]\n3. [thought]'
            }]
        )
        
        response_text = chat_completion.choices[0].message.content
        alternatives = [line.strip() for line in response_text.split('\n') if line.strip()]
        
        return ThoughtReframeResponse(
            user_id=request.user_id,
            original=request.negative_thought,
            alternatives=alternatives[:3],
            cbt_technique="Cognitive restructuring"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.post("/api/financial-leaks", response_model=FinancialLeakResponse)
async def find_leaks(request: FinancialLeakRequest):
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"Analyze transactions for leaks:\n\n{request.csv_data}\n\nFind: 1. Subscriptions 2. Duplicates 3. Overpriced\nFor each: Category, Amount, Cancel template"
            }]
        )
        
        leaks_found = chat_completion.choices[0].message.content
        
        return FinancialLeakResponse(
            user_id=request.user_id,
            leaks_found=leaks_found,
            mental_frame="Financial peace reduces anxiety",
            total_savings=None
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/")
async def root():
    return {
        "message": "MindfulWellness API (FREE)",
        "endpoints": ["/api/mood-checkin", "/api/thought-reframe", "/api/financial-leaks"]
    }


@router.post("/api/find-match", response_model=FindMatchResponse)
async def find_match(request: UserProfileRequest):
    """
    Find accountability partner with matching stress profile
    POWERED BY: Rule-based matching algorithm
    """
    
    try:
        # In production, this would query database
        # For now, return mock matched user
        
        return FindMatchResponse(
            matched_user_id="anon_user_" + request.user_id[-4:],
            match_score=87,
            common_stress=request.main_stress,
            message=f"Great! You're matched with someone who also struggles with {request.main_stress}. Start chatting anonymously!"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.post("/api/send-message")
async def send_message(request: SendMessageRequest):
    """
    Send anonymous message to matched peer
    POWERED BY: Firebase (in production)
    """
    
    try:
        # In production, this would save to database
        # For now, return success
        
        from datetime import datetime
        
        return {
            "success": True,
            "message_id": 12345,
            "sent_at": datetime.now().isoformat(),
            "to_peer": "anonymous",
            "message": request.message
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

