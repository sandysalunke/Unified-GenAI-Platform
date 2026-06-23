
from config.azure_config import client, CHAT_MODEL
from helpers import SQLite

def generate_query(prompt):
    prompt = f"""
    - You are a SQL expert.
    - Generate SQL query for the user prompt.
    
    STRICT RULES:
    - Limit results where needed.
    - Generate ONLY SELECT queries. Never modify data.
    - Only return valid SQL query.
    - No explanations.
    - No markdown (no ``` blocks).

    Table: sales
    Columns:
    - id (int)
    - customer_id (int)
    - revenue (float)
    - cost (float)
    - date (date)

    User prompt: {prompt}
    """
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": "You are an enterprise assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def search_context(prompt, result):
    prompt = f"""
    User question: {prompt}
    SQL result: {result}

    - Explain the result in business terms
    - Add if possible the data in summary table
    - Do not use technical language like SQL, results, rows etc
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": "You are an enterprise assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def handle_request(prompt):
    if not prompt:
        return "Prompt is required", 400
    
    try:
        query = generate_query(prompt)
        dbresult = SQLite.readData(query)
        result = search_context(prompt, dbresult)

        return result, 200
    except Exception as e:
        return "Sorry, I couldn't process that. Please try rephrasing.", 500
