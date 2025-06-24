from fastapi import APIRouter, Body, HTTPException  # <- fixed here

from app.services.compare import compare_with_job_description, get_missing_keywords
router = APIRouter()

@router.post("/match/compare")
def compare_resume_to_job(job_description: str = Body(..., embed=True)):
    result = compare_with_job_description(job_description)
    missing_keywords = get_missing_keywords(job_description)

    return {
        "result": result,
        "missing_keywords": missing_keywords
    }
