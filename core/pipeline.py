from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_qa_pipeline():
    """
    Loads the Question-Answering pipeline using the DistilBERT model.

    Returns:
        Pipeline: The Question-Answering pipeline.
    """
    return pipeline(
        task="question-answering",
        model="distilbert-base-uncased-distilled-squad",
    )
