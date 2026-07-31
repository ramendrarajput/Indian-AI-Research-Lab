"""
Project BRAHMA
Developer : Ramendra Singh Rajput
Module : Speech Utilities
"""
def t_2_s(response):

 t=response
 # Select the language for the text to be spoken in
 language = 'en'
 # Create an instance of the gTTS class
 tts = gtts.gTTS(text=t, lang=language, slow=False)
 # Save the audio file
 audio_file = 'response.mp3'
 tts.save(audio_file)
 return audio_file

