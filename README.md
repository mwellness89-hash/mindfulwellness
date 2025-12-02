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
GROQ_API_KEY=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
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

## API Endpoints
- `POST /api/mood-checkin` - Mood logging + AI CBT  
- `POST /api/thought-reframe` - Cognitive reframing  
- `POST /api/financial-leaks` - Find subscription leaks  
- `GET /health` - Server status  

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

**🚀 100% FREE • Powered by Groq • Ready to run!**

