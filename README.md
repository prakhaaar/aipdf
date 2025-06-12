# 📄 AI-PDF: Fullstack Document Question Answering App

A fullstack application that allows users to upload PDFs and ask intelligent questions about their content using LLMs. Built using **FastAPI**, **LangChain**, **React.js**, and **SQLite**.

---

## 🚀 Features

- 🔼 Upload PDF documents
- 🤖 Ask questions based on PDF content (powered by LangChain/LLamaIndex)
- 🗃️ Store and retrieve document metadata with SQLite
- 🧠 NLP-powered context-aware answers
- ⚛️ Responsive frontend built with React + Tailwind CSS

---

## 🧱 Tech Stack

| Layer       | Tech                            |
|-------------|----------------------------------|
| Frontend    | React.js, Vite, Tailwind CSS     |
| Backend     | FastAPI, LangChain, PyMuPDF      |
| NLP         | OpenAI API via LangChain         |
| Database    | SQLite (via SQLAlchemy)          |
| Storage     | Local file system for PDFs       |

---

## 📂 Project Structure

aipdf/
├──pdf-qa-backend
│ ├── main.py # FastAPI app
│ ├── pdf_processor.py # Extract PDF text
│ ├── qa_engine.py # Answer questions using LangChain
│ ├── database.py # SQLite setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ └── .env.example # Sample env config
├── pdf-qa-frontend/
│ ├── src/
│ │ ├── App.jsx # Main app layout
│ │ ├── api.js # Axios for backend calls
│ │ └── components/
│ │ ├── Upload.jsx # PDF upload UI
│ │ └── Chat.jsx # Ask/answer interface
├── uploads/ # Uploaded PDFs
├── pdfs.db # SQLite database
└── README.md



## ⚙️ Setup Instructions

### 🧠 Backend (FastAPI + LangChain)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Add your OpenAI API key here
uvicorn main:app --reload
🌐 Frontend (React)
bash
Copy
Edit
cd frontend
npm install
npm run dev
Frontend runs on: http://localhost:5173

Backend runs on: http://127.0.0.1:8000

📦 Environment Variables (.env)
Create a .env file inside backend/ with:

env

OPENAI_API_KEY=your_openai_key_here

📌 API Endpoints
Method	Endpoint	Description
POST	/upload_pdf	Upload a PDF file
POST	/ask_question	Ask a question about PDF



