"""
Project BRAHMA
Developer : Ramendra Singh Rajput
Module : Speech To Text
"""
import speech_recognition as sr

# Function to convert speech to text
def speech_to_text():
 #import speech_recognition as sr
 # Create a Recognizer object
 r = sr.Recognizer()

 # Create a Microphone object to capture audio
 mic = sr.Microphone()

 # Set the threshold for the recognizer
 r.energy_threshold = 400

 # Start recording audio from the microphone
 with mic as source:
    print("Speak now!")
    audio = r.record(source, duration=5)

 # Recognize the audio and print the transcription
 try:
    # Use the recognizer to recognize the audio
     text = r.recognize_google(audio)
     print(text)
 except sr.RequestError:
     print("Could not request results from Google Speech Recognition service")
 except sr.UnknownValueError:
     print("Unknown error occurred")
