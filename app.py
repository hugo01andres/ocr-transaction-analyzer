# app.py
import streamlit as st
from src import chat_agent

st.set_page_config(page_title="OCR Transaction Analyzer", page_icon="🧾", layout="centered")

st.title("💬 OCR Transaction Analyzer (Conversational Mode)")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Save user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    reply = chat_agent.handle_user_input(prompt)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)