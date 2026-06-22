import streamlit as st
from services import image2text_service

def render():

    # Display chat
    def display_chat():
        for role, msg in st.session_state.image2text_history:
            with st.chat_message(role):
                if role == "user" and isinstance(msg, bytes):
                    st.image(msg, width=400)
                else:
                    st.write("Here is the extracted text:")
                    st.write(msg)

    if "image2text_history" not in st.session_state:
        st.session_state.image2text_history = []

    
    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = 0
    
    display_chat()
    uploaded_file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"], key=f"file_uploader_{st.session_state.uploader_key}")
    
    if uploaded_file:
        image_bytes = uploaded_file.read()
        st.session_state.image2text_history.append(("user", image_bytes))

        # Placeholder for spinner (important)
        spinner_placeholder = st.empty()

        # Show spinner ABOVE input using placeholder
        with spinner_placeholder:
            with st.spinner("Extracting text..."):
                text = image2text_service.handle_request(image_bytes)

        # Clear spinner (optional)
        spinner_placeholder.empty()

        #Add Text to chat history
        st.session_state.image2text_history.append(("assistant", text[0]))

        # ✅ Reset uploader by changing key
        st.session_state.uploader_key += 1

        st.rerun()
    