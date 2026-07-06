################################################################################
#from langchain_google_genai import ChatGoogleGenerativeAI
#from config import DEFAULT_MODEL
#from config import TEMPERATURE
#from config import GOOGLE_API_KEY

#def get_llm():

#    llm = ChatGoogleGenerativeAI(
#        model=DEFAULT_MODEL,
#        temperature=TEMPERATURE,
#        google_api_key=GOOGLE_API_KEY
#    )

#   return llm
################################################################################

from core.providers.gemini import get_model

PROVIDER = "gemini"


def get_llm():

    if PROVIDER == "gemini":
        return get_model()

    raise ValueError(f"Unknown provider: {PROVIDER}")