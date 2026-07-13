import streamlit as st

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo


@st.cache_resource
def create_web_search_agent():
    return Agent(
        name="Web Search Agent",
        role="Search the web for information",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        instructions=[
            "Always include sources and provide reference web links"
        ],
        show_tool_calls=True,
        markdown=True,
    )


web_search_agent = create_web_search_agent()