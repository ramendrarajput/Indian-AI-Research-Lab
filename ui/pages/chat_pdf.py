"""
Project BRAHMA
Developer : Ramendra Singh Rajput
Module : Chat PDF
"""
import streamlit as st

from core.rag import (
    get_pdf_text,
    get_text_chunks,
    get_vector_store,
    user_input,
)

def ChatPdf():
    
    def get_pdf_text(pdf_docs):
        text=""
        for pdf in pdf_docs:
            pdf_reader=PdfReader(pdf)
            for page in pdf_reader.pages:
                text+=page.extract_text()
        return  text
    
    def get_text_chunks(text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
        return chunks
    
    def get_vector_store(text_chunks):
     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
     vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
     vector_store.save_local("faiss_index")

    ############################################################################
    
    def get_conversational_chain():

     prompt_template = """
     You are an Expert in pdf file reading RAG system. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput . Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
     provided context just say, "answer is not available in the context", don't provide the wrong answer, last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n\n\n
     Context:\n {context}?\n
     Question:\n{question}\n

     Answer:
     """

     model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

     prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

     return chain
    
    def user_input(user_question):
     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
     new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
     docs = new_db.similarity_search(user_question)

     chain = get_conversational_chain() 

     response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

     print(response)
     st.write(response["output_text"])

    user_question=st.text_input("Ask a question from pdf files.")
    
    if user_question:
        user_input(user_question)
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs=st.file_uploader("Upload your pdf files and click on the submit & process")
        if st.button("Submit & Process") :#and user_input is not None:
            with st.spinner("Processing..."):
                st.balloons()
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")
