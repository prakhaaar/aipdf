from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.models import PDF
from schemas.pdf_schema import PDFUploadResponse, QuestionRequest
from utils.file_handler import save_pdf
from services.langchain_service import answer_from_pdf

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Upload PDF endpoint
@router.post("/upload", response_model=PDFUploadResponse)
def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename, path = save_pdf(file)
    
    # Check for duplicate filenames
    existing = db.query(PDF).filter(PDF.filename == filename).first()
    if existing:
        raise HTTPException(status_code=400, detail="File with this name already exists.")
    
    pdf = PDF(filename=filename, filepath=path)
    db.add(pdf)
    db.commit()
    db.refresh(pdf)
    
    return {"id": pdf.id, "filename": filename}

# Ask question based on uploaded PDF
@router.post("/ask")
def ask_question(request: QuestionRequest, db: Session = Depends(get_db)):
    pdf = db.query(PDF).filter(PDF.id == request.pdf_id).first()
    if not pdf:
        raise HTTPException(status_code=404, detail="PDF not found")

    # Call LangChain/LLM logic
    answer = answer_from_pdf(pdf.filepath, request.question)
    return {"answer": answer}
