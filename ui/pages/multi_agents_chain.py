import os
import streamlit as st
#from app import mac
from agents.multi_agents_chain import mac
from ui.pages.video_agent import vdo_agnt
#from ui.pages.image_agent import image_agent
from ui.pages.image_analysis import image_analysis_ui
from PIL import Image
from core.image import input_image_setup
from pathlib import Path
from core.ai import vision
from prompts.system.image_analysis import IMAGE_ANALYSIS_SYSTEM_PROMPT
from core.prompts import IMAGE_ANALYSIS_SYSTEM_PROMPT
from agents.base_agent import create_web_multimodal_agent

web_multimodal_agent = create_web_multimodal_agent()
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
         #image_analysis_ui()
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
                      response = web_multimodal_agent.run(analysis_prompt,images=[image_path])
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