def calculate_match(text):

    role_keywords = [
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

    matched = []
    missing = []

    for skill in role_keywords:

        if skill.lower() in text.lower():
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(role_keywords)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }