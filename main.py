import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path

# --- Page config ---
st.set_page_config(page_title="Student Performance Dashboard", page_icon="📊", layout="wide")

# --- Load data ---
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data" / "sample_data.csv"
df = pd.read_csv(csv_path)

# Basic cleanup
if "score" in df.columns:
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

# --- Title and sidebar ---
st.title("Student Performance Dashboard")
st.caption("Insights from the sample student dataset")

with st.sidebar:
    st.header("Filters")
    selected_subject = st.selectbox(
        "Choose a subject to focus on:",
        ["All subjects"] + sorted(df["subject"].dropna().unique().tolist())
    )
    st.markdown("---")
    st.caption("Dataset: sample_data.csv")

# Filter data
if selected_subject != "All subjects":
    filtered_df = df[df["subject"] == selected_subject].copy()
else:
    filtered_df = df.copy()

# --- Key metrics ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Students", len(filtered_df))
with col2:
    st.metric("Average Score", f"{filtered_df['score'].mean():.1f}")
with col3:
    st.metric("Highest Score", f"{filtered_df['score'].max():.0f}")
with col4:
    subject_avg = filtered_df.groupby("subject")["score"].mean()
    highest_subject = subject_avg.idxmax() if not subject_avg.empty else "N/A"
    highest_subject_score = f"{subject_avg.max():.1f}" if not subject_avg.empty else "N/A"
    st.metric("Top Subject Avg", f"{highest_subject} ({highest_subject_score})")

# --- Charts: averages by subject ---
subject_summary = df.groupby("subject", as_index=False)["score"].mean().sort_values("score", ascending=False)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Average Score by Subject")
    st.bar_chart(subject_summary.set_index("subject")["score"])

with right_col:
    st.subheader("Student Count by Subject")
    subject_counts = df["subject"].value_counts()
    st.bar_chart(subject_counts)

# --- Pie chart using matplotlib ---
st.subheader("Subject Share")
fig, ax = plt.subplots(figsize=(6, 5))
subject_pie = df["subject"].value_counts()
ax.pie(subject_pie.values, labels=subject_pie.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# --- Student score table ---
st.subheader("Student Data")
st.dataframe(filtered_df, width="stretch")

# --- Top performers ---
ranked_students = df.sort_values("score", ascending=False).head(10)
st.subheader("Top 10 Students by Score")
st.bar_chart(ranked_students.set_index("name")["score"])

# --- Footer ---
st.markdown("---")
st.caption("Built with Streamlit using the sample CSV dataset.")
