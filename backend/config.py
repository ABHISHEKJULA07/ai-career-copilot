from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY FOUND:", os.getenv("GEMINI_API_KEY")[:10])