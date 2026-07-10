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

import streamlit as st

from core.ai import chat

st.set_page_config(
    page_title="Project BRAHMA",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded",
)
############################welcome#########################################
from ui.pages.welcome import welcome
#####################################################################
from ui.pages.image_analysis import image_proc
##############################################################3
from ui.pages.speech_to_text import speech_to_text
################################################################
from ui.pages.chat_gpt import ChatGPT
######################################
from ui.pages.text_processor import text_proc
######################################
from ui.pages.mp_lr import MP_LR
######################Health Expert System########################
from ui.pages.health_expert import Health_Expert
##################################################################

##################philosophy Expert System########################
from ui.pages.philosophy_expert import Philosophy_Expert
##################################################################             
from core.ai import vision
from core.prompts import IMAGE_ANALYSIS_SYSTEM_PROMPT             
from core.prompts import MEDICAL_XRAY_ANALYSIS_SYSTEM_PROMPT
#####################################################
from ui.pages.medical_xray import MAS
#####################################################

import elevenlabs
from elevenlabs.client import ElevenLabs

import subprocess
import platform

from core.tts import text_to_speech_with_elevenlabs
##########################################################
from core.rag import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain,user_input
########################################################## 
from ui.pages.chat_pdf import ChatPdf
############################################################################

########################Resume##################################
from ui.pages.dev_resume import Dev_Resume

################################################################


############## kisan mitra ########################
from ui.pages.kisan_mitra import Kisan_mitra_main
###################################################

############ATS########################
from ui.pages.application_tracking_system import ATS
#######################################

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

from ui.pages.image_generation import (
    IT_2_Image,
    IT_2_Image2,
    Text_2_Image2,
    Image_2_Image_Overlaping,
    Image_2_Image_Overlaping1,
)

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
                      response = vision(image=image_data[0],prompt=user_query,system_prompt=IMAGE_ANALYSIS_SYSTEM_PROMPT,)
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
from ui.pages.ai_chat import AI_Chatbot
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

###############################################
from ui.pages.wikipedia import Mypedia
##############################################
def Automation():
        st.warning("Under Maintainance")
############################################################
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
            image_proc()
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
            vdo_agnt()     
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

  