from src.parser import read_resume
from src.preprocessing import clean_text
from src.matcher import extract_skills
from src.ai_matcher import semantic_match, full_text_match


file_path = "data/sample_resume.txt"
# file_path = "data/sample_resume.pdf"
# file_path = "data/sample_resume.docx"


job_description = """
Looking for a strong Python developer with expertise in machine learning,
deep learning, TensorFlow, and data analysis. Must have experience with SQL,
Pandas, and NumPy. Bonus: Docker, AWS.
"""


try:
    # Resume processing
    raw_text = read_resume(file_path)
    cleaned_text = clean_text(raw_text)
    resume_skills = extract_skills(cleaned_text)

    # Job processing
    job_cleaned = clean_text(job_description)
    job_skills = extract_skills(job_cleaned)

    # AI Matching (skills)
    skill_result = semantic_match(resume_skills, job_skills)

    # AI Matching (full resume)
    full_score = full_text_match(cleaned_text, job_cleaned)

    # OUTPUT
    print("\n==============================")
    print("📄 RESUME SKILLS")
    print("==============================")
    for skill in resume_skills:
        print(f"- {skill}")

    print("\n==============================")
    print("💼 JOB SKILLS")
    print("==============================")
    for skill in job_skills:
        print(f"- {skill}")

    print("\n==============================")
    print("🤖 SKILL MATCH (AI)")
    print("==============================")
    print(f"Score: {skill_result['score']} %")

    print("\n✔ Matched Skills:")
    for skill in skill_result["matched_skills"]:
        print(f"  ✔ {skill}")

    print("\n✘ Missing Skills:")
    for skill in skill_result["missing_skills"]:
        print(f"  ✘ {skill}")

    print("\n==============================")
    print("🧠 FULL RESUME MATCH")
    print("==============================")
    print(f"Overall Match Score: {full_score} %")


except Exception as e:
    print(f"Error: {e}")