from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text_list):
    return model.encode(text_list)


def semantic_match(resume_skills, job_skills):
    """
    Skill-level semantic matching
    """

    resume_embeddings = get_embedding(resume_skills)
    job_embeddings = get_embedding(job_skills)

    matched = []
    missing = []

    for i, job_skill in enumerate(job_skills):
        similarities = cosine_similarity(
            [job_embeddings[i]],
            resume_embeddings
        )[0]

        max_score = max(similarities)

        if max_score > 0.6:
            matched.append(job_skill)
        else:
            missing.append(job_skill)

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    return {
        "score": round(score, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }


def full_text_match(resume_text, job_text):
    """
    Full resume vs job description matching
    """

    embeddings = model.encode([resume_text, job_text])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity * 100, 2)