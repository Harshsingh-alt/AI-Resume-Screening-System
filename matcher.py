from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Main skills/keywords list (you can expand later)
SKILLS = [
    "mern", "react", "next.js", "node.js", "express",
    "mongodb", "rest", "rest api", "websocket", "socket.io",
    "javascript", "html", "css", "sql",
    "c++", "trie", "bm25", "search engine",
    "machine learning", "bert", "word2vec", "glove",
    "git", "github", "deployment", "vercel", "render"
]

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in SKILLS if skill in text]
    return found

def calculate_match_score(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_desc)

    # Convert skill lists into strings
    resume_filtered = " ".join(resume_skills)
    jd_filtered = " ".join(jd_skills)

    if len(jd_skills) == 0:
        return 0.0, resume_skills, jd_skills

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_filtered, jd_filtered])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    score = round(similarity * 100, 2)

    return score, resume_skills, jd_skills
