import base64
from config.azure_config import client, CHAT_MODEL

def image_to_text(image_bytes):
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract text and describe this image"},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image}"
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content

def handle_request(image_bytes):
    if not image_bytes:
        return "Image is required", 400
    
    try:
        text = image_to_text(image_bytes)
        return text, 200
    except Exception as e:
        return "We couldn't extract text from the image. Please try again.", 500