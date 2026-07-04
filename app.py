from prompts.agents.health import HEALTH_PROMPT
import streamlit as st
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import google.generativeai as genai
from google.cloud import texttospeech
import os
from PIL import Image
import gtts
#from playsound import playsound
import multiprocessing
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain.chains.question_answering import load_qa_chain
#from langchain.chains.combine_documents import create_stuff_documents_chain
#from langchain.prompts import PromptTemplate
import speech_recognition as sr
import io
from huggingface_hub import InferenceClient
#from diffusers import AutoPipelineForInpainting
from diffusers.utils import load_image   
import torch

from phi.agent import Agent, RunResponse
#from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
from google.generativeai import upload_file,get_file
import google.generativeai as genai

import time
from pathlib import Path

import tempfile

#from phi.knowledge.pdf import PDFUrlKnowledgeBase
#from phi.vectordb.pgvector import PgVector
#from phi.tools.exa import ExaTools
    
from textwrap import dedent
from datetime import datetime

from phi.agent import Agent
from phi.tools.exa import ExaTools

#from phi.tools.googlesearch import GoogleSearch
from phi.tools.arxiv_toolkit import ArxivToolkit
#from openai import OpenAI

def get_gemini_response_t(question,prompt):
    #model = GenerativeModel('gemini-1.5-flash')
    #model = genai.GenerativeModel('gemini-2.5-flash')
    from core.gemini import get_text_model

    model = get_text_model()
    response = model.generate_content([question,prompt])
    return response.text

#import google.generativeai as genai
#def get_gemini_response_t(question,prompt):
# client = genai.Client(api_key="AIzaSyDGWcTTU4sLb3BoYojLkXfrCdaE8gDcIg4")
# response = client.models.generate_content(
#     question,prompt,model="gemini-2.0-flash"
# )
# return response.text

def get_gemini_response_i(input,image,prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')##('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text

def get_gemini_response_pdf(prompt_template):
    model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.3)
    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain

#####################################################################
def welcome():
    st.markdown(
                """
                Innovating AI for Research and Development.\n
                Welcome to the Indian AI Research Lab, an advanced artificial intelligence platform designed for research, automation, and AI-driven decision-making. Developed by Ramendra Singh Rajput, this lab integrates state-of-the-art AI models to support various applications across multiple domains.

                Key Features:
                - 🔍 Wikipedia Search -Retrieve accurate and relevant information quickly.
                - 🤖 AI Chatbot -Engage in intelligent conversations with a powerful AI chatbot.
                - 📝 Text Classifier System -Automate text analysis and classification.
                - 🖼️ Image Classifier System -Identify and categorize images using AI.
                - 🏥 Medical Diagnosis Agent -Assist in preliminary medical assessments.
                - 🧠 Agentic & Multi-Agent AI Systems -AI-driven automation and problem-solving.
                - 💰 Finance & Investment Agents -Get AI-powered financial advice and stock recommendations.
                - 📽️ Video Summarizer -Condense long videos into concise summaries.
                - 🖌️ AI-Powered Creativity -Generate text-to-image, image regeneration, and video content.
                - 👨‍🌾 Kisan Mitra Chatbot -AI-powered agricultural assistance for farmers.
                - 📚 Retrieval Augmented Generation -Extract insights from documents using AI.
                - 🛠️ AI for Developers & Recruiters -AI-driven developer resume builder and recruitment assistant.
                - 🎵 Expert Systems -AI-based assistance in health, philosophy, music, and more.

                This lab is built for AI research and educational purposes only and aims to empower users with cutting-edge AI solutions. Whether you're a researcher, student, or enthusiast, explore the potential of AI with this innovative platform! 🚀
                """
    )

    #st.markdown(
    #            """
    #            ###### Advanced Artificial Intelligence Brain (AAIB) - A Conversational AI System
    #            The AAIB is a comprehensive conversational AI system designed to provide users with a range of interactive experiences. This system allows users to select from various application types, including text chatbots, image chatbots, ChatGPT, and more. Depending on the user's selection, the system will engage in conversations, provide information, or assist with tasks.
    #            The AAIB is equipped with advanced natural language processing (NLP) capabilities, enabling it to understand and respond to user queries in a human-like manner. The system can also process and analyze large volumes of text data, including PDF files, to provide users with relevant information and insights.
    #            With its modular design, the AAIB can be easily customized and extended to support new application types and use cases. This system has a wide range of potential applications, including customer service, education, healthcare, and more.
    #            Key Features:
    #           
    #            - Advanced NLP capabilities for natural language understanding and response.
    #            - Ability to process and analyze large volumes of text data, including PDF files.
    #            - Modular design for easy customization and extension.
    #            - Potential applications in customer service, education, healthcare, and more.
    #            """
    #)
#####################################################################

##Function to process the user input images
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##############################################################3
# Function to convert speech to text
def speech_to_text():
    #import speech_recognition as sr

 # Create a Recognizer object
 r = sr.Recognizer()

 # Create a Microphone object to capture audio
 mic = sr.Microphone()

 # Set the threshold for the recognizer
 r.energy_threshold = 400

 # Start recording audio from the microphone
 with mic as source:
    print("Speak now!")
    audio = r.record(source, duration=5)

 # Recognize the audio and print the transcription
 try:
    # Use the recognizer to recognize the audio
     text = r.recognize_google(audio)
     print(text)
 except sr.RequestError:
     print("Could not request results from Google Speech Recognition service")
 except sr.UnknownValueError:
     print("Unknown error occurred")
################################################################

#chat applications
def ChatGPT():
    prompt1 = st.chat_input("You can ask anything")
    V_input = st.button("Voice")         # Audio input is inactive due to some prob
    V_enable = st.checkbox('Enable Voice')
    input_prompt = """
                   You are an AI agent of Ramendra. You are an expert in chatting like human and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                   you will have to answer questions based on the user input and perform the task given to you.
                   """
    
   ## If enter button is clicked
    if V_enable==True and prompt1:
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,prompt1)
        if response:
            af=t_2_s(response)
            st.write(response)
            st.success('Done')
            #p = multiprocessing.Process(target=playsound(af), args=(af))
            #p.start()
    elif prompt1:
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,prompt1)
        if response:
            st.success('Done')
            st.write(response)
            
    if V_enable==True and V_input:
        text = speech_to_text()
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,text)
        if response:
            af=t_2_s(response)
            st.write(response)
            st.success('Done')
            #p = multiprocessing.Process(target=playsound(af), args=(af))
            #p.start()
    elif V_input:
        text = speech_to_text()
        st.balloons()
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,text)
        if response:
            st.success('Done')
            st.write(response)
                     
