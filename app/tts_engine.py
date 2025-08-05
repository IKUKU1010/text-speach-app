import os
from gtts import gTTS
import uuid

def text_to_speech(text: str) -> str:
    output_dir = "audio"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.mp3"
    file_path = os.path.join(output_dir, filename)

    tts = gTTS(text)
    tts.save(file_path)

    return file_path  # This path is relative to the project root