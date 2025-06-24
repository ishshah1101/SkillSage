from app.state.resume_state import get_resume_text
### app/services/compare.py

# from app.services.resume import get_resume_text
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import CountVectorizer


def compare_with_job_description(job_description: str) -> str:
    resume_text = get_resume_text()

    if not resume_text:
        return "❌ Resume not uploaded yet."

    # Simple similarity ratio
    similarity = SequenceMatcher(None, resume_text.lower(), job_description.lower()).ratio()

    if similarity > 0.6:
        return f"✅ Resume matches the job description fairly well. Similarity: {similarity:.2f}"
    else:
        return f"⚠️ Partial match. Similarity: {similarity:.2f}"


def extract_keywords(text: str, top_k=50) -> list:
    vectorizer = CountVectorizer(stop_words='english', max_features=top_k)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()


def get_missing_keywords(job_description: str) -> list:
    resume_text = get_resume_text()
    if not resume_text:
        return []

    jd_keywords = set(extract_keywords(job_description))
    resume_keywords = set(extract_keywords(resume_text))

    return list(jd_keywords - resume_keywords)


### app/api/match.py

from fastapi import APIRouter, Body
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
