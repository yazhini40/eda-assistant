import streamlit as st
import pandas as pd
from analyzer import analyze, summary_to_text
from llm import get_llm_insights

st.set_page_config(page_title="EDA Assistant", page_icon="🔍")
st.title("Intelligent EDA Assistant")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary")
    summary = analyze(df)
    st.write(f"**Rows:** {summary['shape'][0]} | **Columns:** {summary['shape'][1]}")
    st.write(f"**Duplicate Rows:** {summary['duplicate_rows']}")

    st.subheader("Missing Values")
    st.dataframe(pd.Series(summary["missing_values"], name="Missing Count"))

    st.subheader("Statistics")
    st.dataframe(pd.DataFrame(summary["statistics"]))

    st.subheader("LLM Insights")
    if st.button("Generate Insights"):
        with st.spinner("Analyzing..."):
            text_summary = summary_to_text(summary)
            insights = get_llm_insights(text_summary)
            st.write(insights)