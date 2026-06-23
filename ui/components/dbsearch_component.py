import streamlit as st
from services import dbsearch_service

def render():
    
    # Display chat
    def display_chat():
        for role, msg in st.session_state.dbsearch_history:
            st.chat_message(role).write(msg)

    if "dbsearch_history" not in st.session_state:
        st.session_state.dbsearch_history = []
        
    prompt = st.chat_input("Ask a question...")
    
    if "dbsearch_history" in st.session_state:
        display_chat()
        if prompt:
            st.session_state.dbsearch_history.append(("user", prompt))
            st.chat_message("user").write(prompt)
            # ✅ Placeholder for spinner (important)
            spinner_placeholder = st.empty()

            # Generate answer
            # ✅ Show spinner ABOVE input using placeholder
            with spinner_placeholder:
                with st.spinner("Thinking..."):
                    answer = dbsearch_service.handle_request(prompt)
            
            # Clear spinner (optional)
            spinner_placeholder.empty()

            st.session_state.dbsearch_history.append(("assistant", answer[0]))

            # Display response immediately
            st.chat_message("assistant").write(answer[0])
