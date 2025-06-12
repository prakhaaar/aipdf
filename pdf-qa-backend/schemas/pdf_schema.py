from pydantic import BaseModel

class PDFDocument(BaseModel):
    file_path: str  # path to the uploaded PDF file

class QARequest(BaseModel):
    question: str   # question asked by the user
    file_path: str  # path of the PDF to extract answer from
