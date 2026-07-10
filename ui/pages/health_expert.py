import streamlit as st
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
            from core.ai import chat

            response = chat(prompt=prompt,system_prompt=input_prompt,)
        if response:
            st.success('Done')
            st.write(response)
            af=t_2_s(response)
