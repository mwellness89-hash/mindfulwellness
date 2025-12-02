"""
Database Models for MindfulWellness MVP
"""

from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MoodLog(Base):
    __tablename__ = "mood_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    mood_score = Column(Integer)
    stress_reason = Column(Text)
    ai_response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class FinancialLeak(Base):
    __tablename__ = "financial_leaks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    leak_type = Column(String)
    amount = Column(Float)
    description = Column(Text)
    cancellation_template = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class ThoughtReframe(Base):
    __tablename__ = "thought_reframes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    original_thought = Column(Text)
    alternatives = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    profession = Column(String)  # e.g., "Software Engineer"
    salary_range = Column(String)  # e.g., "200k-250k"
    main_stress = Column(String)  # e.g., "debt", "burnout"
    mood_average = Column(Integer)  # 1-10
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PeerMatch(Base):
    __tablename__ = "peer_matches"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id_1 = Column(String, index=True)
    user_id_2 = Column(String, index=True)
    match_score = Column(Integer)  # 1-100 (how similar)
    matched_at = Column(DateTime, default=datetime.utcnow)
    active = Column(String, default="active")  # active or inactive

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer)  # Link to PeerMatch.id
    sender_id = Column(String)  # Anonymous ID
    message = Column(Text)
    sent_at = Column(DateTime, default=datetime.utcnow)

