import streamlit as st

from ENGINEERING.UI.pages.audio_agent import audio_agent_ui
from ENGINEERING.UI.pages.image_agent import image_agent_ui
from ENGINEERING.UI.pages.text_agent import text_agent_ui
from ENGINEERING.UI.pages.video_agent import video_agent_ui

PAGES = {
    "Text Only": text_agent_ui,
    "Text And Image": image_agent_ui,
    "Text And Video": video_agent_ui,
    "Text And Audio": audio_agent_ui,
}

def Multi_Agents_Chain_UI():

    st.markdown(
        """
        <style>
        .stTextArea textarea {
            height:100px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    input_type = st.radio(
        "Select Input Type:",
        options=PAGES.keys(),
        index=None,
    )

    if input_type:
        PAGES[input_type]()
    else:
        st.info("Please Select The Input Type.")