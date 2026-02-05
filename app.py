import streamlit as st
from parser import extract_resume_text
from matcher import calculate_match_score

st.title("📄 AI Resume Screening System")
st.write("Upload your resume and check match score with Job Description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here")

if uploaded_file and job_desc:
    resume_text = extract_resume_text(uploaded_file)

    # Updated output
    score, resume_skills, jd_skills = calculate_match_score(resume_text, job_desc)

    st.subheader("📌 Match Score")
    st.write(f"✅ Resume matches JD by: **{score}%**")

    st.subheader("🧠 Skills Found in Resume")
    st.write(resume_skills)

    st.subheader("📌 Skills Required in Job Description")
    st.write(jd_skills)

    missing = [skill for skill in jd_skills if skill not in resume_skills]

    st.subheader("❌ Missing Skills")
    if missing:
        st.write(missing)
    else:
        st.success("No missing skills — Excellent match 🎯")

    # Feedback
    if score > 75:
        st.success("Excellent Match 🎯")
    elif score > 50:
        st.warning("Good Match 👍")
    else:
        st.error("Low Match ❌ Improve skill alignment")
