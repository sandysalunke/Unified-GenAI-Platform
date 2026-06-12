import streamlit as st
from services import image_service

def render():

    # Display chat
    def display_chat():
        for role, msg in st.session_state.image_history:
            with st.chat_message(role):
                if role == "assistant" and isinstance(msg, bytes):
                    st.write("Here is your generated image:")
                    st.image(msg, width=400)
                else:
                    st.write(msg)

    if "image_history" not in st.session_state:
        st.session_state.image_history = []
    
    style = st.selectbox(
        "Select Style",
        ["Realistic", "Cartoon", "3D", "Anime", "Cyberpunk"]
    )
    prompt = st.chat_input("A futuristic Mumbai skyline at sunset")
    
    if "image_history" in st.session_state:
        display_chat()
        if prompt:
            final_prompt = f"{style} style: {prompt}"
            st.session_state.image_history.append(("user", final_prompt))
            st.chat_message("user").write(final_prompt)
            
            # Placeholder for spinner (important)
            spinner_placeholder = st.empty()

            # Show spinner ABOVE input using placeholder
            with spinner_placeholder:
                with st.spinner("Generating image..."):
                    image_bytes = image_service.handle_request(final_prompt)

            # Clear spinner (optional)
            spinner_placeholder.empty()

            #Add Image to chat history
            st.session_state.image_history.append(("assistant", image_bytes[0]))

            st.rerun()
    