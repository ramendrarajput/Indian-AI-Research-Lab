import os
from ui.pages.video_agent import video_agent_ui
import streamlit as st
from dotenv import load_dotenv
import speech_recognition as sr
from phi.model.google import Gemini
import openai
from textwrap import dedent
from datetime import datetime
from phi.agent import Agent
from phi.tools.exa import ExaTools
from phi.tools.arxiv_toolkit import ArxivToolkit
import streamlit as st
from agents.base_agent import create_web_multimodal_agent
from ui.pages.welcome import welcome
from ui.pages.image_llm import image_analysis_ui
from ui.pages.chat_gpt import ChatGPT
from ui.pages.text_processor import text_proc
from ui.pages.mp_lr import MP_LR
from ui.pages.health_expert import Health_Expert
from ui.pages.philosophy_expert import Philosophy_Expert
from ui.pages.medical_xray import MAS
from core.rag import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain,user_input
from ui.pages.dev_resume import Dev_Resume
from ui.pages.stock_agent import stock_agnt
from ui.pages.finance_agent import finance_agnt
from ui.pages.kisan_mitra import Kisan_mitra_main
from ui.pages.application_tracking_system import ATS
from ui.pages.recipe_system import recipe_system
from ui.pages.research_system import Research_system
from ui.pages.kisan_mitra import Kisan_mitra_main
from ui.pages.application_tracking_system import ATS
from ui.pages.multi_agents_chain import Multi_Agents_Chain_UI
from ui.pages.ai_chat import AI_Chatbot
import wikipediaapi
from transformers import pipeline
from ui.pages.image_to_video import Image_2_video
from ui.pages.image_generation import (
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

agent = Agent(tools=[ArxivToolkit()], show_tool_calls=True)

#@st.cache(allow_output_mutation=True)
def load_qa_pipeline():
    """
    Loads the Question-Answering pipeline using the DistilBERT model.

    Returns:
        Pipeline: The Question-Answering pipeline.
    """
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return qa_pipeline

def load_wiki(query, language="hi"):
    """
    Searches Wikipedia for the given query in the specified language and returns a summary of the first search result.

    Args:
        query (str): The search query for Wikipedia.
        language (str): The language code for the Wikipedia search (default is "hi" for Hindi).

    Returns:
        str: The summary of the first Wikipedia search result.
    """
    headers = {
        'User-Agent': 'WikiMindAI/1.0 (https://gideonogunbanjo.netlify.app)'
    }
    wiki_wiki = wikipediaapi.Wikipedia(language, headers=headers)
    try:
        page = wiki_wiki.page(query)
        summary = page.summary
        return summary
    # Disambiguation Error Exception
    except wikipediaapi.exceptions.DisambiguationError:
        return "Multiple articles found. Please provide a more specific topic."
    except wikipediaapi.exceptions.HTTPTimeoutError:
        return "No internet connection. Please check your internet connection settings."
    except Exception as e:
        return f"An Error Occurred: {e}"

def answer_questions(pipeline, question, paragraph):
    """
    Uses the Question-Answering pipeline to answer a question based on the given context (paragraph).

    Args:
        pipeline (Pipeline): The Question-Answering pipeline.
        question (str): The question to be answered.
        paragraph (str): The context (paragraph) from which the question should be answered.

    Returns:
        dict: A dictionary containing the answer to the question and additional details.
    """
    input_data = {
        "question": question,
        "context": paragraph
    }
    output = pipeline(input_data)
    return output

def text_to_speech(text, language_code):
    """
    Converts text to speech in the specified language using gTTS.

    Args:
        text (str): The text to be converted to speech.
        language_code (str): The language code for the speech synthesis.

    Returns:
        AudioSegment: The audio segment containing the speech.
    """
    tts = gTTS(text, lang=language_code)
    mp3_data = BytesIO()
    tts.write_to_fp(mp3_data)
    mp3_data.seek(0)
    audio = AudioSegment.from_file(mp3_data, format="mp3")
    return audio

def recognize_speech(language_code):
    """
    Captures audio from the microphone and converts it into text using SpeechRecognition.

    Args:
        language_code (str): The language code for the speech recognition.

    Returns:
        str: The recognized text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        st.write("Could not understand audio.")
    except sr.RequestError as e:
        st.write(f"Error with the service; {e}")

from ui.pages.wikipedia import Mypedia

def Automation():
        st.warning("Under Maintainance")

def main():
    try:
        load_dotenv()  # take environment variables from .env
        openai.api_key=os.getenv("OPENAI_API_KEY")
        from ui.navigation import render_sidebar
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

  