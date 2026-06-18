# 🚀 AI Career Copilot

[![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=flat-square&logo=google)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ABHISHEKJULA07/ai-career-copilot?style=flat-square)](https://github.com/ABHISHEKJULA07/ai-career-copilot/stargazers)

A full-stack **RAG-powered Generative AI** application that transforms your career journey. AI Career Copilot helps job seekers analyze resumes, evaluate ATS readiness, identify skill gaps, and discover relevant opportunities using cutting-edge AI technology.

**Leveraging Retrieval-Augmented Generation (RAG), Large Language Models, and intelligent resume analysis to boost your chances of getting shortlisted.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Support](#support)

---

## 📖 Overview

**AI Career Copilot** is an intelligent career guidance platform that combines the power of:

- 🧠 **Retrieval-Augmented Generation (RAG)** - Contextual knowledge retrieval
- 🤖 **Large Language Models (Google Gemini)** - Advanced AI understanding
- 📄 **Resume Intelligence** - Smart document analysis
- 🔍 **Vector Search** - Semantic skill matching
- 📊 **Real-Time Analytics** - Actionable insights

Whether you're a fresh graduate or an experienced professional, AI Career Copilot provides personalized guidance to elevate your career prospects.

---

## ✨ Key Features

### 📄 Resume Intelligence
- **Resume Upload & Parsing** - Seamless PDF document upload and content extraction
- **Intelligent Text Processing** - Extract and structure resume data automatically
- **Multi-Format Support** - Handle various resume formats and layouts

### 🎯 ATS Optimization
- **ATS Score Evaluation** - Real-time compatibility scoring against Applicant Tracking Systems
- **Keyword Analysis** - Identify missing high-impact keywords for your target role
- **Format Assessment** - Get feedback on resume structure, layout, and ATS readiness

### 🤖 AI-Powered Analysis
- **Comprehensive Resume Review** - AI-driven deep analysis of your professional profile
- **Quality Assessment** - Evaluate content relevance, impact, and achievements
- **Experience Evaluation** - Analyze work history, skills, and accomplishments

### 💡 Personalized Recommendations
- **Tailored Improvement Suggestions** - Get specific, actionable suggestions to enhance your resume
- **Skill Enhancement Plans** - Identify gaps and receive upskilling recommendations
- **Content Optimization** - Improve description quality, metrics, and impact

### 🔍 Job Matching & Discovery
- **Smart Job Recommendations** - Discover roles aligned with your profile and aspirations
- **Skill Gap Identification** - Know exactly what skills you need for your dream role
- **Market Insights** - Understand current job market trends and in-demand skills

### 🧠 RAG-Based Career Guidance
- **Contextual Insights** - Leverage industry knowledge for personalized advice
- **Experience-Based Learning** - Learn from similar career paths and success stories
- **Real-Time Knowledge Retrieval** - Access up-to-date career guidance and industry trends

### ⚡ Real-Time AI Insights
- **Instant Feedback** - Get immediate AI-powered analysis and suggestions
- **Interactive Guidance** - Receive detailed explanations and improvement strategies
- **Continuous Learning** - Access resources and recommendations for career growth

### 🌐 Interactive Dashboard
- **User-Friendly Interface** - Modern, intuitive React-based dashboard
- **Data Visualization** - Clear charts and graphs for skill analysis
- **Progress Tracking** - Monitor improvements and achievements over time

---

## 🛠️ Tech Stack

### **Frontend**
```
React.js          - Modern UI framework
Vite              - Lightning-fast build tool
JavaScript (ES6+) - Core language
HTML5             - Semantic markup
CSS3              - Responsive styling
Axios             - HTTP client for API calls
```

### **Backend**
```
Python 3.10+      - Core programming language
FastAPI           - Modern, fast web framework
Pydantic          - Data validation and settings
REST APIs         - RESTful API design
Uvicorn           - ASGI server
```

### **AI & Machine Learning**
```
Google Gemini API      - Advanced LLM capabilities
Retrieval-Augmented    - RAG pipeline for contextual AI
Generation (RAG)
Prompt Engineering     - Optimized AI prompts
LLM Integration        - Seamless model integration
Vector Embeddings      - Semantic understanding
```

### **Data Processing & Storage**
```
PDF Processing         - Extract text from PDF resumes
Text Extraction        - Parse resume content
Vector Database        - Store and search embeddings
Vector Search          - Semantic matching capabilities
```

### **Development & Deployment**
```
Git & GitHub           - Version control
VS Code                - Development environment
Postman                - API testing
Virtual Environment    - Python dependency isolation
```

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React + Vite)                  │
│                                                              │
│  Dashboard │ Resume Upload │ Analysis Results │ Insights    │
└───────────────────────┬─────────────────────────────────────┘
                        │ (REST API Calls)
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                  FastAPI Backend                             │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   API        │  │   Resume     │  │   Agents         │  │
│  │   Endpoints  │  │   Parser     │  │   (Controllers)  │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            RAG Pipeline                             │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │   │
│  │  │ Vector   │→ │ Retrieval│→ │ Context Ranking │  │   │
│  │  │ Store    │  │ Module   │  │                │  │   │
│  │  └──────────┘  └──────────┘  └──────────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │   Google Gemini API Integration                     │   │
│  │   (LLM for analysis & recommendations)              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Reports    │  │   Utils      │  │   Config         │  │
│  │   Generator  │  │   Helpers    │  │   Settings       │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│              Data Processing Layer                          │
│                                                              │
│  PDF Parsing │ Text Extraction │ Vector Embeddings         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

