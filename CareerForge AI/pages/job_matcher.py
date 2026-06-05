import streamlit as st
from pypdf import PdfReader
from utils.gemini_client import ask_gemini

st.title("🎯 Resume vs Job Matcher")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file and job_description:

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:

        text = page.extract_text()

        if text:
            resume_text += text

    if st.button("Analyze Match"):

        prompt = f"""
Resume:

{resume_text}

Job Description:

{job_description}

Provide:

1. Match Percentage
2. Matching Skills
3. Missing Skills
4. ATS Improvement Tips
5. Recommended Changes

Format professionally.
"""

        result = ask_gemini(prompt)

        st.markdown(result)