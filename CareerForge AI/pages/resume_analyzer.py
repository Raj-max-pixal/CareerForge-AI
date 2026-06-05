import streamlit as st
from pypdf import PdfReader
from utils.gemini_client import ask_gemini

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    st.success("Resume uploaded successfully!")

    # DEBUG PREVIEW
    st.write("### Extracted Text Preview")
    st.text(resume_text[:1000])

    if st.button("Analyze Resume"):

        prompt = f"""
        You are an expert ATS Resume Analyzer.

        Resume Content:

        {resume_text}

        Analyze and provide:

        1. ATS Score out of 100
        2. Strengths
        3. Weaknesses
        4. Missing Skills
        5. Recommended Certifications
        6. Resume Improvement Suggestions

        Format professionally.
        """

        result = ask_gemini(prompt)

        st.markdown(result)