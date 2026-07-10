import streamlit as st
from core.pdf_utils import create_pdf, get_pdf_download_link
def Dev_Resume():
    prompt = "Show me your Developers Resume."
    input_prompt = """
                   You are a Resume expert. Expert in Resume creating.Here you have to create your developers resume profile his name is Ramendra Singh Rajput. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari since 2015 and have gained greate experience to work with land records, citizence problem solving, land measorment, managing the data of citizence, providing them end to end goverment services in variouse manners. Have gained experience of different different fields work provided by goverment in line order duties. Utilizing this knowledge to develop a powerfull echo system for goverment to help people and solve theire problem in a smart way. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also working on Health Expert System, Music Expert System projects.He is having google developer profile.His education and qualification is Bachelore of computer application from M.I.M.T. college Narsimhapur(2007-2010),  master of computer application from ShriRam Institue Of Technology and Science(2010 to 2012).Active learner for Machine learning, Deep learning and Generative AI.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                   you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
                   """

    if prompt:
        with st.spinner(text='Generating Resume'):
            from core.ai import chat
            response = chat(prompt=prompt,system_prompt=input_prompt,)
        if response:
            st.success('Done')
            st.write(response)
            #af=t_2_s(response)
            if st.button("Generate PDF"):
              with st.spinner(text='Generating PDF'):
               pdf_path = create_pdf(response)
               st.success("PDF generated successfully! Click below to download.")
               st.markdown(get_pdf_download_link(pdf_path), unsafe_allow_html=True)
