import os
from uuid import uuid4

UPLOAD_FOLDER = "uploads"

def save_pdf(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    filename = f"{uuid4()}.pdf"
    path = os.path.join(UPLOAD_FOLDER, filename)
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())
    return filename, path