import streamlit as st
from PIL import Image

from core.ai import vision
from core.prompts import MEDICAL_XRAY_ANALYSIS_SYSTEM_PROMPT

def MAS():
    prompt="Just give me detailed analysis of this x-ray image of human body and also provide key references at last"
    #prompt = st.text_input("Here you can ask anything about uploaded image")  
    uploaded_file = st.file_uploader("Upload a medical X-ray image", type=["jpg", "jpeg", "png", "pdf"])
    image = ""
    if uploaded_file is not None:
         image = Image.open(uploaded_file)
         st.image(image, caption="Uploaded Image.", use_column_width=True)
            
    if image:
        with st.spinner(text='Wait...I am analysing it'):
             response = vision(image=image, prompt=prompt, system_prompt=MEDICAL_XRAY_ANALYSIS_SYSTEM_PROMPT)
             if response:
               st.success('Done')
               st.write(response)