#def check():
    #p = multiprocessing.Process(target=playsound("response.mp3"), args=("response.mp3"))
    #if st.button("Listen"):
    #    p.start()
    #else:
    #    p.stop()
    #if st.checkbox("Enable Voice"):
    #    p.stop()

def text_proc():
    from elevenlabs import play, voices, stream, client
    prompt = st.text_input("You can ask anything")
    input_prompt = """
                   You are an expert in chatting like human. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                   you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark. 
                   """

    if prompt:
        with st.spinner(text='Thinking'):
             response = get_gemini_response_t(input_prompt,prompt)
        if response:
            st.success('Done')
            st.write(response)
            #client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
            client=ElevenLabs() 
            audio=client.generate(
            text= response,
            voice= "Aria",
            #voice="Rashid",
            output_format= "mp3_22050_32",
            #model= "eleven_turbo_v2"
            model= "eleven_multilingual_v2"
            )
            #elevenlabs.play(audio)
    

def MP_LR():
    prompt = st.text_input("Here You can ask anything related to MP Land Record:")
    input_prompt = """
                   You are an expert in understanding Madhya pradesh Land Record. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                   you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.
                   """

    if prompt:
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,prompt)
        if response:
            st.success('Done')
            st.write(response)
            af=t_2_s(response)
                        
def Health_Expert():
    from prompts.agents.health import HEALTH_PROMPT
    prompt = st.text_input("Here You can ask anything related to Health.")
    #input_prompt = """
    #               You are a Health expert. Expert in understanding medical science, human decies etc.Your each and every answer would be related to medical science. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
    #               you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.
    #               """
    input_prompt = HEALTH_PROMPT 
    if prompt:
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,prompt)
        if response:
            st.success('Done')
            st.write(response)
            af=t_2_s(response)
            
def Philosophy_Expert():
    from prompts.agents.philosophy import PHILOSOPHY_PROMPT
    prompt = st.text_input("Here You can ask anything related to Philosophy")
    input_prompt = PHILOSOPHY_PROMPT
    if prompt:
        with st.spinner(text='Thinking'):
            response = get_gemini_response_t(input_prompt,prompt)
        if response:
            st.success('Done')
            st.write(response)
            af=t_2_s(response)
             
def image_proc():
    prompt = st.text_input("Here you can ask anything about uploaded image")
    with st.sidebar:
         #prompt = st.text_input("Ask anything about the image")  
         uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
         image = ""
         if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)
            
    input_prompt1 = """
                     You are an expert in understanding invoices.
                     You will receive input images as invoices &
                     you will have to answer questions based on the input image
                    """
    input_prompt2 = """
                     You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                     You are an expert in understanding images patterns.
                     You will receive input images &
                     you will have to answer questions based on the input image but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.
                    """
    if prompt:
        with st.spinner(text='Thinking'):
             image_data = input_image_setup(uploaded_file)
             response = get_gemini_response_i(input_prompt2, image_data, prompt)
             if response:
               st.success('Done')
               st.write(response)

def MAS():
    prompt="Just give me detailed analysis of this x-ray image of human body and also provide key references at last"
    #prompt = st.text_input("Here you can ask anything about uploaded image")  
    uploaded_file = st.file_uploader("Upload a medical X-ray image", type=["jpg", "jpeg", "png", "pdf"])
    image = ""
    if uploaded_file is not None:
         image = Image.open(uploaded_file)
         st.image(image, caption="Uploaded Image.", use_column_width=True)
            
    input_prompt1 = """
                     You are an expert in understanding invoices.
                     You will receive input images as invoices &
                     you will have to answer questions based on the input image
                    """
    input_prompt2 = """
                     You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                     You are an expert in understanding x-ray images of human body.
                     You will receive input images &
                     you will have to do medical analysis based on the input x-ray image. Firstly check it wether it is x-ray image otherwise just say its not x-ray image. Last line of analisys should contain only profile links of Ramendra singh rajput as water mark.
                    """
    if image:
        with st.spinner(text='Wait...I am analysing it'):
             image_data = input_image_setup(uploaded_file)
             response = get_gemini_response_i(input_prompt2, image_data, prompt)
             if response:
               st.success('Done')
               st.write(response)

def t_2_s(response):

 t=response
 # Select the language for the text to be spoken in
 language = 'en'
 # Create an instance of the gTTS class
 tts = gtts.gTTS(text=t, lang=language, slow=False)
 # Save the audio file
 audio_file = 'response.mp3'
 tts.save(audio_file)
 return audio_file

import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

import subprocess
import platform

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    return output_filepath
    #os_name = platform.system()
    #try:
    #    if os_name == "Darwin":  # macOS
    #        subprocess.run(['afplay', output_filepath])
    #    elif os_name == "Windows":  # Windows
    #        #subprocess.run(['afplay', output_filepath])
    #        subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
    #    elif os_name == "Linux":  # Linux
    #        subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
    #    else:
    #        raise OSError("Unsupported operating system")
    #except Exception as e:
    #    print(f"An error occurred while trying to play the audio: {e}")
