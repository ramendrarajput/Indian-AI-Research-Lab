import google.generativeai as genai

from config.models import GEMINI_TEXT_MODEL
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def get_model():
    """
    Return the configured Gemini text model.
    """
    return genai.GenerativeModel(
        GEMINI_TEXT_MODEL
    )

def get_vision_model():
    return genai.GenerativeModel(
        GEMINI_TEXT_MODEL
    )

def get_gemini_response(prompt):
    model = GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    return response.text
