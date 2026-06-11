import pandas as pd

def analyze_excel(file):
    df = pd.read_excel(file)
    return df.describe().to_string()

def handle_request(input_data):
    file = input_data.get("file")
    if not file:
        return "Excel file is required", 400
    
    try:
        analysis_result = analyze_excel(file)
        return analysis_result, 200
    except Exception as e:
        return str(e), 500