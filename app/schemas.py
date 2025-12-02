"""
Pydantic Schemas for request/response validation
"""

from pydantic import BaseModel
from typing import Optional, List

class MoodCheckInRequest(BaseModel):
    user_id: str
    mood_score: int
    stress_reason: str

class MoodCheckInResponse(BaseModel):
    user_id: str
    mood_score: int
    ai_response: str
    next_step: str
    mood_logged: bool

class ThoughtReframeRequest(BaseModel):
    user_id: str
    negative_thought: str

class ThoughtReframeResponse(BaseModel):
    user_id: str
    original: str
    alternatives: List[str]
    cbt_technique: str

class FinancialLeakRequest(BaseModel):
    user_id: str
    csv_data: str

class FinancialLeakResponse(BaseModel):
    user_id: str
    leaks_found: str
    mental_frame: str
    total_savings: Optional[float] = None

