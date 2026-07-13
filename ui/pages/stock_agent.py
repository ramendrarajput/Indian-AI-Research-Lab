from ui.pages.multi_agents_chain import mac
import streamlit as st
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
             
