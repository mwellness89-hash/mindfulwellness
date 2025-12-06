# MindfulWellness MVP - 100% FREE

AI Mental Health + Financial Stress Relief Platform

**Cost: $0**  
**Powered by: Groq (Free API)**

## Quick Start

### 1. Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Configure Environment
Your `.env` file is already created:
GROQ_API_KEY=your_groq_key_here
GOOGLE_API_KEY=AIzaSyBt89gPI5iUQU0SU14V_cvDj_PfTRg6LfY
DATABASE_URL=sqlite:///mindfulwellness.db
ENVIRONMENT=development
DEBUG=True

### 3. Run Server
uvicorn main:app --reload
Server runs at http://localhost:8000

### 4. Test API
In new terminal (venv active):
python test_api.py

## Endpoints (6 Total)

### Original 3 Endpoints
- `POST /api/mood-checkin` - Mood logging + AI CBT response
- `POST /api/thought-reframe` - Cognitive reframing (3 alternatives)
- `POST /api/financial-leaks` - Find subscription leaks

### NEW Day 2 Endpoints (Peer Matching)
- `POST /api/find-match` - Find accountability partner with matching profile
- `POST /api/send-message` - Send anonymous message to matched peer

### Health
- `GET /health` - Server status check
  

## Project Structure ✅  
✅ .env (keys loaded)  
✅ app/__init__.py  
✅ app/models.py (SQLAlchemy)  
✅ app/schemas.py (Pydantic)  
✅ app/routes.py (Groq AI)  
✅ main.py (FastAPI)  
✅ .gitignore  
✅ test_api.py  
✅ README.md ← CURRENT  
## Status
✅ MVP Version 0.2.0
✅ 6 Core endpoints working
✅ Peer matching algorithm built
✅ Anonymous chat backend ready
✅ All 6 tests passing
✅ 100% FREE (Groq)
✅ Ready for beta testing

**🚀 100% FREE • Powered by Groq • Ready to run!**

