# app/api/chat.py

from fastapi import APIRouter, Query
from app.services import resume  # to access VECTORSTORE
from app.services.rag import get_rag_chain

router = APIRouter()

@router.get("/ask")
async def ask_question(q: str = Query(..., description="Enter your question")):
    # Check if resume was uploaded first
    if resume.VECTORSTORE is None:
        return {"error": "No resume uploaded yet. Please upload one first."}
    
    # Create RAG pipeline from stored resume
    qa_chain = get_rag_chain(resume.VECTORSTORE)
    
    # Get answer
    answer = qa_chain.run(q)
    
    return {"question": q, "answer": answer}
