#import google.generativeai as genai

#from config.settings import GEMINI_API_KEY
#from config.models import GEMINI_TEXT_MODEL

#genai.configure(api_key=GEMINI_API_KEY)


#def get_model():
#    return genai.GenerativeModel(GEMINI_TEXT_MODEL)
########################################################

import google.generativeai as genai

from config.models import GEMINI_TEXT_MODEL
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def get_text_model():

    return genai.GenerativeModel(
        GEMINI_TEXT_MODEL
    )