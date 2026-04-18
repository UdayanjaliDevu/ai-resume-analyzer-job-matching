import streamlit as st
import uuid
import os

from src.parser import read_resume
from src.preprocessing import clean_text
from src.matcher import extract_skills
from src.ai_matcher import semantic_match, full_text_match

# PAGE CONFIG
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer with Job Matching")
st.write("Analyze how well your resume matches a job description using AI")

st.write("---")

# INPUTS
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "txt", "docx"])

with col2:
    job_description = st.text_area("💼 Paste Job Description")

analyze = st.button("🔍 Analyze Resume")

if analyze:

    if uploaded_file is not None and job_description:

        # Save temp file
        os.makedirs("temp", exist_ok=True)
        temp_path = f"temp/{uuid.uuid4()}.pdf"

        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            # =========================
            # RESUME PROCESSING
            # =========================
            raw_text = read_resume(temp_path)
            cleaned_text = clean_text(raw_text)
            resume_skills = extract_skills(cleaned_text)

            # =========================
            # JOB PROCESSING
            # =========================
            job_cleaned = clean_text(job_description)

            # 🔥 IMPORTANT: ONLY THIS LINE (NO .split())
            job_skills = extract_skills(job_cleaned)

            # =========================
            # MATCHING
            # =========================
            skill_result = semantic_match(resume_skills, job_skills)
            full_score = full_text_match(cleaned_text, job_cleaned)

            st.write("---")

            # =========================
            # SCORE
            # =========================
            st.subheader("📊 Match Score")
            st.progress(int(full_score))
            st.write(f"### {full_score}% Match")

            if full_score > 80:
                st.success("🔥 Strong Match")
            elif full_score > 60:
                st.warning("⚡ Moderate Match")
            else:
                st.error("❌ Low Match")

            st.write("---")

            # =========================
            # SKILLS DISPLAY
            # =========================
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📄 Resume Skills")
                st.write(resume_skills)

            with col2:
                st.subheader("💼 Job Skills")
                st.write(job_skills)

            st.write("---")

            # =========================
            # MATCH DETAILS
            # =========================
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✔ Matched Skills")
                st.success(skill_result["matched_skills"])

            with col2:
                st.subheader("✘ Missing Skills")
                st.error(skill_result["missing_skills"])

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    else:
        st.warning("⚠ Please upload resume and enter job description")