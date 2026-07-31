import streamlit as st
from ENGINEERING.AGENTS.research_agent import ra
import traceback
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
                 st.error(error)
                 st.code(traceback.format_exc())
                 #st.error(f"An error occurred during analysis: {error}")
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
