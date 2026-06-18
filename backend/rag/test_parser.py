from rag.parser import extract_text

text = extract_text("data/Linkedin_CV.pdf")

print(text[:1000])