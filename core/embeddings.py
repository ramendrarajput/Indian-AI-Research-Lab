from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import GOOGLE_API_KEY

def get_embeddings():

    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )