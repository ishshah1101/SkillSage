from fastapi import APIRouter, UploadFile, File
import os
from app.services.parser import extract_text_from_pdf
from app.vectorstore.store import create_vectorstore_from_text
from app.state.resume_state import set_resume_text

router = APIRouter()

VECTORSTORE = None

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    global VECTORSTORE

    # 1. Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # 2. Extract text
    extracted_text = extract_text_from_pdf(temp_path)

    # 3. Delete temp file
    os.remove(temp_path)

    # 4. Create vectorstore (for chatbot)
    VECTORSTORE = create_vectorstore_from_text(extracted_text)

    # 5. Store plain text for JD comparison
    set_resume_text(extracted_text)

    return {
        "filename": file.filename,
        "message": "Resume processed and stored successfully ✅",
        "chunk_preview": extracted_text[:300]
    }
