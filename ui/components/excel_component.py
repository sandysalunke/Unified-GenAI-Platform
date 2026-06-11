import streamlit as st
import pandas as pd
from helpers.utils import load_file
from services import data_service, text_service

def render():
    
    # Display chat
    def display_chat():
        if st.session_state.df is not None:
            st.write("### Data Preview", st.session_state.df.head())

        for role, msg in st.session_state.analytics_history:
            if role == "user":
                st.chat_message("user").write(msg)
            else:
                run_code(msg)

    # Function to run code from history and display results
    def run_code(code):
        try:
            result = data_service.run_code(code, st.session_state.df)

            st.write("### Result")
            if result is not None:
                st.chat_message("assistant").write(result)

        except Exception as e:
            st.error(f"Error executing code: {e}")

    if "analytics_history" not in st.session_state:
        st.session_state.analytics_history = []

    if "df" not in st.session_state:
        st.session_state.df = None
    
    # File uploader
    file = st.file_uploader("Upload Excel or CSV", type=["xlsx", "csv"])
    if file and st.session_state.df is None:
        df = load_file(file)
        st.session_state.df = df

    # User prompt
    prompt = st.chat_input("Ask a question about your data...")
    
    if "analytics_history" in st.session_state:
        display_chat()
        if prompt:
            st.session_state.analytics_history.append(("user", prompt))
            st.chat_message("user").write(prompt)
            # ✅ Placeholder for spinner (important)
            spinner_placeholder = st.empty()

            if prompt.lower() == "exit":
                st.session_state.analytics_history = []
                st.success("Session reset ✅")
                st.stop()
        
            # Generate answer
            # ✅ Show spinner ABOVE input using placeholder
            with spinner_placeholder:
                with st.spinner("Thinking..."):
                    code = data_service.generate_code(st.session_state.df, prompt)
                    
            # Clear spinner (optional)
            spinner_placeholder.empty()

            st.session_state.analytics_history.append(("assistant", code))

            # Reload app
            st.rerun()
    