"""
Project BRAHMA

UI Page Dispatcher
"""

import streamlit as st


def render_page(selected_page: str):
    """
    Render selected application page.
    """

    if selected_page == "2: AI Chatbot":
        st.info("AI Chatbot module coming soon.")