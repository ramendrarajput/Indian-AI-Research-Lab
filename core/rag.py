import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    #embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

#def get_conversational_chain():

#    prompt_template = """
#    You are an Expert in pdf file reading RAG system. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput . Answer the question as detailed as possible from the provided context. If the question is in hindi then reply in hindi, If the question is in English then reply in english , make sure to provide all the details, if the answer is not in
#    provided context, give answer by yourself but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark.\n\n
#    Context:\n {context}?\n
#    Question: \n{question}\n
#    Answer:
#    """
#    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
#                             temperature=0.3)

#    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
#    chain = create_stuff_documents_chain( llm=model,prompt=prompt)
#    return chain

def get_conversational_chain():

    prompt_template = """
You are an expert PDF RAG assistant.

Answer the question only from the given context.

If the answer is not available in the context, clearly say:
"I could not find this information in the uploaded PDF."

If the user's question is in Hindi, answer in Hindi.
If it is in English, answer in English.

Context:
{context}

Question:
{input}

Answer:
"""

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "input"],
    )

    document_chain = create_stuff_documents_chain(
        llm=model,
        prompt=prompt,
    )

    return document_chain

def user_input(user_question):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )

    document_chain = get_conversational_chain()

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain,
    )

    response = retrieval_chain.invoke(
        {
            "input": user_question
        }
    )

    #st.write(response["answer"])
    st.write(response.get("answer", response))