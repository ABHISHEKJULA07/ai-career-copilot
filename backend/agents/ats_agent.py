import os
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ats_analysis(text: str) -> str:

    keywords = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "FastAPI",
        "LangChain",
        "RAG",
        "Docker",
        "AWS"
    ]

    score = 50
    found = []
    missing = []

    for keyword in keywords:
        pattern = rf"\b{re.escape(keyword.lower())}\b"

        if re.search(pattern, text.lower()):
            score += 5
            found.append(keyword)
        else:
            missing.append(keyword)

    if score > 100:
        score = 100

    prompt = f"""
You are an ATS Analyzer.

Resume Score: {score}/100

Skills Found:
{", ".join(found)}

Missing Skills:
{", ".join(missing)}

Provide:

## OVERALL ATS SCORE

## STRENGTHS

## AREAS FOR IMPROVEMENT

## RECOMMENDED ROLES

## STRATEGIC RECOMMENDATIONS

Resume:
{text}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2
            )
        )

        return response.text

    except Exception as e:

        error = str(e)

        if "RESOURCE_EXHAUSTED" in error:

            return f"""
## OVERALL ATS SCORE

{score}/100

## SKILLS FOUND

{", ".join(found)}

## MISSING KEYWORDS

{", ".join(missing)}

## STATUS

Gemini API quota exceeded.

## RECOMMENDATIONS

- Add missing keywords
- Quantify project achievements
- Include deployment experience
"""

        return f"""
## ATS ANALYSIS FAILED

{error}
"""

