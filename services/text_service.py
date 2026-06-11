
from config.azure_config import client, CHAT_MODEL

def generate_text(prompt):
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def context_search(query, context):
    prompt = f"""
    Answer only using the context.

    Context:
    {context}

    Question:
    {query}
    """

    res = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": "You are an enterprise assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return res.choices[0].message.content

def handle_request(prompt):
    if not prompt:
        return "Prompt is required", 400
    
    try:
        text_response = generate_text(prompt)
        return text_response, 200
    except Exception as e:
        return str(e), 500
