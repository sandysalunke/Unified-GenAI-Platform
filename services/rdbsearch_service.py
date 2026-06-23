from langchain_openai import AzureChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from config.azure_config import AZURE_API_KEY, API_ENDPOINT, API_VERSION, CHAT_MODEL

def ask_langChainLLM(prompt):
    # LLM
    llm = AzureChatOpenAI(
        azure_deployment=CHAT_MODEL,
        api_version=API_VERSION,
        azure_endpoint=API_ENDPOINT,
        api_key=AZURE_API_KEY,
        temperature=0
    )

    # SQLite DB connection
    db = SQLDatabase.from_uri(
        "sqlite:///sales_multi.db",
        include_tables=["customers", "orders", "products"]
    )

    # Set Rules
    custom_suffix = """
    You are a SQL expert.

    Tables:
    - customers(customer_id, name, city)
    - products(product_id, product_name, category, price)
    - orders(order_id, customer_id, product_id, quantity, total_amount, order_date)

    Rules:
    - Use JOIN when needed
    - Only SELECT queries
    - Use correct column names
    """

    # SQL Agent
    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=True,
        suffix=custom_suffix
    )

    response = agent.run(prompt)

    return response

def handle_request(prompt):
    if not prompt:
        return "Prompt is required", 400
    
    try:
        result = ask_langChainLLM(prompt)
        return result, 200
    except Exception as e:
        return "Sorry, I couldn't process that. Please try rephrasing.", 500
