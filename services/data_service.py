import pandas as pd
import matplotlib.pyplot as plt
from openai import AzureOpenAI
from config.azure_config import client, CHAT_MODEL

def generate_code(df, user_query):
    prompt = f"""
    You are a Python data analyst.

    Data columns:
    {list(df.columns)}

    User question:
    {user_query}

    STRICT RULES:
    - Only return valid Python code
    - No explanations
    - No markdown (no ``` blocks)
    - Use dataframe name: df
    - Store final result in variable 'result'
    - If visualization is useful, include matplotlib code and use streamlit to display it (st.pyplot(fig))
    - Use plot size (10,6) for matplotlib charts
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_code = response.choices[0].message.content
    return clean_code(raw_code)


def run_code(code, df):
    if "import os" in code or "open(" in code:
        raise Exception("Unsafe code detected")

    safe_globals = {"pd": __import__("pandas")}
    local_vars = {"df": df}

    exec(code, safe_globals, local_vars)

    return local_vars.get("result", None)


def plot_if_possible(result):
    if isinstance(result, pd.DataFrame):
        try:
            result.plot()
            plt.title("Generated Chart")
            st.pyplot(plt)
        except:
            pass

def clean_code(code):
    # Remove markdown formatting
    code = code.replace("```python", "")
    code = code.replace("```", "")
    
    # Remove leading/trailing spaces
    code = code.strip()

    return code