import streamlit as st

from core.ai import chat
from core.memory import Memory
from core.prompts import AI_CHATBOT_SYSTEM_PROMPT


def AI_Chatbot():

    memory = Memory()

    # ---------- Sidebar ----------
    st.sidebar.title("💬 AI Chat")

    if st.sidebar.button("🗑 Clear Chat"):
        memory.clear_history()
        st.rerun()

    st.sidebar.markdown(
        """
        ### Features

        - Gemini Powered
        - Conversation Memory
        - ChatGPT Style UI
        """
    )

    # ---------- Header ----------
    st.title("💬 AI Chat")
    st.caption("Powered by Project BRAHMA")

    # ---------- Chat History ----------
    for msg in memory.get_history():

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ---------- User Input ----------
    user_input = st.chat_input("Type your message...")

    if not user_input:
        return

    # ---------- Store User Message ----------
    memory.add_message("user", user_input)

    # ---------- Simple Memory ----------
    if "my name is" in user_input.lower():

        name = user_input.lower().split("my name is")[-1].strip()

        memory.remember("name", name)

        response = f"Ok {name}, I'll remember your name."

    elif "what is my name" in user_input.lower():

        name = memory.recall("name")

        if name:
            response = f"Your name is {name}."
        else:
            response = "Sorry! Please tell me your name first."

    else:

        with st.spinner("Thinking..."):

            response = chat(
                prompt=user_input,
                system_prompt=AI_CHATBOT_SYSTEM_PROMPT,
            )

    # ---------- Store Assistant Message ----------
    memory.add_message("assistant", response)

    st.rerun()