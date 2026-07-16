import speech_recognition as sr
import streamlit as st
def recognize_speech(language_code):
    """
    Captures audio from the microphone and converts it into text using SpeechRecognition.

    Args:
        language_code (str): The language code for the speech recognition.

    Returns:
        str: The recognized text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        st.write("Could not understand audio.")
    except sr.RequestError as e:
        st.write(f"Error with the service; {e}")