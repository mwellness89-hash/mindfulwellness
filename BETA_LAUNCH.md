# 🚀 MindfulWellness BETA LAUNCH

## Welcome to the Beta!

We're launching MindfulWellness - AI Mental Health + Financial Stress Relief.

**Status:** 🔴 BETA (Invite-only access)
**Cost:** 💰 FREE forever
**Powered by:** 🤖 Groq AI (no credit card needed)

---

## Your Public API

Your API is now LIVE on the internet:

https://mindfulwellness.onrender.com
---

## Available Features

### 1. Mood Check-in + AI Coaching
POST /api/mood-checkin
Log your mood and get AI-powered CBT guidance.

### 2. Thought Reframing (CBT)
POST /api/thought-reframe
Get 3 alternative thoughts for negative thinking.

### 3. Financial Leak Finder
POST /api/financial-leaks
Find forgotten subscriptions and save money.

### 4. Find Accountability Partner
POST /api/find-match
Get matched with someone with similar stress profile.

### 5. Send Anonymous Message
POST /api/send-message
Chat anonymously with your matched peer.

### 6. Health Check
GET /health
Check if API is running.

---

## How to Test

### Quick Test (Health Check)
```bash
curl https://YOUR_PUBLIC_URL/health
Should return:
{"status":"ok"}
Test Mood Check-in
curl -X POST "https://https://mindfulwellness.onrender.com/api/mood-checkin" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"beta_user_001","mood_score":6,"stress_reason":"worried about finances"}'
Test Find Match
curl -X POST "https://https://mindfulwellness.onrender.com/api/find-match" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"beta_user_001","profession":"Software Engineer","salary_range":"200k-250k","main_stress":"debt","mood_average":6}'
Test Send Message
curl -X POST "https://https://mindfulwellness.onrender.com/api/send-message" \
  -H "Content-Type: application/json" \
  -d '{"sender_id":"anon_user_001","match_id":1,"message":"Hi!"}'
Tech Stack

Backend: FastAPI (Python)

AI: Groq (Free API - no credit card)

Database: SQLite

Hosting: Render (Free tier - unlimited)

Cost: $0 total

Status: Production-ready

Endpoints

Method	Path	Purpose
GET	/health	Server health check
POST	/api/mood-checkin	Log mood + get AI response
POST	/api/thought-reframe	Get CBT alternatives
POST	/api/financial-leaks	Find subscription leaks
POST	/api/find-match	Find accountability partner
POST	/api/send-message	Send anonymous message
Why MindfulWellness?

The Problem:

75% of mental health issues are caused by financial stress

Most mental health apps ignore financial anxiety

Isolation makes it worse

The Solution:

AI coaching for both mental health AND finances

Peer matching to connect with people in same situation

Anonymous chat for judgment-free support

100% free to start

Feedback

We're collecting beta feedback:

What works?

What doesn't?

What would you add?

Email: mwellness89@gmail.com

Next Steps

Week 1: Launch beta (100 users)

Week 2: Collect feedback

Week 3: Add mobile app

Week 4: Series A funding

About

Mission: Make mental health + financial wellness accessible to everyone.

Vision: $1B company helping millions escape financial stress.

Team: Founder building in public

🚀 Welcome to the future of mental wellness!

Let's build something amazing together.

Made with ❤️ by MindfulWellness
Cost: $0 | Launched: Dec 3, 2025
