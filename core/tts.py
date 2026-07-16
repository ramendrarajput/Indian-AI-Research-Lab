import os
import elevenlabs
from elevenlabs import ElevenLabs
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY")
    )

    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

    return output_filepath

def text_to_speech(text, language_code):
    """
    Converts text to speech in the specified language using gTTS.

    Args:
        text (str): The text to be converted to speech.
        language_code (str): The language code for the speech synthesis.

    Returns:
        AudioSegment: The audio segment containing the speech.
    """
    tts = gTTS(text, lang=language_code)
    mp3_data = BytesIO()
    tts.write_to_fp(mp3_data)
    mp3_data.seek(0)
    audio = AudioSegment.from_file(mp3_data, format="mp3")
    return audio