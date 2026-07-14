import streamlit as st
import tempfile
import time
from pathlib import Path
from agents.base_agent import web_multimodal_Agent
from google.generativeai import upload_file, get_file

def video_agent_ui():
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
