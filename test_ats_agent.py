from backend.rag.parser import extract_text
from backend.agents.ats_agent import ats_analysis

text = extract_text("backend/data/Linkedin_CV.pdf")

print(ats_analysis(text))