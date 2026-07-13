import os
from pathlib import Path

import streamlit as st
from PIL import Image

from agents.base_agent import create_web_multimodal_agent
#from core.vision import vision
from core.ai import vision
from core.image import input_image_setup
from prompts.system.image_analysis import IMAGE_ANALYSIS_SYSTEM_PROMPT

web_multimodal_Agent = create_web_multimodal_agent()

def image_agent_ui():
    uploaded_file = st.file_uploader(
        "Upload an image file",
        type=["jpg", "jpeg", "png", "pdf"],
    )

    if uploaded_file is None:
        st.info("Upload an image file to begin analysis.")
        return

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

    image_data = input_image_setup(uploaded_file)

    os.makedirs("tmp", exist_ok=True)

    image_path = os.path.join("tmp", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    user_query = st.text_area(
        "What insights are you seeking from the Image?",
        placeholder="Ask anything about the image content.",
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Analyze Image Using Agent"):

            if not user_query:
                st.warning("Please enter your question.")
            else:
                _run_agent(image_path, user_query)

    with col2:
        if st.button("🔍 Analyze Image Using LLM"):

            if not user_query:
                st.warning("Please enter your question.")
            else:
                _run_llm(image_data, user_query)


def _run_agent(image_path, user_query):

    try:

        with st.spinner("Processing image..."):

            prompt = f"""
Analyze the uploaded image.

Answer the following user query:

{user_query}

Search the web if required.

Provide a detailed response.
"""

            response = web_multimodal_Agent.run(
                prompt,
                images=[Path(image_path)],
            )

        st.subheader("Agent Analysis Result")

        st.markdown(response.content)

    except Exception as e:

        st.error(e)


def _run_llm(image_data, user_query):

    try:

        with st.spinner("Processing image..."):

            response = vision(
                image=image_data[0],
                prompt=user_query,
                system_prompt=IMAGE_ANALYSIS_SYSTEM_PROMPT,
            )

        st.subheader("LLM Analysis Result")

        st.markdown(response)

    except Exception as e:

        st.error(e)    