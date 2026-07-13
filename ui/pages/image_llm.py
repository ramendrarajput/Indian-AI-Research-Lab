import streamlit as st
from PIL import Image
from core.ai import vision
from core.image import input_image_setup
from core.prompts import IMAGE_ANALYSIS_SYSTEM_PROMPT

#def image_proc():
def image_analysis_ui():
    prompt = st.text_input("Here you can ask anything about uploaded image")
    with st.sidebar:
         #prompt = st.text_input("Ask anything about the image")  
         uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
         image = ""
         if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)
            
    input_prompt1 = """
                     You are an expert in understanding invoices.
                     You will receive input images as invoices &
                     you will have to answer questions based on the input image
                    """
    input_prompt2 = """
                     You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                     You are an expert in understanding images patterns.
                     You will receive input images &
                     you will have to answer questions based on the input image but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.
                    """
    if prompt:
        with st.spinner(text='Thinking'):
             response = vision(image=image,prompt=f"{IMAGE_ANALYSIS_SYSTEM_PROMPT}\n\n{prompt}",)
             if response:
               st.success('Done')
               st.write(response)




