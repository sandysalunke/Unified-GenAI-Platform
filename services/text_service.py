
from config.azure_config import client, CHAT_MODEL

def generate_text(prompt):
    messages=[{"role": "system", "content": "You are an enterprise assistant."}]
    for c in prompt:
        if len(messages) >= 10:  # Limit to last 10 messages
            messages.pop(0)
        messages.append({"role": c[0], "content": c[1]})
        
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages
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
        return "Sorry, we couldn't generate the text. Please try again.", 500
