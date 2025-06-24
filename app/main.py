from fastapi import FastAPI
from app.api import chat, match
from app.services import resume

app = FastAPI(
    title="SkillSage - AI Career Coach",
    description="RAG-powered Resume Analyzer and Career Coach API",
    version="1.0.0"
)

# Routers
app.include_router(resume.router, prefix="/resume", tags=["Resume Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Career Q&A"])
app.include_router(match.router, prefix="/match")

@app.get("/")
async def root():
    return {"message": "SkillSage backend is running 🚀"}
