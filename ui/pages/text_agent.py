import streamlit as st
from agents.multi_agents_chain import mac

def text_agent_ui():
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