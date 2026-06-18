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
