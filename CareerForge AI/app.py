import streamlit as st

st.set_page_config(
    page_title="CareerForge AI",
    page_icon="🚀",
    layout="wide"
)

st.title("CareerForge AI")

st.markdown("""
### Personalized Career Intelligence Platform

CareerForge AI helps students and professionals with:

- Career Assessment
- Resume Analysis
- Interview Preparation
- Job Matching
- Career Roadmaps
- Certification Recommendations
- AI Career Reports

Use the sidebar on the left to access all modules.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("Career Assessment")

with col2:
    st.info("Resume Analyzer")

with col3:
    st.info("Interview Coach")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("Job Matcher")

with col5:
    st.info("Agent Workflow")

with col6:
    st.info("Career Reports")

st.markdown("---")

st.success("CareerForge AI is ready to use.")