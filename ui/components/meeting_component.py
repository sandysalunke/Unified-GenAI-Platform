import streamlit as st
from services import meeting_service, text_service
from helpers.utils import save_data, load_data, chunk_text
from helpers.embeddings import create_embeddings, search

def render():

    # Display chat
    def display_chat():
        st.subheader("Transcript")
        st.write(st.session_state.transcript)
        st.subheader("Meeting Insights")
        st.write(st.session_state.meeting_insights)
        for role, msg in st.session_state.meeting_assistant_history:
            st.chat_message(role).write(msg)

    if "meeting_assistant_history" not in st.session_state:
        st.session_state.meeting_assistant_history = []

    if "transcript" not in st.session_state:
        st.session_state.transcript = []

    if "meeting_insights" not in st.session_state:
        st.session_state.meeting_insights = []

    if "uploaded_names" not in st.session_state:
        st.session_state.uploaded_names = []

    if "embeddings" not in st.session_state:
        emb, ch = load_data()
        st.session_state.embeddings = emb
        st.session_state.chunks = ch
    
    # Streamlit UI
    # File uploader for meeting audio
    uploaded_file = st.file_uploader("Upload Meeting Audio", type=["mp4", "wav"])
    new_file_names = uploaded_file if uploaded_file else []

    if uploaded_file and new_file_names != st.session_state.uploaded_names:
        st.session_state.uploaded_names = new_file_names
        with open("data/audio.wav", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("Transcribing..."):
            transcript = meeting_service.transcribe_audio("data/audio.wav")
            st.session_state.transcript = transcript

        st.subheader("Transcript")
        st.write(transcript)
        
        with st.spinner("Analyzing..."):
            insights = meeting_service.process_meeting(transcript)
            st.session_state.meeting_insights = insights

        st.subheader("Meeting Insights")
        st.write(insights)

        with st.spinner("Getting you ready to ask questions..."):
            chunks = chunk_text(transcript)
            embeddings = create_embeddings(chunks)
            save_data(embeddings, chunks)

            st.session_state.embeddings = embeddings
            st.session_state.chunks = chunks

            st.success("✅ Transcript processed, you can ask questions now!")
    
    # Chat
    if st.session_state.embeddings is not None:
        
        query = st.chat_input("Ask a question (type 'exit' to reset)...")

        if query:
            display_chat()
            st.session_state.meeting_assistant_history.append(("user", query))
            st.chat_message("user").write(query)
            # ✅ Placeholder for spinner (important)
            spinner_placeholder = st.empty()

            if query.lower() == "exit":
                st.session_state.embeddings = None
                st.session_state.chunks = None
                st.session_state.meeting_assistant_history = []
                st.success("Session reset ✅")
                st.stop()

            # Generate answer
            # ✅ Show spinner ABOVE input using placeholder
            with spinner_placeholder:
                with st.spinner("Thinking..."):
                    context = search(query, st.session_state.embeddings, st.session_state.chunks)
                    answer = text_service.context_search(query, context)

            
            # Clear spinner (optional)
            spinner_placeholder.empty()

            st.session_state.meeting_assistant_history.append(("assistant", answer))

            # Display response immediately
            st.chat_message("assistant").write(answer)
