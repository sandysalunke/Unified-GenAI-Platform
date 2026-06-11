from config.azure_config import client, WHISPER_MODEL, CHAT_MODEL


def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model=WHISPER_MODEL   # or your Azure deployment name
        )
    return transcript.text

def process_meeting(transcript):
    response = client.chat.completions.create(
        model=CHAT_MODEL,  # your deployment name
        messages=[
            {
                "role": "system",
                "content": "You are an AI meeting assistant."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this meeting transcript:

                Provide:
                1. Summary
                2. Key Points
                3. Action Items (with owner if possible)
                4. List of attendees (if mentioned)

                Transcript:
                {transcript}
                """
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content