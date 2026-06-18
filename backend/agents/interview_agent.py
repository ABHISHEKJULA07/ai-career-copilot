from google import genai
from google.genai import types  # Imported to pass optional configuration parameters
from dotenv import load_dotenv
import os

load_dotenv()

# Initializes the standard developer client using the 2025+ google-genai SDK
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_questions(text):
    # Clean up whitespace token bloat from raw PDF extraction
    cleaned_text = " ".join(text.split())

    prompt = f"""
Generate interview questions based on this resume. 

Return the response strictly matching this markdown structure without adding any introductory or concluding pleasantries.

# TECHNICAL QUESTIONS
- Question 1
- Question 2
- Question 3
- Question 4
- Question 5

# PROJECT QUESTIONS
- Question 1
- Question 2
- Question 3
- Question 4
- Question 5

# MACHINE LEARNING QUESTIONS
- Question 1
- Question 2
- Question 3
- Question 4
- Question 5

# HR QUESTIONS
- Question 1
- Question 2
- Question 3
- Question 4
- Question 5

Resume:
{cleaned_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        # Optional temperature control: slightly lower numbers keep the questions focused 
        # and heavily anchored to the hard data provided in the resume text.
        config=types.GenerateContentConfig(
            temperature=0.3
        )
    )

    return response.text