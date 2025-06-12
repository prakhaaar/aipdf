from transformers import pipeline
from PyPDF2 import PdfReader

# Load HuggingFace QA pipeline (loads once on startup)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_from_pdf(filepath: str, question: str) -> str:
    try:
        # Read the PDF content
        reader = PdfReader(filepath)
        full_text = ""

        for page in reader.pages[:5]:  # Only first 5 pages to keep it fast
            full_text += page.extract_text() or ""

        if not full_text.strip():
            return "Could not extract readable text from the PDF."

        # Limit input length to avoid overflow
        context = full_text[:4000]

        # Use the QA model to answer the question
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    
    except Exception as e:
        return f"Error: {str(e)}"
