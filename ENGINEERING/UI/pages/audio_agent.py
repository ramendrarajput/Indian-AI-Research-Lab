import streamlit as st
def audio_agent_ui():
    uploaded_file = st.file_uploader("Upload a sound file", type=["mp3","wave"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        st.warning("Under Development")
    else:
                st.info("Upload a sound file to begin analysis.")    