#import google.generativeai as genai
#from config.settings import GEMINI_API_KEY
#from config.models import GEMINI_TEXT_MODEL

#genai.configure(api_key=GEMINI_API_KEY)

#def get_text_model():

#    return genai.GenerativeModel(
#        GEMINI_TEXT_MODEL
#    )

####################################################
"""
Legacy compatibility layer.

Do not add new code here.
This module exists only to support legacy imports during migration.
"""

from core.providers.gemini import get_model


def get_text_model():
    return get_model()