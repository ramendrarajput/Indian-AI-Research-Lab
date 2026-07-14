import streamlit as st
from ui.pages.text_agent import text_agent_ui
from ui.pages.video_agent import video_agent_ui
from ui.pages.image_agent import image_agent_ui
from ui.pages.audio_agent import audio_agent_ui
from agents.base_agent import create_web_multimodal_agent

web_multimodal_agent = create_web_multimodal_agent()

def Multi_Agents_Chain_UI():
    Input_Type = st.radio("Select Input Type:", ("Text Only","Text And Image","Text And Video","Text And Audio"),index=None)
    if Input_Type ==  "Text Only":
       text_agent_ui()
    elif Input_Type=="Text And Video":
        video_agent_ui()       
    elif Input_Type=="Text And Image":
        image_agent_ui()
    elif Input_Type=="Text And Audio":
        audio_agent_ui() 
    else:
     st.info("Please Select The Input Type.")

 # Customize text area height
    st.markdown(
     """
     <style>
     .stTextArea textarea {
         height: 100px;
     }
     </style>
     """,
     unsafe_allow_html=True
 )