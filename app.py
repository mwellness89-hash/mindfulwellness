from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import random
import os

app = Flask(__name__)
CORS(app)

# ============================================
# EXISTING ENDPOINTS (Your original 3)
# ============================================

@app.post('/api/mood-checkin')
def mood_checkin():
    """
    Frontend sends: { "mood": 7, "thought": "I'm stressed about bills" }
    Backend responds: { "coaching": "That's valid. Here's what might help..." }
    """
    data = request.json
    mood = data.get('mood', 5)
    thought = data.get('thought', '')
    
    # Generate coaching based on mood
    if mood <= 3:
        coaching = '🆘 You\'re struggling. It\'s okay to ask for help. Reach out to someone you trust. You\'ve gotten through hard times before.'
    elif mood <= 5:
        coaching = '💭 You\'re managing, but there\'s room for relief. Try one small action today. What\'s one thing you can control right now?'
    elif mood <= 7:
        coaching = '✨ You\'re doing okay! Keep the momentum. What small win can you celebrate today?'
    else:
        coaching = '🏆 You\'re thriving! Help someone else. Kindness boosts your mood even more.'
    
    return jsonify({
        'success': True,
        'mood': mood,
        'coaching': coaching,
        'timestamp': str(datetime.now())
    })


@app.post('/api/thought-reframe')
def thought_reframe():
    """
    Frontend sends: { "thought": "I'll never be able to save money" }
    Backend responds: { "alternatives": ["I can start small...", "Many people...", "What if..."] }
    """
    data = request.json
    thought = data.get('thought', '')
    
    # Generate reframes using CBT
    alternatives = [
        '🔄 What evidence contradicts this thought? Have you ever saved, even a small amount?',
        '💭 Would you say this to a friend? Try talking to yourself with kindness instead.',
        '📊 What would "good enough" look like instead of "perfect"? Can you start there?',
        '🎯 Is this thought helpful or just scary? What\'s one small step you could take anyway?'
    ]
    
    return jsonify({
        'success': True,
        'original_thought': thought,
        'alternatives': alternatives,
        'timestamp': str(datetime.now())
    })


@app.post('/api/financial-leaks')
def financial_leaks():
    """
    Frontend sends: { "subscriptions": ["netflix 15", "spotify 10", "unused app 5"] }
    Backend responds: { "leaks": [...], "total_savings": 20 }
    """
    data = request.json
    subscriptions = data.get('subscriptions', [])
    
    # Analyze for leaks
    leaks = []
    total_savings = 0
    
    # Simple analysis: subscriptions over $10/month are flagged as potential leaks
    for sub in subscriptions:
        if isinstance(sub, str):
            parts = sub.split()
            if parts:
                name = ' '.join(parts[:-1])
                try:
                    cost = float(parts[-1])
                    if cost > 10:
                        leaks.append({
                            'name': name,
                            'cost': cost,
                            'reason': 'High cost - consider if you use it weekly'
                        })
                        total_savings += cost
                except:
                    pass
    
    return jsonify({
        'success': True,
        'leaks': leaks,
        'total_savings': total_savings,
        'recommendation': f'You could save ${total_savings:.2f}/month by reviewing these subscriptions.'
    })


# ============================================
# NEW ENDPOINT 1: PEER MATCHING
# ============================================

@app.post('/api/peer-matching')
def peer_matching():
    """
    Frontend sends: { "mood": 7, "stress": "high", "concern": "debt" }
    Backend responds: { "name": "Sarah", "mood": 6, "stress": "high", "concern": "debt" }
    """
    data = request.json
    
    # Get user input
    user_mood = int(data.get('mood', 5))
    user_stress = data.get('stress', 'medium')
    user_concern = data.get('concern', 'debt')
    
    # Mock database of other users (replace with real DB later)
    other_users = [
        {
            'id': 'user_001',
            'name': 'Sarah',
            'mood': 6,
            'stress': 'high',
            'concern': 'debt',
            'email': 'sarah@example.com'
        },
        {
            'id': 'user_002',
            'name': 'Jordan',
            'mood': 5,
            'stress': 'high',
            'concern': 'income',
            'email': 'jordan@example.com'
        },
        {
            'id': 'user_003',
            'name': 'Casey',
            'mood': 7,
            'stress': 'medium',
            'concern': 'savings',
            'email': 'casey@example.com'
        },
        {
            'id': 'user_004',
            'name': 'Morgan',
            'mood': 4,
            'stress': 'high',
            'concern': 'expenses',
            'email': 'morgan@example.com'
        }
    ]
    
    # Find best match (same stress level is most important)
    best_match = None
    best_score = -999
    
    for user in other_users:
        score = 0
        
        # Same stress level = 10 points
        if user['stress'] == user_stress:
            score += 10
        
        # Similar mood (within 2 points) = 5 points
        if abs(user['mood'] - user_mood) <= 2:
            score += 5
        
        # Same concern = 3 points
        if user['concern'] == user_concern:
            score += 3
        
        # Update best match
        if score > best_score:
            best_score = score
            best_match = user
    
    # If no good match, pick the first one
    if best_match is None:
        best_match = other_users[0]
    
    # Return matched peer
    return jsonify({
        'success': True,
        'name': best_match['name'],
        'mood': best_match['mood'],
        'stress': best_match['stress'],
        'concern': best_match['concern'],
        'user_id': best_match['id']
    })


# ============================================
# NEW ENDPOINT 2: CHAT SUPPORT
# ============================================

