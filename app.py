from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI()

# Allow your GitHub Pages frontend to call this API
origins = [
    "https://mwellness89-hash.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------- MODELS ---------
class PeerMatchRequest(BaseModel):
    mood: int = 5
    stress: str = "medium"
    concern: str = "debt"


class ChatMessageRequest(BaseModel):
    message: str
    conversation_id: str = "default"


class AICoachRequest(BaseModel):
    user_id: str = "default_user"


# --------- HEALTH ---------
@app.get("/health")
async def health():
    return {"status": "ok"}


# --------- ENDPOINT 1: PEER MATCHING ---------
@app.post("/api/peer-matching")
async def peer_matching(payload: PeerMatchRequest):
    user_mood = payload.mood
    user_stress = payload.stress
    user_concern = payload.concern

    other_users = [
        {
            "id": "user_001",
            "name": "Sarah",
            "mood": 6,
            "stress": "high",
            "concern": "debt",
        },
        {
            "id": "user_002",
            "name": "Jordan",
            "mood": 5,
            "stress": "high",
            "concern": "income",
        },
        {
            "id": "user_003",
            "name": "Casey",
            "mood": 7,
            "stress": "medium",
            "concern": "savings",
        },
        {
            "id": "user_004",
            "name": "Morgan",
            "mood": 4,
            "stress": "high",
            "concern": "expenses",
        },
    ]

    best_match = None
    best_score = -999

    for user in other_users:
        score = 0
        if user["stress"] == user_stress:
            score += 10
        if abs(user["mood"] - user_mood) <= 2:
            score += 5
        if user["concern"] == user_concern:
            score += 3
        if score > best_score:
            best_score = score
            best_match = user

    if best_match is None:
        best_match = other_users[0]

    return {
        "success": True,
        "name": best_match["name"],
        "mood": best_match["mood"],
        "stress": best_match["stress"],
        "concern": best_match["concern"],
        "user_id": best_match["id"],
    }


# --------- ENDPOINT 2: CHAT SUPPORT ---------
@app.post("/api/chat-message")
async def chat_message(payload: ChatMessageRequest):
    user_message = payload.message

    responses = [
        {
            "keywords": ["debt", "owe", "credit card", "loan"],
            "reply": "💬 Debt is stressful. Here are 3 steps: 1) List all debts, 2) Pay minimum on all, 3) Focus extra payments on smallest debt. You're not alone in this.",
        },
        {
            "keywords": ["savings", "save", "emergency fund", "money"],
            "reply": "💰 Starting to save is tough. Begin with a tiny weekly amount. It's about building the habit, not perfection.",
        },
        {
            "keywords": ["income", "job", "money", "earn", "unemployed"],
            "reply": "💼 Income uncertainty is scary. Focus on what you can control today. List skills and possible next steps.",
        },
        {
            "keywords": ["anxious", "stressed", "worried", "panic", "scared"],
            "reply": "🧠 Your feelings are valid. Try 5 slow breaths: in for 4, hold for 4, out for 4. Calmer mind, clearer choices.",
        },
        {
            "keywords": ["expense", "spending", "bills", "subscription"],
            "reply": "📊 Track your spending for just 1 day. Awareness often reveals easy places to cut back.",
        },
    ]

    best_response = responses[-1]["reply"]
    message_lower = user_message.lower()

    for response_obj in responses:
        for keyword in response_obj["keywords"]:
            if keyword in message_lower:
                best_response = response_obj["reply"]
                break

    return {
        "success": True,
        "reply": best_response,
        "timestamp": datetime.utcnow().isoformat(),
    }


# --------- ENDPOINT 3: AI COACH ---------
@app.post("/api/ai-coach")
async def ai_coach(payload: AICoachRequest):
    user_id = payload.user_id

    mood_history_db = {
        "default_user": [5, 5, 6, 6, 7, 7, 8],
    }

    history = mood_history_db.get(user_id, [5, 5, 6, 6, 7, 8, 8])

    if len(history) >= 2:
        mid = len(history) // 2
        first_half_avg = sum(history[:mid]) / mid
        second_half_avg = sum(history[mid:]) / (len(history) - mid)
        improvement = second_half_avg - first_half_avg
    else:
        improvement = 0

    if improvement > 1:
        trend = "improving"
        trend_emoji = "📈"
    elif improvement < -1:
        trend = "declining"
        trend_emoji = "📉"
    else:
        trend = "stable"
        trend_emoji = "➡️"

    current_mood = history[-1] if history else 5

    if current_mood <= 3:
        tips = [
            "🆘 This is a tough stretch. Reach out to someone you trust and share what’s going on.",
            "💡 Focus on one tiny win today. Small steps still count.",
            "🧠 Feelings move like waves. Breathe slowly and let this one pass.",
        ]
    elif current_mood <= 5:
        tips = [
            "💰 Track one expense today. Awareness is the first step toward change.",
            "📊 Pick one unused subscription and review if you still need it.",
            "🎯 Set one small money goal for this week that you can definitely hit.",
        ]
    elif current_mood <= 7:
        tips = [
            "✨ You’re building momentum. Repeat one habit that helped this week.",
            "💪 Add one simple positive routine, like a 5‑minute walk or journal.",
            "🎉 Notice one thing you did well today and write it down.",
        ]
    else:
        tips = [
            "🏆 You’re in a strong place. Consider supporting someone else who is struggling.",
            "⭐ Use this good period to set up systems for the next stressful time.",
            "🚀 Dream a bit bigger with your next financial goal and break it into steps.",
        ]

    selected_tip = random.choice(tips)

    return {
        "success": True,
        "tip": selected_tip,
        "mood_trend": trend,
        "trend_emoji": trend_emoji,
        "current_mood": current_mood,
        "improvement": round(improvement, 1),
    }

