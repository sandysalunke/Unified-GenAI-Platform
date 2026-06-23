import streamlit as st
from router import route

st.set_page_config(page_title="GenAI Copilot", layout="wide")

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("🧠 GenAI Copilot")

# Map UI → router key
feature_map = {
    "Text AI": "text",
    "Image Generation": "image",
    "Meeting Assistant": "meeting",
    "Excel Analytics": "excel",
    "Image to Text": "image2text",
    "Database Search": "DBSearch"
}

feature = st.sidebar.radio(
    "Select Feature",
    [f for f in feature_map.keys()]
)

selected_feature = feature_map[feature]

# ---------------------------
# Main UI
# ---------------------------
st.title(f"🚀 {feature}")

# ---------------------------
# TEXT AI UI
# ---------------------------
if selected_feature == "text":
    route(selected_feature)
    
# ---------------------------
# IMAGE GENERATION UI
# ---------------------------
elif selected_feature == "image":
    route(selected_feature)

# ---------------------------
# MEETING ASSISTANT UI
# ---------------------------
elif selected_feature == "meeting":
    route(selected_feature)

# # ---------------------------
# # EXCEL ANALYTICS UI
# # ---------------------------
elif selected_feature == "excel":
    route(selected_feature)

# # ---------------------------
# # IMAGE TO TEXT UI
# # ---------------------------
elif selected_feature == "image2text":
    route(selected_feature)

# # ---------------------------
# # DATABASE SEARCH
# # ---------------------------
elif selected_feature == "DBSearch":
    route(selected_feature)
 