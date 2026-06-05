import streamlit as st

st.set_page_config(
    page_title="Agent Workflow",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 CareerForge AI Agent Workflow")

st.markdown("---")

st.subheader("🚀 How CareerForge AI Works")

st.markdown("""
### 👤 User Input

Skills + Interests + Dream Job

⬇️

### 🎯 Career Agent

Analyzes career goals, interests, and strengths.

⬇️

### 📊 Skill Gap Agent

Identifies missing skills required for target careers.

⬇️

### 📚 Learning Agent

Generates personalized learning roadmaps and certification recommendations.

⬇️

### 📄 Resume Agent

Analyzes resume quality and ATS compatibility.

⬇️

### 🎤 Interview Agent

Creates interview questions and preparation guidance.

⬇️

### 💼 Job Matcher Agent

Matches resumes against job descriptions and calculates compatibility scores.

⬇️

### 📑 Report Agent

Generates a complete AI-powered career report.

⬇️

### 🏆 Career Success Plan

Final personalized career guidance.
""")

st.markdown("---")

st.subheader("⚙️ Multi-Agent Architecture")

st.graphviz_chart("""
digraph {
    rankdir=TB;

    User -> "Career Agent";
    "Career Agent" -> "Skill Gap Agent";
    "Skill Gap Agent" -> "Learning Agent";
    "Learning Agent" -> "Resume Agent";
    "Resume Agent" -> "Interview Agent";
    "Interview Agent" -> "Job Matcher Agent";
    "Job Matcher Agent" -> "Report Agent";
    "Report Agent" -> "Career Success Plan";
}
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 🤖 AI Agents

• Career Agent

• Skill Gap Agent

• Learning Agent

• Resume Agent
""")

with col2:
    st.info("""
### 🚀 Advanced Agents

• Interview Agent

• Job Matcher Agent

• Report Agent

• Career Planning Agent
""")

st.markdown("---")

st.success("✅ CareerForge AI uses a Multi-Agent Architecture for personalized career guidance.")

st.metric(
    label="Active AI Agents",
    value="7"
)