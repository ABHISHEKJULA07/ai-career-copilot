import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Instantiates the global client
client = genai.Client()

def analyze_resume(text: str) -> str:
    # Python requires 4 spaces of indentation inside functions
    prompt = f"""
Analyze the following resume and return a professional recruiter-style report.

Use EXACTLY these sections in this order:

# PROFILE

Full Name:
Email:
Phone:
LinkedIn:
Portfolio/GitHub:

# PROFESSIONAL SUMMARY

Provide a concise 4-5 line summary highlighting the candidate's profile, strengths, and career focus.

# EDUCATION

Include:
• Degree
• College/University
• Graduation Year
• CGPA/Percentage (if available)

# EXPERIENCE 



# TECHNICAL SKILLS

Group skills under categories:
like
Programming Languages c++, SQL, PYTHON

Machine Learning & AI : • Skill 1, Skill 2


Generative AI : • Skill 1, Skill 2

Frameworks & Libraries : Skill 1, Skill 2

Tools & Platforms : Skill 1, Skill 2


# PROJECT SUMMARY

For each project provide:

Project Name

Objective:

Brief Description:

Technologies Used:

Key Achievements:

Limit each project to 4-5 lines.

# RESEARCH PAPERS

For each paper provide:

Paper Title 
Publication Venue 
Research Area 
Contribution Summary

If no research papers are found, mention:
"No research papers found."

# CERTIFICATIONS

List all certifications in bullet format. 

# KEY STRENGTHS

• Strength 1
• Strength 2
• Strength 3
• Strength 4
• Strength 5

# AREAS FOR IMPROVEMENT

• Improvement 1
• Improvement 2
• Improvement 3
• Improvement 4

# RECOMMENDED ROLES

Recommend 5 suitable job roles based on the resume.


Rules:
- Use markdown headings
- Use bullet points
- keep subheading bold
- avoid big main headings
- Keep formatting clean and professional
- Avoid long paragraphs
- Make output ATS-friendly
- Focus on AI/ML, Data Science, GenAI, and Software Engineering roles when relevant

Resume:

{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            # Forcing low temperature guarantees the model strictly 
            # adheres to your ordered Markdown header template
            config=types.GenerateContentConfig(
                temperature=0.1
            )
        )
        return response.text

    except Exception as e:
        error = str(e)

        if "RESOURCE_EXHAUSTED" in error:
            return """
# PROFESSIONAL SUMMARY

Gemini API quota has been exhausted.

# AREAS FOR IMPROVEMENT

• Create a new Gemini API key
• Use a different Google account/project
• Wait for quota reset
• Upgrade Gemini API plan

# STATUS

The application is working correctly.
Only the Gemini API quota has been exceeded.
"""

        elif "API_KEY_INVALID" in error or "INVALID_ARGUMENT" in error:
            return """
# ERROR

Invalid Gemini API Key

# SOLUTION

• Check GEMINI_API_KEY in .env
• Generate a new API key
• Restart backend server
"""

        elif "API key expired" in error:
            return """
# ERROR

Gemini API Key Expired

# SOLUTION

• Generate a new Gemini API key
• Update .env file
• Restart backend server
"""

        else:
            return f"""
# RESUME ANALYSIS FAILED

## ERROR DETAILS
{error}
"""