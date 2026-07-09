from elevenlabs import ElevenLabs
import streamlit as st

from core.ai import chat
from core.prompts import TEXT_CLASSIFIER_SYSTEM_PROMPT
from elevenlabs import play, voices, stream, client

def text_proc():
    prompt = st.text_input("You can ask anything")
    if prompt:
        with st.spinner(text='Thinking'):
             response = chat(prompt=prompt,system_prompt=TEXT_CLASSIFIER_SYSTEM_PROMPT,)
        if response:
            st.success('Done')
            st.write(response)
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