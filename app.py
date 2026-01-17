import streamlit as st
from ingestion import ingest_data
from workflow import build_workflow

st.set_page_config(layout="wide")
st.title("Retail Insights Assistant")

mode = st.sidebar.radio("Mode", ["Ingestion", "Q&A"])
if mode == "Ingestion":
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        with open("data.csv", "wb") as f:
            f.write(file.getbuffer())
        if st.button("Ingest"):
            df = ingest_data("data.csv")
            st.success("Data ingested successfully")
            st.dataframe(df.head(10))

if mode == "Q&A":
    question = st.text_input("Ask a question")
    if st.button("Ask") and question:
        workflow = build_workflow()
        result = workflow.invoke({"question": question})
        st.write(result["answer"])
