import streamlit as st
from utils.gemini_client import ask_gemini

st.title("🎤 AI Interview Coach")

job_role = st.selectbox(
    "Select Role",
    [
        "AI Engineer",
        "Software Developer",
        "Cybersecurity Analyst",
        "Data Scientist"
    ]
)

if st.button("Generate Interview Questions"):

    prompt = f"""
    Generate 10 interview questions for a {job_role}.

    Include:
    - Beginner
    - Intermediate
    - Advanced

    Format clearly.
    """

    result = ask_gemini(prompt)

    st.session_state.questions = result

    st.markdown(result)

if "questions" in st.session_state:

    st.divider()

    st.subheader("Answer a Question")

    answer = st.text_area(
        "Paste your answer here"
    )

    if st.button("Evaluate My Answer"):

        prompt = f"""
        Job Role: {job_role}

        Candidate Answer:

        {answer}

        Evaluate:

        1. Score out of 10
        2. Strengths
        3. Weaknesses
        4. Better Answer
        5. Interview Tips

        Format professionally.
        """

        feedback = ask_gemini(prompt)

        st.markdown(feedback)