
from config.azure_config import client, CHAT_MODEL
from helpers import SQLite

def generate_query(prompt):
    prompt = f"""
    - Generate SQL query for the user prompt
    - User prompt: {prompt}
    - Limit the records to Max 10
    - Generate ONLY SELECT queries. Never modify data.
    - Only return valid SQL query
    - No explanations
    - No markdown (no ``` blocks)

    Table: sales
    Columns:
    - id (int)
    - customer_id (int)
    - revenue (float)
    - cost (float)
    - date (date)
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
        return "Sorry, we couldn't generate the text. Please try again.", 500
