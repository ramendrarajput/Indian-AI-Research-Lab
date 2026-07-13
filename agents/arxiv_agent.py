import streamlit as st

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.arxiv_toolkit import ArxivToolkit


@st.cache_resource
def create_arxiv_agent():
    return Agent(
        name="Arxiv paper agent",
        role="Search the web for Arxiv papers",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[ArxivToolkit()],
        instructions=[
            "Always include sources and provide reference web links"
        ],
        show_tool_calls=True,
    )


Arxiv_paper_agent = create_arxiv_agent()