from langchain_google_genai import ChatGoogleGenerativeAI

from config import DEFAULT_MODEL
from config import TEMPERATURE
from config import GOOGLE_API_KEY

def get_llm():

    llm = ChatGoogleGenerativeAI(
        model=DEFAULT_MODEL,
        temperature=TEMPERATURE,
        google_api_key=GOOGLE_API_KEY
    )

    return llm