Get AI Career Copilot running in 10 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/ABHISHEKJULA07/ai-career-copilot.git
cd ai-career-copilot

# 2. Setup Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Setup Frontend
cd ../frontend
npm install

# 4. Configure Environment (see Configuration section)

# 5. Start Backend (Terminal 1)
cd backend
python main.py

# 6. Start Frontend (Terminal 2)
cd frontend
npm run dev
```

Visit `http://localhost:5173` to access the application.

---

## 💻 Installation

### Prerequisites

- **Python 3.10 or higher**
- **Node.js 16 or higher**
- **npm 8 or higher**
- **Git**
- **Google Gemini API Key** (free tier available)
- **4GB RAM minimum** (8GB recommended)

### Step-by-Step Installation

#### **1. Clone Repository**

```bash
git clone https://github.com/ABHISHEKJULA07/ai-career-copilot.git
cd ai-career-copilot
```

#### **2. Backend Setup**

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### **3. Frontend Setup**

```bash
cd ../frontend

# Install dependencies
npm install

# (Optional) Build for production
npm run build
```

#### **4. Verify Installation**

```bash
# Check Python version
python --version

# Check Node version
node --version

# Check npm version
npm --version
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the `backend` directory:

```env
# Google Gemini Configuration
GEMINI_API_KEY=your_google_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-pro  # or gemini-1.5-flash

# FastAPI Configuration
FASTAPI_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# Server Configuration
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:5173

# CORS Configuration
CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]

# File Upload Configuration
MAX_UPLOAD_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=pdf

# Vector Store Configuration
VECTOR_STORE_PATH=./vectorstore
EMBEDDING_MODEL=google-universal-sentence-encoder

# Resume Analysis Configuration
ATS_WEIGHT=0.3
CONTENT_WEIGHT=0.4
FORMAT_WEIGHT=0.3
```

### Frontend Configuration

Create a `.env` file in the `frontend` directory:

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=AI Career Copilot
VITE_LOG_LEVEL=debug
```

---

## 📖 Usage Guide

### **1. Upload & Analyze Resume**

```bash
# Visit http://localhost:5173
# 1. Click "Upload Resume"
# 2. Select a PDF file (max 10MB)
# 3. Wait for analysis (30-60 seconds)
# 4. Review comprehensive report
```

