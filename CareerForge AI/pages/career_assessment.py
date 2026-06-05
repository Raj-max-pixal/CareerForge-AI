import streamlit as st
from utils.gemini_client import ask_gemini
from utils.report_generator import create_report

st.title("🎯 CareerForge AI")
st.subheader("Personalized Career Intelligence Agent")

skills = st.text_area(
    "🛠️ Your Skills",
    placeholder="Python, HTML, CSS, JavaScript"
)

interests = st.text_area(
    "❤️ Your Interests",
    placeholder="AI, Machine Learning, Cybersecurity"
)

goal = st.text_input(
    "🚀 Dream Job",
    placeholder="AI Engineer"
)

if st.button("Generate Career Plan"):

    if not skills or not interests or not goal:
        st.warning("Please fill all fields.")
        st.stop()

    with st.spinner("Analyzing your profile..."):

        prompt = f"""
Student Profile

Skills:
{skills}

Interests:
{interests}

Dream Job:
{goal}

Analyze and provide:

# Career Summary

# Top 3 Career Recommendations

# Skill Gap Analysis

# 30-Day Learning Roadmap

# Recommended Certifications

# Salary Expectations

# Industry Demand

# Action Plan
"""

        try:

            result = ask_gemini(prompt)

            st.success("Career Analysis Generated Successfully!")

            st.markdown(result)

            try:

                pdf_file = create_report(result)

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        label="📥 Download Career Report",
                        data=file.read(),
                        file_name="CareerForge_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception:
                st.warning("PDF generation temporarily unavailable.")

        except Exception as e:
            st.error(f"AI Error: {str(e)}")