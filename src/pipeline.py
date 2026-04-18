def match_resume_to_job(resume_skills, job_skills):
    """
    Weighted skill matching
    """

    # Skill importance weights
    skill_weights = {
        "python": 3,
        "machine learning": 3,
        "deep learning": 3,
        "tensorflow": 3,
        "sql": 2,
        "pandas": 2,
        "numpy": 2,
        "data analysis": 2,
    }

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    total_weight = 0
    matched_weight = 0

    for skill in job_set:
        weight = skill_weights.get(skill, 1)
        total_weight += weight

        if skill in matched:
            matched_weight += weight

    score = (matched_weight / total_weight) * 100 if total_weight else 0

    return {
        "score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }