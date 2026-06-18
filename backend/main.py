from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rag.parser import extract_text
from agents.resume_agent import analyze_resume
from agents.ats_agent import ats_analysis
from agents.job_match_agent import calculate_match
from agents.interview_agent import generate_questions

app = FastAPI(title="AI Career Copilot API")

# CORS Middleware setup for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite/React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Career Copilot API Running"
    }

@app.post("/analyze-resume")
async def resume_analysis(file: UploadFile = File(...)):
    # Extract text using your custom RAG parser
    text = extract_text(file.file)
    result = analyze_resume(text)
    
    return {
        "analysis": result
    }

@app.post("/ats-score")
async def ats_score(file: UploadFile = File(...)):
    # Extract text using your custom RAG parser
    text = extract_text(file.file)
    result = ats_analysis(text)
    
    return {
        "ats": result
    }

@app.post("/resume-match")
async def resume_match(file: UploadFile = File(...)):

    text = extract_text(file.file)

    result = calculate_match(text)

    return result

@app.post("/interview-questions")
async def interview_questions(file: UploadFile = File(...)):

    text = extract_text(file.file)

    result = generate_questions(text)

    return {
        "questions": result
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)