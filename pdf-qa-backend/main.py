from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import shutil
import uuid

# Import your service
from services.langchain_service import answer_from_pdf
from schemas.pdf_schema import PDFDocument, QARequest


# Load environment variables
load_dotenv()

# Setup FastAPI
app = FastAPI()

# Enable CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store PDFs here
UPLOAD_DIR = "pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# In-memory DB substitute (or use SQLite later)
pdf_store = {}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_ext = file.filename.split(".")[-1]
        if file_ext.lower() != "pdf":
            raise HTTPException(status_code=400, detail="Only PDF files allowed.")

        pdf_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{pdf_id}.pdf")

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Save path in simple store
        pdf_store[pdf_id] = file_path

        return {"pdf_id": pdf_id, "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask")
async def ask_question(pdf_id: str = Form(...), question: str = Form(...)):
    try:
        if pdf_id not in pdf_store:
            raise HTTPException(status_code=404, detail="PDF not found.")

        file_path = pdf_store[pdf_id]
        answer = answer_from_pdf(file_path, question)

        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
