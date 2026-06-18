RESUME_ANALYSIS_PROMPT = """
Analyze the resume.

Return:

1. Skills
2. Strengths
3. Weaknesses
4. Project Summary
"""

ATS_PROMPT = """
Compare resume with job description.

Return:

ATS Score

Missing Skills

Recommendations
"""

INTERVIEW_PROMPT = """
Generate interview questions.

Role:
{role}

Provide:
Python
SQL
Machine Learning
Generative AI
"""