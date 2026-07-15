import streamlit as st


class Memory:
    """
    Central Memory Manager for Project BRAHMA.

    Stores:
        1. Conversation History
        2. User Memory / Preferences

    This class is Streamlit-session aware and survives reruns.
    """

    def __init__(self):

        if "history" not in st.session_state:
            st.session_state.history = []

        if "memory" not in st.session_state:
            st.session_state.memory = {}

    # ======================================================
    # Chat History
    # ======================================================

    def add_message(self, role: str, content: str):
        """
        role:
            user
            assistant
            system
        """

        st.session_state.history.append(
            {
                "role": role,
                "content": content,
            }
        )

    def get_history(self):
        return st.session_state.history

    def clear_history(self):
        st.session_state.history.clear()

    # ======================================================
    # User Memory
    # ======================================================

    def remember(self, key: str, value):

        st.session_state.memory[key] = value

    def recall(self, key: str, default=None):

        return st.session_state.memory.get(key, default)

    def forget(self, key: str):

        if key in st.session_state.memory:
            del st.session_state.memory[key]

    def clear_memory(self):

        st.session_state.memory.clear()

    def get_memory(self):

        return st.session_state.memory

    # ======================================================
    # Everything
    # ======================================================

    def reset(self):

        self.clear_history()
        self.clear_memory()