### **2. View ATS Score**

- Get detailed ATS compatibility assessment
- Identify missing keywords
- Understand format improvements needed
- Get specific recommendations

### **3. Explore Personalized Suggestions**

- Read AI-generated improvement recommendations
- Review skill gap analysis
- Discover relevant job opportunities
- Get career guidance insights

### **4. Track Progress**

- View before/after comparisons
- Monitor suggested improvements
- Track skill development goals

---

## 🔌 API Documentation

### **Base URL**
```
http://localhost:8000/api/v1
```

### **Upload & Analyze Resume**

```http
POST /resume/analyze
Content-Type: multipart/form-data

Request:
- file: PDF file (resume)
- target_role: String (optional) - e.g., "Software Engineer"
- industry: String (optional) - e.g., "Technology"

Response:
{
  "status": "success",
  "data": {
    "ats_score": 82,
    "ats_assessment": {...},
    "skill_analysis": {...},
    "improvement_suggestions": [...],
    "job_recommendations": [...],
    "detailed_report": {...}
  },
  "message": "Resume analysis completed successfully"
}
```

### **Get ATS Score Details**

```http
POST /resume/ats-evaluation
Content-Type: application/json

Request:
{
  "resume_text": "string",
  "job_title": "Software Engineer",
  "keywords": ["Python", "FastAPI", "React"]
}

Response:
{
  "ats_score": 82,
  "missing_keywords": ["Docker", "Kubernetes"],
  "format_issues": [...],
  "optimization_tips": [...]
}
```

### **Get AI Recommendations**

```http
POST /recommendations/personalized
Content-Type: application/json

Request:
{
  "resume_summary": "string",
  "experience_level": "5 years",
  "target_role": "Senior Software Engineer"
}

Response:
{
  "improvements": [...],
  "skill_gaps": [...],
  "learning_resources": [...],
  "career_path": {...}
}
```

### **Get Job Matches**

```http
POST /jobs/match
Content-Type: application/json

Request:
{
  "skills": ["Python", "FastAPI", "React"],
  "experience_level": "mid",
  "location": "Remote"
}

Response:
{
  "jobs": [...],
  "match_scores": [...],
  "skill_alignments": [...]
}
```

---

## 🔄 How It Works

### **Step 1: Resume Upload & Extraction**
```
User uploads PDF resume
         ↓
PDF Parser extracts text
         ↓
Text preprocessing & cleaning
         ↓
Structured resume data
```

### **Step 2: ATS Evaluation**
```
Resume parsed
         ↓
Extract keywords & skills
         ↓
Compare with ATS patterns
         ↓
Calculate compatibility score
         ↓
Generate ATS feedback
```

### **Step 3: RAG Pipeline Processing**
```
Resume content
         ↓
Generate vector embeddings
         ↓
Retrieve relevant context from vector store
         ↓
Rank retrieved documents by relevance
         ↓
Prepare context for LLM
```

### **Step 4: AI Analysis with Gemini**
```
Resume + Retrieved context
         ↓
Send to Google Gemini API
         ↓
AI analyzes with contextual knowledge
         ↓
Generate insights & recommendations
         ↓
Create personalized suggestions
```

### **Step 5: Job Matching & Recommendations**
```
Extracted skills & experience
         ↓
Semantic matching with job database
         ↓
Calculate compatibility scores
         ↓
Rank job opportunities
         ↓
Present recommendations
```

### **Step 6: Report Generation**
```
All analyses consolidated
         ↓
Create comprehensive report
         ↓
Format for dashboard display
         ↓
Send to frontend
         ↓
User views interactive dashboard
```

---

## 📂 Project Structure

