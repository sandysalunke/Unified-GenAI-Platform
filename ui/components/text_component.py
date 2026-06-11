import streamlit as st
from services import text_service


def render():
    
    # Display chat
    def display_chat():
        for role, msg in st.session_state.chat_history:
            st.chat_message(role).write(msg)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    prompt = st.chat_input("Ask a question (type 'exit' to reset)...")
    
    if "chat_history" in st.session_state:
        display_chat()
        if prompt:
            st.session_state.chat_history.append(("user", prompt))
            st.chat_message("user").write(prompt)
            # ✅ Placeholder for spinner (important)
            spinner_placeholder = st.empty()

            if prompt.lower() == "exit":
                st.session_state.chat_history = []
                st.success("Session reset ✅")
                st.stop()
        
            # Generate answer
            # ✅ Show spinner ABOVE input using placeholder
            with spinner_placeholder:
                with st.spinner("Thinking..."):
                    answer = text_service.handle_request(prompt)
            
            # Clear spinner (optional)
            spinner_placeholder.empty()

            st.session_state.chat_history.append(("assistant", answer[0]))

            # Display response immediately
            st.chat_message("assistant").write(answer[0])
    