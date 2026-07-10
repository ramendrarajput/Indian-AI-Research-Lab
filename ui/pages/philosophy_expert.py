
import streamlit as st

def Philosophy_Expert():
    from prompts.agents.philosophy import PHILOSOPHY_PROMPT
    prompt = st.text_input("Here You can ask anything related to Philosophy")
    input_prompt = PHILOSOPHY_PROMPT
    if prompt:
        with st.spinner(text='Thinking'):
            from core.ai import chat
            response = chat(prompt=prompt,system_prompt=input_prompt,)
        if response:
            st.success('Done')
            st.write(response)
            af=t_2_s(response)
