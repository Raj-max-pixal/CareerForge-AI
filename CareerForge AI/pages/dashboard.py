import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="CareerForge Dashboard",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("CareerForge AI Dashboard")
st.subheader("Personalized Career Intelligence Platform")

st.markdown("---")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Resume Score",
        value="85%"
    )

with col2:
    st.metric(
        label="Job Match Score",
        value="78%"
    )

with col3:
    st.metric(
        label="Skills Count",
        value="12"
    )

with col4:
    st.metric(
        label="Career Readiness",
        value="75%"
    )

st.markdown("---")

# Career Summary
st.subheader("Career Summary")

col1, col2 = st.columns(2)

with col1:
    st.info("""
Dream Career: AI Engineer

Recommended Career: AI / ML Engineer

Industry Demand: High

Salary Range: ₹8 LPA - ₹25 LPA
""")

with col2:
    st.success("""
Next Goals

• Learn Azure AI

• Build AI Agent Projects

• Improve Resume

• Earn Certifications
""")

st.markdown("---")

# Learning Progress
st.subheader("Learning Progress")

st.progress(75)

st.write("Career Readiness Progress: 75%")

st.markdown("---")

# Certifications
st.subheader("Recommended Certifications")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Azure AI Fundamentals")

with col2:
    st.success("Microsoft AI Engineer Associate")

with col3:
    st.success("GitHub Copilot Certification")

st.markdown("---")

# Analytics Chart
st.subheader("Career Progress Analytics")

data = pd.DataFrame({
    "Category": [
        "Skills",
        "Projects",
        "Certifications",
        "Interview",
        "Resume"
    ],
    "Score": [
        75,
        65,
        50,
        80,
        85
    ]
})

fig = px.bar(
    data,
    x="Category",
    y="Score",
    title="Career Progress Overview",
    text="Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# Recent Activity
st.subheader("Recent Activity")

st.write("Career Assessment Completed")
st.write("Resume Analysis Completed")
st.write("Job Match Analysis Completed")
st.write("Interview Preparation Completed")
st.write("Career Report Generated")

st.markdown("---")

# Agent Status
st.subheader("AI Agent Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Career Agent Active")

with col2:
    st.success("Resume Agent Active")

with col3:
    st.success("Interview Agent Active")

st.markdown("---")

st.success(
    "CareerForge AI is actively supporting your career journey."
)