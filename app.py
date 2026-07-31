import streamlit as st
from ENGINEERING.UI.pages.video_agent import video_agent_ui
from ENGINEERING.UI.pages.welcome import welcome
from ENGINEERING.UI.pages.image_llm import image_analysis_ui
from ENGINEERING.UI.pages.chat_gpt import ChatGPT
from ENGINEERING.UI.pages.text_processor import text_proc
from ENGINEERING.UI.pages.mp_lr import MP_LR
from ENGINEERING.UI.pages.health_expert import Health_Expert
from ENGINEERING.UI.pages.philosophy_expert import Philosophy_Expert
from ENGINEERING.UI.pages.medical_xray import MAS
from ENGINEERING.CORE.rag import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain,user_input
from ENGINEERING.UI.pages.dev_resume import Dev_Resume
from ENGINEERING.UI.pages.stock_agent import stock_agnt
from ENGINEERING.UI.pages.finance_agent import finance_agnt
from ENGINEERING.UI.pages.recipe_system import recipe_system
from ENGINEERING.UI.pages.research_system import Research_system
from ENGINEERING.UI.pages.kisan_mitra import Kisan_mitra_main
from ENGINEERING.UI.pages.application_tracking_system import ATS
from ENGINEERING.UI.pages.multi_agents_chain import Multi_Agents_Chain_UI
from ENGINEERING.UI.pages.ai_chat import AI_Chatbot
from ENGINEERING.UI.pages.image_to_video import Image_2_video
from ENGINEERING.UI.pages.wikipedia import Mypedia
from ENGINEERING.UI.navigation import render_sidebar
from ENGINEERING.UI.pages.image_generation import (
    IT_2_Image,
    IT_2_Image2,
    Text_2_Image2,
    Image_2_Image_Overlaping,
    Image_2_Image_Overlaping1,
)

st.set_page_config(
    page_title="Project BRAHMA",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def Automation():
        st.warning("Under Maintainance")

def main():
    try:
        selected_app = render_sidebar()
        if selected_app == None:
            welcome()
        elif selected_app == "1: Wikipedia Search":
            Mypedia()
        elif selected_app == '2: AI Chatbot':
            AI_Chatbot()
        elif selected_app == "3: Text Classifier System":
            text_proc()
        elif selected_app == "4: Image Classifier System":
            image_analysis_ui()
        elif selected_app == "5: Medical Diagnosis Agent System":
            MAS()
        elif selected_app == "6: Agentic AI System":
            ChatGPT()
        elif selected_app == "7: Multi Agentic AI System":
            Multi_Agents_Chain_UI()    
        elif selected_app == "10: Finance Agent":
            finance_agnt()
        elif selected_app == "11: Stock Investment Adviser Robot":
            stock_agnt()    
        elif selected_app == "12: Video Summerizer Agent":
            video_agent_ui()     
        elif selected_app == "8: Research Agent":
            Research_system()        
        elif selected_app == "9: Recipe Maker Agent":
            recipe_system()             
        elif selected_app == "14: Text to Image Generator System":
            Text_2_Image2()
        elif selected_app == "15: Image to Image Regenerator System":
            IT_2_Image()    
        elif selected_app == '16: Image to Image Overlaping System':
            Image_2_Image_Overlaping()
        elif selected_app == '17: Image to Video Generator System':
            Image_2_video()                
        elif selected_app == "24: Kisan Mitra Chatbot":
            Kisan_mitra_main()
        elif selected_app == "18: Application Tracking System":
            ATS()
        elif selected_app=="20: Health Expert System":
            Health_Expert()
        elif selected_app=="22: MPLRC Expert System":
            MP_LR()    
        elif selected_app=="23: Philosophy Expert System":
            Philosophy_Expert()
        elif selected_app=="26: Developer Resume":
            Dev_Resume()
        elif selected_app=="27: Automate Your Desktop":
            Automation()    
        elif  selected_app == "13: Retrieval Augmented Generation System":
          with st.sidebar:
           st.title("Menu:")
           pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
           if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")
          user_question=st.text_input("Ask a question from pdf files.")
          if user_question:
            with st.spinner("Processing..."):
             user_input(user_question)
             st.success("Done")
    except IOError as e:
        print(f"An error occurred: {e}")
    st.caption("This Lab is for AI Research and educational purposes only, not for Business")

if __name__ == "__main__":
   main()

  