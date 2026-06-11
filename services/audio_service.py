
from config.azure_config import client, WHISPER_MODEL

def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            file=f,
            model=WHISPER_MODEL
        )
    return transcript.text

def handle_request(input_data):
    file_path = input_data.get("file_path")
    if not file_path:
        return "File path is required", 400
    
    try:
        transcript = transcribe_audio(file_path)
        return transcript, 200
    except Exception as e:
        return str(e), 500