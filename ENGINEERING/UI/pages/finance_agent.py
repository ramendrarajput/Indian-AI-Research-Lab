from ENGINEERING.AGENTS.multi_agents_chain import mac
#from agents.finance_agent import ma
import streamlit as st
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
