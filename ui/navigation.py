import streamlit as st
from config.settings import APP_NAME
from config.settings import DEVELOPER_NAME

APPLICATIONS = [
    "1: Wikipedia Search",
    "2: AI Chatbot",
    "3: Text Classifier System",
    "4: Image Classifier System",
    "5: Medical Diagnosis Agent System",
    "6: Agentic AI System",
    "7: Multi Agentic AI System",
    "8: Research Agent",
    "9: Recipe Maker Agent",
    "10: Finance Agent",
    "11: Stock Investment Adviser Robot",
    "12: Video Summerizer Agent",
    "13: Retrieval Augmented Generation System",
    "14: Text to Image Generator System",
    "15: Image to Image Regenerator System",
    "16: Image to Image Overlaping System",
    "17: Image to Video Generator System",
    "18: Application Tracking System",
    "19: AI Engineers Recruiter System",
    "20: Health Expert System",
    "21: Music Expert System",
    "22: MPLRC Expert System",
    "23: Philosophy Expert System",
    "24: Kisan Mitra Chatbot",
    "25: Fine-Tune Your Own Model",
    "26: Developer Resume",
    "27: Automate Your Desktop"
]

def render_sidebar():

    st.sidebar.title(APP_NAME)
    #st.caption("Developer:" + DEVELOPER_NAME)
    st.sidebar.caption(f"Developer: {DEVELOPER_NAME}")
    option = st.sidebar.selectbox(
        "Select Application",
        APPLICATIONS,
        index=None
    )
    
    return option

#render_sidebar()

#render_navigation()

#selected_page