##########################################################
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():

    prompt_template = """
    You are an Expert in pdf file reading RAG system. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput . Answer the question as detailed as possible from the provided context. If the question is in hindi then reply in hindi, If the question is in English then reply in english , make sure to provide all the details, if the answer is not in
    provided context, give answer by yourself but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = create_stuff_documents_chain( llm=model,prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain.invoke(
    {
        "context": docs,
        "question": user_question
    }
 )
    st.write(response)
##########################################################
 
def ChatPdf():
    
    def get_pdf_text(pdf_docs):
        text=""
        for pdf in pdf_docs:
            pdf_reader=PdfReader(pdf)
            for page in pdf_reader.pages:
                text+=page.extract_text()
        return  text
    
    def get_text_chunks(text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
        return chunks
    
    def get_vector_store(text_chunks):
     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
     vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
     vector_store.save_local("faiss_index")

    ############################################################################
    
    def get_conversational_chain():

     prompt_template = """
     You are an Expert in pdf file reading RAG system. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput . Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
     provided context just say, "answer is not available in the context", don't provide the wrong answer, last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n\n\n
     Context:\n {context}?\n
     Question:\n{question}\n

     Answer:
     """

     model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

     prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

     return chain
    
    def user_input(user_question):
     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
     new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
     docs = new_db.similarity_search(user_question)

     chain = get_conversational_chain() 

     response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

     print(response)
     st.write(response["output_text"])

    user_question=st.text_input("Ask a question from pdf files.")
    
    if user_question:
        user_input(user_question)
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs=st.file_uploader("Upload your pdf files and click on the submit & process")
        if st.button("Submit & Process") :#and user_input is not None:
            with st.spinner("Processing..."):
                st.balloons()
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

############################################################################
#from fpdf import FPDF
#import base64

# Function to generate PDF
#def create_pdf(text):
#    pdf = FPDF()
#    pdf.set_auto_page_break(auto=True, margin=15)
#    pdf.add_page()
#    #pdf.set_font("Arial", size=12)
#    #pdf.multi_cell(190, 10, text)
#    # Use a Unicode-compatible font
#    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Add a TrueType font
#    pdf.set_font("DejaVu", size=12)

#    # Save PDF to a temporary file
#    pdf_path = "generated_content.pdf"
#    pdf.output(pdf_path, "F")
#    return pdf_path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import base64

#def create_pdf(text):
def create_pdf(text):
    pdf_path = "generated_content.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter  # Get page size

    # Set font
    c.setFont("Helvetica", 12)

    # Set margins
    left_margin = 50
    top_margin = height - 50  # Start from near the top

    # Wrap text to fit within page width
    max_width = width - 100  # Leave margin on both sides
    lines = simpleSplit(text, "Helvetica", 12, max_width)

    # Print each line, adjusting Y position
    y = top_margin
    line_height = 14  # Space between lines

    for line in lines:
        if y < 50:  # Move to new page if reaching bottom margin
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50  # Reset Y position

        c.drawString(left_margin, y, line)
        y -= line_height  # Move to next line

    c.save()
    return pdf_path

    #pdf_path = "generated_content.pdf"
    #c = canvas.Canvas(pdf_path, pagesize=letter)
    #c.setFont("Helvetica", 12)  # Helvetica supports Unicode
    #c.drawString(1, 50, text)  # Adjust position as needed
    #c.save()
    #return pdf_path


# Function to get PDF download link
def get_pdf_download_link(pdf_path, filename="download.pdf"):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_link = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="{filename}">📥 Download PDF</a>'
    return pdf_link

def Dev_Resume():
    prompt = "Show me your Developers Resume."
    input_prompt = """
                   You are a Resume expert. Expert in Resume creating.Here you have to create your developers resume profile his name is Ramendra Singh Rajput. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari since 2015 and have gained greate experience to work with land records, citizence problem solving, land measorment, managing the data of citizence, providing them end to end goverment services in variouse manners. Have gained experience of different different fields work provided by goverment in line order duties. Utilizing this knowledge to develop a powerfull echo system for goverment to help people and solve theire problem in a smart way. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also working on Health Expert System, Music Expert System projects.He is having google developer profile.His education and qualification is Bachelore of computer application from M.I.M.T. college Narsimhapur(2007-2010),  master of computer application from ShriRam Institue Of Technology and Science(2010 to 2012).Active learner for Machine learning, Deep learning and Generative AI.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                   you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
                   """

    if prompt:
        with st.spinner(text='Generating Resume'):
            response = get_gemini_response_t(input_prompt,prompt)
        if response:
            st.success('Done')
            st.write(response)
            #af=t_2_s(response)
            if st.button("Generate PDF"):
              with st.spinner(text='Generating PDF'):
               pdf_path = create_pdf(response)
               st.success("PDF generated successfully! Click below to download.")
               st.markdown(get_pdf_download_link(pdf_path), unsafe_allow_html=True)

############################################################################
##Function to load the model and get the response
#def get_gemini_response_t(question,prompt):
#    model = GenerativeModel('gemini-pro')
#    response = model.generate_content([question,prompt])
#    return response.text

def get_gemini_response(prompt):
    model = GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    return response.text

def Kisan_mitra(lang,prompt):
    input_prompt_e = """
                   You are an agriculture expert in english language. Expert in Answering questions of farmers related to agriculture in english language.Here you have to answer your farmers question in english language. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari since 2015 and have gained great experience to work with land records, citizence problem solving, land measurment, managing the data of citizence, providing them end to end goverment services in variouse manners. Have gained experience of different different fields work provided by goverment in line order duties. Utilizing this knowledge to develop a powerfull echo system for goverment to help people and solve theire problem in a smart way. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also working on Health Expert System, Music Expert System projects.He is having google developer profile.His education and qualification is Bachelore of computer application from M.I.M.T. college Narsimhapur(2007-2010),  master of computer application from ShriRam Institue Of Technology and Science(2010 to 2012).Active learner for Machine learning, Deep learning and Generative AI.Keen in making corelation between phylosophy and quantom physics.His resident Address is Yashoda nagar, Azad ward, Gadarwara(M.P.). His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/, github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput, live projects link: https://advanced-artificial-intelligence-brain.streamlit.app/, Github link for projects: https://github.com/ramendrarajput/ ,
                   you will have to put all links in bottom of page and each link should be seperated by a new line. Have a notification at bottom to contact me to get there business from solved using AI.Last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n 
                   """
    
    input_prompt_h = """
                   You are an agriculture expert in hindi language. Expert in Answering questions of farmers related to agriculture in hindi language.Here you have to answer your farmers question in hindi language. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari since 2015 and have gained great experience to work with land records, citizence problem solving, land measurment, managing the data of citizence, providing them end to end goverment services in variouse manners. Have gained experience of different different fields work provided by goverment in line order duties. Utilizing this knowledge to develop a powerfull echo system for goverment to help people and solve theire problem in a smart way. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also working on Health Expert System, Music Expert System projects.He is having google developer profile.His education and qualification is Bachelore of computer application from M.I.M.T. college Narsimhapur(2007-2010),  master of computer application from ShriRam Institue Of Technology and Science(2010 to 2012).Active learner for Machine learning, Deep learning and Generative AI.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/, github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput, live projects link: https://advanced-artificial-intelligence-brain.streamlit.app/, Github link for projects: https://github.com/ramendrarajput/ ,
                   you will have to put all links in bottom of page and each link should be seperated by a new line. Have a notification at bottom to contact me to get there business from solved using AI.Last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
                   """

    if prompt:
        with st.spinner(text='Wait...I am answering...'):
            if lang=="English":
             response = get_gemini_response_t(input_prompt_e,prompt)
             if response:
              st.success('Done')
              st.write(response)
            elif lang=="Hindi":
             response = get_gemini_response_t(input_prompt_h,prompt)   
             if response:
              st.success('Done')
              st.write(response)

def Kisan_mitra1():
    
    input_prompt = """
                   You are an agriculture expert in hindi language. Expert in Answering questions of farmers related to agriculture in hindi language.Here you have to generate a question on behalf of former regarding the crop disease and answer regarding this disease in hindi language. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari since 2015 and have gained greate experience to work with land records, citizence problem solving, land measorment, managing the data of citizence, providing them end to end goverment services in variouse manners. Have gained experience of different different fields work provided by goverment in line order duties. Utilizing this knowledge to develop a powerfull echo system for goverment to help people and solve theire problem in a smart way. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also working on Health Expert System, Music Expert System projects.He is having google developer profile.His education and qualification is Bachelore of computer application from M.I.M.T. college Narsimhapur(2007-2010),  master of computer application from ShriRam Institue Of Technology and Science(2010 to 2012).Active learner for Machine learning, Deep learning and Generative AI.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , Google developer profile is https://g.dev/ramendrarajput, live projects link: https://advanced-artificial-intelligence-brain.streamlit.app/, Github link for projects: https://github.com/ramendrarajput/ ,
                   you will have to put all links in bottom of page and each link should be seperated by a new line. Have a notification at bottom to contact me to get there business from solved using AI.Last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
                   """

    response = get_gemini_response(input_prompt)
    if response:
     st.success('Done')
     st.write(response)

def Kisan_mitra_main():
    ##initialize our streamlit app
        #st.set_page_config(page_title="Advanced Artificial Intelligence Brain",page_icon="Kisan-Mitra.png")
        #sidebar = st.sidebar(expanded=True)
        #st.subheader("")
        st.caption("किसान मित्र चैटबॉट")
        #st.caption("Developer: Ramendra Singh Rajput")
        prompt=st.chat_input("Enter Your Question Here")
        lang = st.radio("Select Language:", ("Hindi","English"))
        with st.sidebar:
         st.write("प्रिय किसान बंधु,") 
         st.write("    मै आपकी किसानी से संबन्धित किसी भी प्रकार की मदद के लिए अग्रसर एक भाषा मॉडल हू जिसे आर्टिफ़िश्यल इंटेलिजेंस की मशीन लर्निंग पद्धति से बनाया गया है। आप यहा मुझे अपनी समस्या से अवगत कराएं। मै आपके हर सवाल का जवाब देने की पूरी कोशिश करुगा। मेरे निर्माता द्वारा मुझे निरंतर नयी जानकारियों से प्रशिक्षित किया जा रहा है। आपसे हुये संवाद से मै निरंतर सीखता जाता हू।")
         st.write("मैं कृषि से संबंधित आपके सवालों का जवाब दूंगा। मैं एक कृषि विशेषज्ञ हूं और मुझे कृषि संबंधी सवालों का जवाब देने में खुशी होगी।")
         st.write("अपनी पूछताछ साझा करने में संकोच न करें। मैं आपकी कृषि संबंधी चिंताओं को दूर करने में मदद करने के लिए यहां हूं।")
         st.write("    कृपया ध्यान दें कि मैं एक कृत्रिम बुद्धिमत्ता (एआई) द्वारा संचालित चैटबॉट हूं और आपके व्यक्तिगत डेटा तक पहुंच या संग्रह करने में सक्षम नहीं हूं।")
         st.write("निर्माता के बारे मे अधिक जानकारी के लिए आप निर्माता संबंधी प्रश्न कर सकते है।")
         st.write("धन्यवाद!")        
         
        if prompt:
         Kisan_mitra(lang,prompt)
        else:
         Kisan_mitra1()
                

def ATS():
    st.warning("Under development.............!")

def Text_2_Image():
    # Add a text input field for the user to enter the text
  text = st.text_input("Enter the text you want to generate an image for:")

 # Generate the image from the text
  if st.button("Generate"):
    image = get_gemini_response_i(text,prompt="Create an image for given text")
      # Display the generated image
    st.image(image, caption="Generated image",use_column_width=True)
     # Get the output.
    output = image.predictions[0].image_bytes.value

     # Convert the output to a PIL Image object.
    try:
      image = Image.open(io.BytesIO(output))
      st.image(image)
      #image.show()
    except IOError as e:
        print(f"Error opening image: {e}")


#def Text_2_Image1():
#    # Import the necessary libraries.
#
# prompt = st.text_input("Enter your prompt:")
#
# if st.button("Generate Image"):
#       model = ImageGenerationModel.from_pretrained("image-generation-text-to-image")
#       image = model.generate_image(prompt)
#       st.image(image, caption="Generated image",use_column_width=True)
#       #st.image(image)
#       output = image.predictions[0].image_bytes.value
#       try:
#           image = Image.open(io.BytesIO(output))
#           image.show()
#       except IOError as e:
#        print(f"Error opening image: {e}")

def IT_2_Image2():
         
         client = InferenceClient("stabilityai/stable-diffusion-3.5-large",token=os.environ.get("HUGGING_FACE_API_KEY"))#"black-forest-labs/FLUX.1-dev", token=os.environ.get("HUGGING_FACE_API_KEY"))#"Datou1111/shou_xin", token=os.environ.get("HUGGING_FACE_API_KEY"))
         uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
         image = ""
         image = Image.open(uploaded_file)
         st.image(image, caption="Uploaded Image.", use_column_width=True)   
         if uploaded_file is not None:
            prompt = st.text_input("Enter your prompt:")
            if prompt:
                image = client(prompt,image).images[0]
                st.image(image)

def IT_2_Image():
    import torch
    from diffusers import AutoPipelineForImage2Image
    from diffusers.utils import make_image_grid, load_image
    pipeline = AutoPipelineForImage2Image.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    pipeline.enable_model_cpu_offload()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
    init_image = ""
    init_image = Image.open(uploaded_file) 
    st.image(init_image, caption="Uploaded Image.", use_column_width=True)
    if uploaded_file is not None:
            prompt = st.text_input("Enter your prompt:")
            if prompt:
                image = pipeline(prompt, image=init_image).images[0]
                make_image_grid([init_image, image], rows=1, cols=2)


def Text_2_Image2():
    client = InferenceClient("stabilityai/stable-diffusion-3.5-large",token=os.environ.get("HUGGING_FACE_API_KEY"))
    prompt = st.text_input("Enter your prompt:")
  # output is a PIL.Image object
    if st.button("Generate Image"):   
     with st.spinner(text='Wait...I am generating image'):
      image = client.text_to_image(prompt)
      #print(image)
      st.image(image)
      #image.show()
      st.success("Done")

def Image_2_Image_Overlaping1():

    from diffusers import DiffusionPipeline
    pipe = DiffusionPipeline.from_pretrained()#"Lykon/absolute-reality-1.6525-inpainting")#("yisol/IDM-VTON")
    prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
    with st.sidebar:
         #prompt = st.text_input("Ask anything about the image")  
         uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
         image = ""
         if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)
    image = pipe(prompt).images[0]

def Image_2_Image_Overlaping():
    from diffusers import AutoPipelineForInpainting, DEISMultistepScheduler
    import torch
    from diffusers.utils import load_image

    pipe = AutoPipelineForInpainting.from_pretrained('lykon/absolute-reality-1.6525-inpainting', torch_dtype=torch.float16, variant="fp16")
    pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config) 
    pipe = pipe.to("cuda")

    img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
    mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"

    image = load_image(img_url)
    mask_image = load_image(mask_url)


    prompt = "a majestic tiger sitting on a park bench"

    generator = torch.manual_seed(33)
    image = pipe(prompt, image=image, mask_image=mask_image, generator=generator, num_inference_steps=25).images[0]  
    image.save("./image.png")


def Image_2_video():
    pipe = AutoPipelineForInpainting.from_pretrained("diffusers/stable-diffusion-xl-1.0-inpainting-0.1", torch_dtype=torch.float16, variant="fp16").to("cuda")

    img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
    mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"

    image = load_image(img_url).resize((1024, 1024))
    mask_image = load_image(mask_url).resize((1024, 1024))

    prompt = "a tiger sitting on a park bench"
    generator = torch.Generator().manual_seed(0)#device="cuda"

    image = pipe(
    prompt=prompt,
    image=image,
    mask_image=mask_image,
    guidance_scale=8.0,
    num_inference_steps=5,  # steps between 15 and 30 work well for us
    strength=0.99,  # make sure to use `strength` below 1.0
    generator=generator,
).images[0]
    image.show()

## web search agent
Arxiv_paper_agent = Agent(
    name="Arxiv paper agent",
    role="Search the web for Arxiv papers",
    #model=Gemini(id="gemini-2.0-flash-exp"),
    model=Gemini(id="gemini-2.5-flash"),
    tools=[ArxivToolkit()], 
    instructions=["Always include sources and provide reference web links"],
    show_tool_calls=True)

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Gemini(id='gemini-2.5-flash'),#Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo],
    instructions=["Always include sources and provide reference web links"],
    show_tools_calls=True,
    markdown=True,
 )

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Gemini(id='gemini-2.5'
    '-flash'),#Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    #instructions=prompt,
    show_tool_calls=True,
    markdown=True,
 )

## Research Agent
research_Agent=Agent(
    #model=Gemini(id="gemini-2.0-flash-exp"),
    model=Gemini(id="gemini-2.5-flash"),
    tools=[ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"), type="keyword")],
    description="You are an advanced AI researcher writing a report on a topic.",
    instructions=[
        "For the provided topic, run 3 different searches.Read the results carefully and prepare a NYT worthy report.Focus on facts and make sure to provide references.",
    ],
    expected_output=dedent("""\
    An engaging, informative, and well-structured report in markdown format:

    ## Engaging Report Title

    ### Overview
    {give a brief introduction of the report and why the user should read this report}
    {make this section engaging and create a hook for the reader}

    ### Section 1
    {break the report into sections}
    {provide details/facts/processes in this section}

    ... more sections as necessary...

    ### Takeaways
    {provide key takeaways from the article}

    ### References
    - [Reference 1](link)
    - [Reference 2](link)
    - [Reference 3](link)

    - published on {date} in dd/mm/yyyy
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file="tmp/{message}.md",
)
agent = Agent(tools=[ArxivToolkit()], show_tool_calls=True)

