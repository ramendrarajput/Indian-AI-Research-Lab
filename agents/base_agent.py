import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

#@st.cache_resource
from core.cache import get_web_agent
agent = get_web_agent()
def create_web_multimodal_agent():
    return Agent(
        name="Summarizer",
        instructions="Always do a web search for getting details",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
    )
web_multimodal_Agent = create_web_multimodal_agent()