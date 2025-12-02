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


class UserProfileRequest(BaseModel):
    user_id: str
    profession: str  # e.g., "Software Engineer"
    salary_range: str  # e.g., "200k-250k"
    main_stress: str  # e.g., "debt"
    mood_average: int  # 1-10

class FindMatchResponse(BaseModel):
    matched_user_id: str  # Anonymous ID
    match_score: int  # 0-100
    common_stress: str
    message: str

class SendMessageRequest(BaseModel):
    sender_id: str  # Your anonymous ID
    match_id: int  # ID of your match
    message: str

class SendMessageResponse(BaseModel):
    success: bool
    message_id: int
    sent_at: str