@app.post('/api/chat-message')
def chat_message():
    """
    Frontend sends: { "message": "I'm anxious about debt", "conversation_id": "conv_123" }
    Backend responds: { "reply": "That's common. Here are 3 steps..." }
    """
    data = request.json
    
    # Get user input
    user_message = data.get('message', '')
    conversation_id = data.get('conversation_id', 'default')
    
    # List of helpful responses
    responses = [
        {
            'keywords': ['debt', 'owe', 'credit card', 'loan'],
            'reply': '💬 Debt is stressful. Here are 3 steps: 1) List all debts, 2) Pay minimum on all, 3) Focus extra payments on smallest debt. You\'re not alone in this.'
        },
        {
            'keywords': ['savings', 'save', 'emergency fund', 'money'],
            'reply': '💰 Starting to save is tough. Begin with $5/week. It\'s not about the amount, it\'s about building the habit. You can do this!'
        },
        {
            'keywords': ['income', 'job', 'money', 'earn', 'unemployed'],
            'reply': '💼 Income uncertainty is scary. Focus on what you can control today. What skills do you have? Let\'s talk about options.'
        },
        {
            'keywords': ['anxious', 'stressed', 'worried', 'panic', 'scared'],
            'reply': '🧠 Your feelings are valid. Take 5 deep breaths. Breathe in for 4, hold for 4, out for 4. Clear mind = better decisions. You\'ve handled tough things before.'
        },
        {
            'keywords': ['expense', 'spending', 'bills', 'subscription'],
            'reply': '📊 Track your spending for 1 day. Just write it down. You might find hidden expenses. Knowledge is power!'
        }
    ]
    
    # Find best matching response
    best_response = responses[-1]['reply']  # Default response
    
    message_lower = user_message.lower()
    
    for response_obj in responses:
        for keyword in response_obj['keywords']:
            if keyword in message_lower:
                best_response = response_obj['reply']
                break
    
    # Log message (placeholder - would save to database in production)
    print(f"[Chat] User: {user_message}")
    print(f"[Chat] Bot: {best_response}")
    
    # Return response
    return jsonify({
        'success': True,
        'reply': best_response,
        'timestamp': str(datetime.now())
    })


# ============================================
# NEW ENDPOINT 3: AI COACH
# ============================================

@app.post('/api/ai-coach')
def ai_coach():
    """
    Frontend sends: { "user_id": "user_123" }
    Backend responds: { "tip": "You've improved...", "mood_trend": "improving" }
    """
    data = request.json
    
    # Get user ID
    user_id = data.get('user_id', 'default_user')
    
    # Mock user mood history (replace with real DB later)
    mood_history = {
        'default_user': [5, 5, 6, 6, 7, 7, 8],  # 7 days of mood data
    }
    
    # Get this user's history (or create default)
    history = mood_history.get(user_id, [5, 5, 6, 6, 7, 8, 8])
    
    # Calculate trend
    if len(history) >= 2:
        first_half_avg = sum(history[:len(history)//2]) / (len(history)//2)
        second_half_avg = sum(history[len(history)//2:]) / (len(history) - len(history)//2)
        improvement = second_half_avg - first_half_avg
    else:
        improvement = 0
    
    # Determine mood trend
    if improvement > 1:
        trend = 'improving'
        trend_emoji = '📈'
    elif improvement < -1:
        trend = 'declining'
        trend_emoji = '📉'
    else:
        trend = 'stable'
        trend_emoji = '➡️'
    
    # List of coaching tips based on current mood
    current_mood = history[-1] if history else 5
    
    if current_mood <= 3:
        tips = [
            '🆘 You\'re going through a tough time. It\'s okay to ask for help. Reach out to someone you trust.',
            '💡 When everything feels hard, focus on ONE small win today. Just one.',
            '🧠 Deep breaths. Your feelings are temporary. You\'ve gotten through hard times before.'
        ]
    elif current_mood <= 5:
        tips = [
            '💰 Start tracking one expense today. Awareness is the first step to change.',
            '📊 You\'re managing. Try one small money win: Cancel one unused subscription.',
            '🎯 Set one financial goal for this week. Make it small and achievable.'
        ]
    elif current_mood <= 7:
        tips = [
            '✨ Your mood is improving! Keep doing what you\'re doing.',
            '💪 You\'ve built momentum. Add one more positive habit to your routine.',
            '🎉 Celebrate this week. You\'re making progress!'
        ]
    else:
        tips = [
            '🏆 You\'re in a great place! Help someone else today. Kindness boosts mood even more.',
            '⭐ Your mood is strong. Now focus on building resilience for when stress returns.',
            '🚀 You\'re thriving! Set a bigger financial goal. You\'ve got this!'
        ]
    
    # Pick a random tip
    selected_tip = random.choice(tips)
    
    # Return coaching
    return jsonify({
        'success': True,
        'tip': selected_tip,
        'mood_trend': trend,
        'trend_emoji': trend_emoji,
        'current_mood': current_mood,
        'improvement': round(improvement, 1)
    })


# ============================================
# HEALTH CHECK ENDPOINT
# ============================================

@app.get('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'MindfulWellness API',
        'timestamp': str(datetime.now())
    })


# ============================================
# ROOT ENDPOINT
# ============================================

@app.get('/')
def root():
    return jsonify({
        'message': 'MindfulWellness API is running',
        'endpoints': [
            'POST /api/mood-checkin',
            'POST /api/thought-reframe',
            'POST /api/financial-leaks',
            'POST /api/peer-matching',
            'POST /api/chat-message',
            'POST /api/ai-coach',
            'GET /health'
        ]
    })


# ============================================
# START SERVER
# ============================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)

