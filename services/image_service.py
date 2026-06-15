import base64
from config.azure_config import client, IMAGE_MODEL

def generate_image(prompt):
    result = client.images.generate(
        model=IMAGE_MODEL,
        prompt=prompt,
        size="1024x1024"
    )

    img_base64 = result.data[0].b64_json
    return base64.b64decode(img_base64)


def generate_multiple_images(prompt, n=4):
    return [generate_image(prompt) for _ in range(n)]

def handle_request(prompt):
    if not prompt:
        return "Prompt is required", 400
    
    try:
        image_data = generate_image(prompt)
        return image_data, 200
    except Exception as e:
        return "We couldn't generate the image. Please try again.", 500