```
AI-Career-Copilot/
│
├── backend/
│   ├── agents/                      # AI Agent Controllers
│   │   ├── resume_agent.py         # Resume analysis agent
│   │   ├── ats_agent.py            # ATS evaluation agent
│   │   ├── recommendation_agent.py # Recommendation engine
│   │   └── job_match_agent.py      # Job matching agent
│   │
│   ├── rag/                         # RAG Pipeline
│   │   ├── retriever.py            # Document retrieval
│   │   ├── embeddings.py           # Embedding generation
│   │   ├── context_manager.py      # Context preparation
│   │   └── prompt_manager.py       # Prompt engineering
│   │
│   ├── reports/                     # Report Generation
│   │   ├── report_generator.py     # Generate reports
│   │   ├── formatter.py            # Format output
│   │   └── templates/              # Report templates
│   │
│   ├── utils/                       # Utility Functions
│   │   ├── pdf_parser.py           # PDF extraction
│   │   ├── text_processor.py       # Text processing
│   │   ├── validators.py           # Input validation
│   │   └── logger.py               # Logging
│   │
│   ├── vectorstore/                 # Vector Store
│   │   ├── vector_db.py            # Vector database
│   │   ├── embeddings_store.py     # Embedding storage
│   │   └── search.py               # Vector search
│   │
│   ├── models/                      # Pydantic Models
│   │   ├── resume.py               # Resume data model
│   │   ├── analysis.py             # Analysis models
│   │   └── responses.py            # Response schemas
│   │
│   ├── main.py                      # FastAPI app entry point
│   ├── config.py                    # Configuration settings
│   ├── requirements.txt             # Python dependencies
│   └── .env.example                 # Environment template
│
├── frontend/
│   ├── public/                      # Static assets
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── components/              # Reusable components
│   │   │   ├── ResumeUpload.jsx
│   │   │   ├── AnalysisDashboard.jsx
│   │   │   ├── ATSScore.jsx
│   │   │   ├── Recommendations.jsx
│   │   │   ├── JobMatches.jsx
│   │   │   └── SkillGapAnalysis.jsx
│   │   │
│   │   ├── pages/                   # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── Analysis.jsx
│   │   │   └── Results.jsx
│   │   │
│   │   ├── services/                # API services
│   │   │   ├── api.js              # API calls
│   │   │   └── geminiService.js    # Gemini integration
│   │   │
│   │   ├── styles/                  # CSS files
│   │   │   ├── global.css
│   │   │   ├── dashboard.css
│   │   │   └── components.css
│   │   │
│   │   ├── App.jsx                  # Main App component
│   │   ├── main.jsx                 # Entry point
│   │   └── index.css                # Global styles
│   │
│   ├── vite.config.js               # Vite configuration
│   ├── package.json                 # Node dependencies
│   ├── .env.example                 # Environment template
│   └── .gitignore
│
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

---

## 🎯 Future Enhancements

### **Phase 2.0**
- 🎤 **Interview Preparation Agent** - AI-powered mock interviews with feedback
- 🎯 **Advanced Job Match Analysis** - Deeper role compatibility scoring
- 📝 **Cover Letter Generator** - Automated cover letter creation
- 🛣️ **AI Career Roadmap Generator** - Personalized growth paths

### **Phase 3.0**
- 🤖 **Mock Interview Simulator** - Video-based practice with AI evaluation
- 🧠 **Multi-Agent Workflow** - Complex task orchestration
- 🔗 **LangGraph Integration** - Advanced workflow management
- 📊 **Advanced Analytics** - Career progression tracking

### **Phase 4.0**
- ☁️ **Cloud Deployment** - AWS/GCP integration
- 🔐 **User Authentication** - Secure account system
- 📱 **Mobile Application** - iOS/Android apps
- 🌍 **Multi-Language Support** - Global accessibility
- 💾 **User Workspace** - Save and manage multiple resumes
- 🔄 **Integration Ecosystem** - LinkedIn, GitHub, Portfolio links

---

## 🤝 Contributing

We love contributions! Here's how to get involved:

### **Fork & Clone**
```bash
git clone https://github.com/YOUR-USERNAME/ai-career-copilot.git
cd ai-career-copilot
git checkout -b feature/your-feature-name
```

### **Make Changes**
```bash
# Make improvements
git add .
git commit -m "feat: Add description of your feature"
git push origin feature/your-feature-name
```

### **Create Pull Request**
1. Go to the original repository
2. Click "Pull Request" → "New Pull Request"
3. Select your fork and branch
4. Add detailed description
5. Submit for review

### **Development Guidelines**

**Python Code**
```bash
# Follow PEP 8
# Use type hints
# Write docstrings
# Add unit tests
```

**JavaScript/React**
```bash
# Use ES6+ features
# Follow Airbnb style guide
# Write functional components
# Use meaningful variable names
```

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

```
MIT License: You're free to use, modify, and distribute this software
for personal and commercial projects.
```

---

## 👨‍💻 Author

**Abhishek Jula**  
*AI/ML Engineer | Generative AI Enthusiast | Full-Stack Developer*

- 🔗 **GitHub**: [github.com/ABHISHEKJULA07](https://github.com/ABHISHEKJULA07)
- 💼 **LinkedIn**: [linkedin.com/in/abhishek-jula0711](https://www.linkedin.com/in/abhishek-jula0711)
- 📧 **Email**: [Contact via GitHub](https://github.com/ABHISHEKJULA07)

---

## 🆘 Support & Help

### **Getting Help**

- 🐛 **Report Issues**: [GitHub Issues](https://github.com/ABHISHEKJULA07/ai-career-copilot/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ABHISHEKJULA07/ai-career-copilot/discussions)
- 📚 **Documentation**: Check the [Wiki](https://github.com/ABHISHEKJULA07/ai-career-copilot/wiki)

### **Common Issues & Solutions**

**Q: "ModuleNotFoundError" when running backend**
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Q: Frontend can't connect to backend**
```
# Solution: Ensure backend is running on port 8000
# Check CORS_ORIGINS in .env file
# Verify API_URL in frontend .env
```

**Q: "Invalid API Key" error**
```
# Solution: 
# 1. Get free Google Gemini API key from https://ai.google.dev
# 2. Add to backend/.env as GEMINI_API_KEY
# 3. Restart backend server
```

**Q: Resume upload fails**
```
# Solution:
# - Ensure file is PDF format
# - Check file size (max 10MB)
# - Verify ALLOWED_EXTENSIONS in .env
```

**Q: AI responses are too generic**
```
# Solution:
# - Try specifying target_role and industry
# - Ensure resume has detailed descriptions
# - Check vector store has relevant context
```

---

## 📊 Repository Stats

![GitHub commits](https://img.shields.io/github/commit-activity/m/ABHISHEKJULA07/ai-career-copilot?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/ABHISHEKJULA07/ai-career-copilot?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ABHISHEKJULA07/ai-career-copilot?style=flat-square)
![Repository size](https://img.shields.io/github/repo-size/ABHISHEKJULA07/ai-career-copilot?style=flat-square)

---

## 🌟 Acknowledgments

- **Google Gemini API** - For powerful LLM capabilities
- **FastAPI** - Modern Python web framework
- **React & Vite** - Amazing frontend technologies
- **Open Source Community** - For inspiration and support
- **Career Professionals** - For invaluable insights

---

## 📝 Changelog

### v1.0.0 (Current Release)
- ✅ Resume upload and parsing
- ✅ ATS score evaluation
- ✅ AI-powered resume analysis
- ✅ Personalized recommendations
- ✅ Job matching system
- ✅ Skill gap identification
- ✅ RAG-based contextual guidance
- ✅ Interactive React dashboard

---

<div align="center">

### Made with ❤️ by [Abhishek Jula](https://github.com/ABHISHEKJULA07)

**If you found this project helpful, consider giving it a ⭐ star!**

[⬆ Back to Top](#-ai-career-copilot)

---

*Your AI-powered career companion for success* 🚀

</div>