def multi_ai_agent():
 from textwrap import dedent
#multi_ai_agent=Agent(
 return Agent(
    team=[web_search_agent,finance_agent],
    model=Gemini(id='gemini-2.5-flash'),
    instructions=["Always include sources and provide reference web links","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    add_datetime_to_instructions=True,
    save_response_to_file="venv\output\{user_query}.md",

 )
ma=multi_ai_agent()

#################################################################
def finance_agnt():
    user_query = st.text_area(
         "What insights are you seeking from Finance World?",
         placeholder="Ask anything about the Finance world. The AI agent will analyze and gather additional context if needed.",
         help="Provide specific questions or insights you want from Finance. Ex.Summarize analyst recommendation and share the latest news for NVDA"
     )
    if st.button("🔍 Analyze Report", key="analyze_Finance_button"):
         if not user_query:
             st.warning("Please enter a question or insight to analyze the Financial report.")
         else:
             try:
                 with st.spinner("Processing and gathering insights..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Finance Multi Agent System of Ramendra. You are an expert in Finance and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem drived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Search the web for content and context.
                         Respond to the following query using insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  ma.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Analysis Result")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
    else:
     st.info("Enter your desired Finance Question to begin analysis.")

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

##################################################################
@st.cache_resource
def initialize_agent():
    return Agent(
        name="Summarizer",
        instructions="Always do a web search for getting details",
        #model=Gemini(id="gemini-2.0-flash-exp"),
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
    )
## Initialize the agent
web_multimodal_Agent=initialize_agent()
##################################################################
def vdo_agnt():
# File uploader
 video_file = st.file_uploader(
     "Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI analysis"
 )

 if video_file:
     with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
         temp_video.write(video_file.read())
         video_path = temp_video.name

     st.video(video_path, format="video/mp4", start_time=0)

     user_query = st.text_area(
         "What insights are you seeking from the video?",
         placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
         help="Provide specific questions or insights you want from the video."
     )

     if st.button("🔍 Analyze Video", key="analyze_video_button"):
         if not user_query:
             st.warning("Please enter a question or insight to analyze the video.")
         else:
             try:
                 with st.spinner("Processing video and gathering insights..."):
                     # Upload and process video file
                     processed_video = upload_file(video_path)
                     while processed_video.state.name == "PROCESSING":
                         time.sleep(1)
                         processed_video = get_file(processed_video.name)
 
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Video Analizer Multi Agent System of Ramendra. You are an expert in gethering insights from a video and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem derived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Analyze the uploaded video for content and context.
                         Respond to the following query using video insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response = web_multimodal_Agent.run(analysis_prompt, videos=[processed_video])
 
                 # Display the result
                 st.subheader("Analysis Result")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             finally:
                 # Clean up temporary video file
                 Path(video_path).unlink(missing_ok=True)
 else:
     st.info("Upload a video file to begin analysis.")

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
########################################################################
def stock_agnt():
    #st.warning("Under development")
    try:
                 with st.spinner("Processing and gathering insights..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a crudoil Analyser Agent. You are an expert in crudoil analysis. You have to do analysis for 5:00 pm crudoil investment. At 5.00 pm current day in indian stock marcket cruidoil will be increasing or decreasing. Developer email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Search the web for content and context.
                         Respond to the following query using insights and supplementary web research:
                    
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  mac.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Analysis Result")
                 st.markdown(response.content)
    except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
             
########################################################################
def recipe_agent():
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    from phi.tools.exa import ExaTools
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

    knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://www.poshantracker.in/pdf/Awareness/MilletsRecipeBook2023_Low%20Res_V5.pdf",
        "https://www.cardiff.ac.uk/__data/assets/pdf_file/0003/123681/Recipe-Book.pdf",
    ],
    vector_db=PgVector(table_name="recipes", db_url=db_url),  # we are using PgVector here, you can also use other vector dbs
 )
    knowledge_base.load(recreate=False)
    return Agent(
    name="RecipeGenie",
    knowledge_base=knowledge_base,
    search_knowledge=True,
    tools=[ExaTools()],
    markdown=True,
    instructions=[
        "Search for recipes based on the ingredients and time available from the knowledge base.",
        "Include the exact calories, preparation time, cooking instructions, and highlight allergens for the recommended recipes.",
        "Always search exa for recipe links or tips related to the recipes apart from knowledge base.",
        "Provide a list of recipes that match the user's requirements and preferences.",
    ],
)
#ra=recipe_agent()

def recipe_system():
    user_query = st.text_area(
         "Give me detail about the recipe you want",
         placeholder="Ask any kind of recipe. The AI agent will analyze and gather additional context if needed.",
         help="Provide detailed information of the recipe you want. Ex.I have potatoes, tomatoes, onions, garlic, ginger, and chicken. Suggest me a quick recipe for dinner"
     )
    if st.button("🔍 Generate recipe", key="Generate_Recipe_button"):
         if not user_query:
             st.warning("Provide detailed information of the recipe you want")
         else:
             try:
                 with st.spinner("Processing and gathering insights..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Smart Recipe Maker Agent System of Ramendra. You are an expert in making Recipe and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem drived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Search the web for content and context.
                         Respond to the following query using insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  ra.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Your Recipe:")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
    else:
     st.info("Provide detailed information of the recipe you want.")

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
########################################################################
def Research_Agent():
    from textwrap import dedent
    from datetime import datetime

    from phi.agent import Agent
    from phi.tools.exa import ExaTools

    return Agent(
    #model=Gemini(id="gemini-2.0-flash-exp"),
    model=Gemini(id="gemini-2.5-flash"),
    tools=[ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"), type="keyword")],
    description="You are an advanced AI researcher writing a report on a topic.",
    instructions=[
        "For the provided topic, run 3 different searches.",
        "Read the results carefully and prepare a NYT worthy report.",
        "Focus on facts and make sure to provide references.",
    ],
    expected_output=dedent("""\
    An engaging, informative, and well-structured report in markdown format:

    ## Engaging Report Title

    ### Overview
    {give a brief introduction of the report and why the user should read this report}
    {make this section engaging and create a hook for the reader}

    ### Section 1
    {break the report into sections}
    {provide details/facts/processes in this section}

    ... more sections as necessary...

    ### Takeaways
    {provide key takeaways from the article}

    ### References
    - [Reference 1](link)
    - [Reference 2](link)
    - [Reference 3](link)

    - published on {date} in dd/mm/yyyy
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file="tmp/{message}.md",
)
ra=Research_Agent()

def Research_system():
    user_query = st.text_area(
         "Give a Topic For Your Research",
         placeholder="Give any kind of Research Topic. The AI agent will analyze and gather additional context if needed.",
         help="Provide Research Topic you want. Ex. Simulation theory"
     )
    if st.button("🔍 Generate Research Report", key="Generate_Research_button"):
         if not user_query:
             st.warning("Provide The Topic of Research you want")
         else:
             try:
                 with st.spinner("Processing and gathering insights..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Smart Research Agent System of Ramendra. You are an expert in doing Research and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem drived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Search the web for content and context.
                         Respond to the following query using insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  ra.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Research Report:")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
    else:
     st.info("Please Provide Your Research Topic.")

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
##########################################################
from phi.tools.calculator import Calculator

Calculator_agent = Agent(
    name="Calculator Agent",
    instructions=["Always do calculation according user"],
    model=Gemini(id='gemini-2.5-flash'),
    tools=[
        Calculator(
            add=True,
            subtract=True,
            multiply=True,
            divide=True,
            exponentiate=True,
            factorial=True,
            is_prime=True,
            square_root=True,
        )
    ],
    show_tool_calls=True,
    markdown=True,
) 
###########################################################
from phi.tools.email import EmailTools
receiver_email = "ramendra.rajput85@gmail.com"
sender_email = "ramendra.rajput85@gmail.com"
sender_name = "Ramendra rajput"
sender_passkey = "Ram1234$ingh"

Email_agent = Agent(
    name="Email Agent",
    instructions=["Always send email to given user"],
    model=Gemini(id='gemini-2.5-flash'),
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ],
    show_tool_calls=True,
    markdown=True,
)
###########################################################
def Multi_Agents_Chain():
    return Agent(
    team=[web_search_agent,finance_agent,research_Agent,Arxiv_paper_agent,Email_agent,Calculator_agent],
    model=Gemini(id='gemini-2.5-flash'),
    instructions=["Always include sources and provide reference web links","Use tables to display the data","For the provided topic, run 3 different searches.Read the results carefully and prepare a NYT worthy report.Focus on facts and make sure to provide references.","Always include sources and provide reference web links","Always send email to given user","Always do calculation according user"
    ],
    show_tool_calls=True,
    markdown=True,
    add_datetime_to_instructions=True,
    save_response_to_file="venv\output\{user_query}.md",

 )
mac=Multi_Agents_Chain()

def Multi_Agents_Chain_UI():
    Input_Type = st.radio("Select Input Type:", ("Text Only","Text And Image","Text And Video","Text And Audio"),index=None)
    if Input_Type ==  "Text Only":
       user_query = st.text_area(
         "Enter Your Query",
         placeholder="Give any kind of Query. Query will be transfered to Related Agent, Finance Query will be transfered to Finance Agent, Your web search query will be transfered to Web Agent. Related agents will responde you.",
         help="Provide Your Query to Research Agent, Finance Agent, Web Agent etc"
        )
       if st.button("🔍 Call Agent", key="Call_Agent_button"):
           if not user_query:
             st.warning("Provide Your Query For Agents")
           else:
             try:
                 with st.spinner("Calling Related Agent..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Smart Multi Agent System of Ramendra. You are an expert in doing this and continuouly being trained to perform by calling multi agents. You are trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem drived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         {user_query}
                         Transfer this user query to related Agent
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  mac.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Agent Report:")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
    elif Input_Type=="Text And Video":
        vdo_agnt()       
    elif Input_Type=="Text And Image":
         uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "pdf"])
         
         image = ""
         if uploaded_file is not None:
                #file_details={"fileName":uploaded_file.name,"FileType":uploaded_file.type,"FilePath":uploaded_file._file_urls}
                #st.write(file_details)
                image = Image.open(uploaded_file)
                image_data = input_image_setup(uploaded_file)
                image_path = Path(__file__).parent.joinpath(str(image))
                st.image(image, caption="Uploaded Image.", use_column_width=True)
                with open(os.path.join("tmp",uploaded_file.name),"wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.write("File saved")    
                user_query = st.text_area(
         "What insights are you seeking from the Image?",
         placeholder="Ask anything about the image content. The AI agent will analyze and gather additional context if needed.",
         help="Provide specific questions or insights you want from the image."
     )          
                #st.button("🔍 Analyze Image Using Agent", key="analyze_image_agent_button",on_click=ag())
                #st.button("🔍 Analyze Image Using LLM", key="analyze_image_llm_button",on_click=llm())
                if st.button("🔍 Analyze Image Using Agent", key="analyze_image_agent_button"):
                 if not user_query:
                  st.warning("Please enter a question or insight to analyze the image.")
                 else:
                  try:
                   with st.spinner("Processing image and gathering insights..."):
                      image_path = Path(__file__).parent.joinpath(os.path.join("tmp",uploaded_file.name))
                      # Prompt generation for analysis
                      analysis_prompt = (
                         f"""
                         You are a Image Analizer Multi Agent System of Ramendra. You are an expert in gethering insights from an image and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem derived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Analyze the uploaded Image for content and context.
                         Respond to the following query using Image insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                         )
                      #AI agent processing
                      response = web_multimodal_Agent.run(analysis_prompt,images=[image_path])
                      #Display the result
                      st.subheader("Agent Analysis Result")
                      st.markdown(response.content)
                  except Exception as error:
                   st.error(f"An error occurred during analysis: {error}")
                if st.button("🔍 Analyze Image Using LLM", key="analyze_image_llm_button"):
                 if not user_query:
                  st.warning("Please enter a question or insight to analyze the image.")
                 else:
                  try:
                   with st.spinner("Processing image and gathering insights..."):
                      #image_path = Path(__file__).parent.joinpath(os.path.join("tmp",uploaded_file.name))
                      # Prompt generation for analysis
                      analysis_prompt = (
                         f"""
                         You are a Image Analizer System of Ramendra. You are an expert in gethering insights from an image and continuouly being trained to perform task being LLM. You are a multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem derived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Analyze the uploaded Image for content and context.
                         Respond to the following query using Image insights and supplementary web research:
                         {user_query}
                         Provide a detailed, user-friendly, and actionable response.
                         """
                         )
                      #AI agent processing
                      response = get_gemini_response_i(analysis_prompt,image_data,user_query)
                      #Display the result
                      st.subheader("LLM Analysis Result")
                      st.markdown(response)

                  except Exception as error:
                   st.error(f"An error occurred during analysis: {error}")
         else:
                st.info("Upload an image file to begin analysis.")      
    elif Input_Type=="Text And Audio":
        uploaded_file = st.file_uploader("Upload a sound file", type=["mp3","wave"])
        #playsound(upload_file)
        st.warning("Under Development")       
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
###########################################################
from streamlit_chat import message  # Install using: pip install streamlit-chat
def AI_Chatbot():
    st.sidebar.title("AI Chatbot")
    st.sidebar.markdown("""
    ### Features:
    - Chat with AI
    - Memory of past conversations
    - Sleek UI like ChatGPT
    """)

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "memory" not in st.session_state:
        st.session_state["memory"] = {}

    st.subheader("My AI Chatbot💬")
    st.markdown("""
    Welcome to the AI Chatbot! Type your message below and start chatting.
    """)
    #st.caption("Developer: Ramendra Singh Rajput")

    for chat in st.session_state.messages:  
        message(chat["content"], is_user=chat["is_user"])

    user_input = st.chat_input("Type your message:", key="user_input")
    st.caption("Powered by Ramendra Singh Rajput")
    input_prompt = """
                       You are an expert in chatting like human. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                       you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark. 
                       """
    input_prompt1 = """
                        You are Ramendra Singh Rajput, an expert of everything. Your response must be related to user question only. Dont add axtra things. Reply quickly.
                        """

    if user_input:  
        st.session_state.messages.append({"content": user_input, "is_user": True})
        # Updating memory with relevant information
        if "my name is" in user_input.lower():
             name = user_input.lower().split("my name is")[-1].strip()
             st.session_state.memory["name"] = name
             response=f"Ok {name}, i'll remember your name"
             st.session_state.messages.append({"content": response, "is_user": False})
             st.rerun()
        elif "what is my name" in user_input.lower() and "name" in st.session_state.memory:
             response = f"Your name is {st.session_state.memory['name']}!"
             st.session_state.messages.append({"content": response, "is_user": False})
             #st.write(response)
             st.rerun()
        elif "what is my name" in user_input.lower() and "name" not in st.session_state.memory:
         response="Sorry! Please tell me your name"
         st.session_state.messages.append({"content": response, "is_user": False})
         st.rerun()
        else:
          with st.spinner(text='Thinking'):
           response = get_gemini_response_t(input_prompt1,user_input)
          # Simulating AI memory recall
           #previous_context = "\n".join([chat["content"] for chat in st.session_state.messages if not chat["is_user"]][-5:])  
           #response = f"Hey {st.session_state.memory['name']},\n{get_gemini_response_t(input_prompt,user_input)}\n"        
           st.session_state.messages.append({"content": response, "is_user": False})
           if response:
            st.success('Done')
            #st.write(response)
           st.rerun()
############################################################
import wikipediaapi
from transformers import pipeline
import requests

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

def get_search_suggestions(query, language):
    """
    Fetches search suggestions from Wikipedia based on the query.

    Args:
        query (str): The search query.
        language (str): The language code for the search.

    Returns:
        list: A list of search suggestions.
    """
    url = f"https://{language}.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "format": "json",
        "search": query,
        "limit": 5,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[1]

def Mypedia():
    topic = st.text_input("Search Topic:", "")
    if not topic:
        st.info("Enter a specific topic to search.", icon="ℹ️")

    # Search Suggestions
    if topic:
        with st.spinner("Fetching search suggestions..."):
            suggestions = get_search_suggestions(topic, "en")  # Default language code, "en"
        st.write("Search Suggestions:")
        if suggestions:
            selected_suggestion = st.selectbox("Select a suggestion", suggestions)
            st.write("Click on a suggestion to learn more.")
        else:
            st.write("No suggestions found. Try refining your search.")

    # Article Paragraph
    article_paragraph = st.empty()

    # Question Input
    #question = st.text_input("Question:", "")
    #if not question:
    #    st.info("Ask a question about the topic to receive informative answers.", icon="ℹ️")

    if topic:
        # Loads Wikipedia summary of the topic
        with st.spinner("Fetching Wikipedia summary..."):
            summary = load_wiki(topic, language="en")  # Default language code, "en"

        # Displays article summary in paragraph
        article_paragraph.markdown(summary)
        #st.write("Scroll down for more details or ask a specific question about the topic.")

    #    # -- Questions--
    #    if question:
    #        # Loads the question answering pipeline
    #        with st.spinner("Answering your question..."):
    #            qa_pipeline = load_qa_pipeline()

    #        # Answers query question using article summary
    #        result = answer_questions(qa_pipeline, question, summary)
    #        answer = result["answer"]

    #        # Displaying answer in real-time
    #        st.write(answer)

# Footer with link
    #link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
    #st.markdown(link, unsafe_allow_html=True)            
def Automation():
        st.warning("Under Maintainance")
############################################################
def main():
    try:
        load_dotenv()  # take environment variables from .env
        ####genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        openai.api_key=os.getenv("OPENAI_API_KEY")
        ##initialize our streamlit app
        #st.set_page_config(page_title="Indian AI Research Lab")
        #st.subheader("Advanced Artificial Intelligence Brain")
        st.title("Indian AI Research Lab")
        st.caption("Developer: Ramendra Singh Rajput")
        chat_type = st.selectbox(
            'Select Application type',
            ('1: Wikipedia Search','2: AI Chatbot','3: Text Classifier System', '4: Image Classifier System','5: Medical Diagnosis Agent System','6: Agentic AI System',"7: Multi Agentic AI System","8: Research Agent","9: Recipe Maker Agent",'10: Finance Agent',"11: Stock Investment Adviser Robot",'12: Video Summerizer Agent','13: Retrieval Augmented Generation System','14: Text to Image Generator System',"15: Image to Image Regenerator System",'16: Image to Image Overlaping System','17: Image to Video Generator System','18: Application Tracking System','19: AI Engineers Recruiter System','20: Health Expert System','21: Music Expert System','22: MPLRC Expert System','23: Philosophy Expert System','24: Kisan Mitra Chatbot','25: Fine-Tune Your Own Model','26: Developer Resume', '27: Automate Your Desktop'), index=None)
        if chat_type == None:
            welcome()
        elif chat_type == "1: Wikipedia Search":
            Mypedia()
        elif chat_type == '2: AI Chatbot':
            AI_Chatbot()
        elif chat_type == "3: Text Classifier System":
            text_proc()
        elif chat_type == "4: Image Classifier System":
            image_proc()
        elif chat_type == "5: Medical Diagnosis Agent System":
            MAS()
        elif chat_type == "6: Agentic AI System":
            ChatGPT()
        elif chat_type == "7: Multi Agentic AI System":
            Multi_Agents_Chain_UI()    
        elif chat_type == "10: Finance Agent":
            finance_agnt()
        elif chat_type == "11: Stock Investment Adviser Robot":
            stock_agnt()    
        elif chat_type == "12: Video Summerizer Agent":
            vdo_agnt()     
        elif chat_type == "8: Research Agent":
            Research_system()        
        elif chat_type == "9: Recipe Maker Agent":
            recipe_system()             
        elif chat_type == "14: Text to Image Generator System":
            Text_2_Image2()
        elif chat_type == "15: Image to Image Regenerator System":
            IT_2_Image()    
        elif chat_type == '16: Image to Image Overlaping System':
            Image_2_Image_Overlaping()
        elif chat_type == '17: Image to Video Generator System':
            Image_2_video()                
        elif chat_type == "24: Kisan Mitra Chatbot":
            Kisan_mitra_main()
        elif chat_type == "18: Application Tracking System":
            ATS()
        elif chat_type=="20: Health Expert System":
            Health_Expert()
        elif chat_type=="22: MPLRC Expert System":
            MP_LR()    
        elif chat_type=="23: Philosophy Expert System":
            Philosophy_Expert()
        elif chat_type=="26: Developer Resume":
            Dev_Resume()
        elif chat_type=="27: Automate Your Desktop":
            Automation()    
        elif  chat_type == "13: Retrieval Augmented Generation System":
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

  