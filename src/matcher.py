import re

def extract_skills(text):
    text = text.lower()

    skills_db = {
        "python": ["python"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning", "dl"],
        "nlp": ["nlp", "natural language processing"],
        "numpy": ["numpy"],
        "pandas": ["pandas"],
        "tensorflow": ["tensorflow"],
        "keras": ["keras"],
        "scikit-learn": ["scikit-learn", "sklearn"],
        "pytorch": ["pytorch"],
        "sql": ["sql"],
        "data analysis": ["data analysis"],
        "docker": ["docker"],
        "aws": ["aws"],
        "git": ["git"]
    }

    found_skills = set()

    text = re.sub(r'\s+', ' ', text)

    for skill, variations in skills_db.items():
        for variant in variations:
            pattern = r'\b' + re.escape(variant) + r'\b'
            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return list(found_skills)