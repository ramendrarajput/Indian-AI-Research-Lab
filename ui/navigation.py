import streamlit as st


APPLICATIONS1 = {
    1: "AI Chatbot",
    2: "Image Chatbot",
    3: "PDF Chat",
    4: "Health Expert",
    5: "Philosophy Expert",
}

APPLICATIONS = {
    1: "Wikipedia Search",
    2: "AI Chatbot",
    3: "Text Classifier System",
    4: "Image Classifier System",
    5: "Medical Diagnosis Agent System",
    6: "Agentic AI System",
    7: "Multi Agentic AI System",
    8: "Research Agent",
    9: "Recipe Maker Agent",
    10: "Finance Agent",
    11: "Stock Investment Adviser Robot",
    12: "Video Summerizer Agent",
    13: "Retrieval Augmented Generation System",
    14: "Text to Image Generator System",
    15: "Image to Image Regenerator System",
    16: "Image to Image Overlaping System",
    17: "Image to Video Generator System",
    18: "Application Tracking System",
    19: "AI Engineers Recruiter System",
    20: "Health Expert System",
    21: "Music Expert System",
    22: "MPLRC Expert System",
    23: "Philosophy Expert System",
    24: "Kisan Mitra Chatbot",
    25: "Fine-Tune Your Own Model",
    26: "Developer Resume",
    27: "Automate Your Desktop"
}

def render_sidebar():

    st.sidebar.title("Project BRAHMA")
    st.caption("Developer: Ramendra Singh Rajput")
    option = st.sidebar.selectbox(
        "Select Application",
        list(APPLICATIONS.values()),
        index=None
    )
    
    return option

#render_sidebar()

#render_navigation()

#selected_page