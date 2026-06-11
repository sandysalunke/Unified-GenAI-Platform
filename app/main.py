import streamlit as st
from router import route

st.set_page_config(page_title="GenAI Copilot", layout="wide")

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("🧠 GenAI Copilot")

feature = st.sidebar.radio(
    "Select Feature",
    ["Text AI", "Image AI", "Meeting Assistant", "Excel Analytics", "Audio Transcription"]
)

# Map UI → router key
feature_map = {
    "Text AI": "text",
    "Image AI": "image",
    "Meeting Assistant": "meeting",
    "Excel Analytics": "excel",
    "Audio Transcription": "audio"
}

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
# IMAGE AI UI
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
# elif selected_feature == "excel":

#     file = st.file_uploader("Upload Excel", type=["xlsx"])

#     if file:
#         st.write(route(selected_feature, file))

# # ---------------------------
# # AUDIO TRANSCRIPTION UI
# # ---------------------------
# elif selected_feature == "audio":

#     file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

#     if file:
#         st.write(route(selected_feature, file))
