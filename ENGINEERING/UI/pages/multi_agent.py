import streamlit as st

from phi.agent import Agent
from phi.model.google import Gemini

from ENGINEERING.AGENTS.web_search_agent import web_search_agent
from ENGINEERING.AGENTS.finance_agent import finance_agent
from ENGINEERING.AGENTS.research_agent import ra as research_Agent
from ENGINEERING.AGENTS.arxiv_agent import Arxiv_paper_agent


@st.cache_resource
def create_multi_agents_chain():
    return Agent(
        team=[
            web_search_agent,
            finance_agent,
            research_Agent,
            Arxiv_paper_agent,
        ],
        model=Gemini(id="gemini-2.5-flash"),
        instructions=[
            "Always include sources and provide reference web links",
            "Use tables to display the data",
            "Transfer the user's request to the most appropriate agent.",
        ],
        show_tool_calls=True,
        markdown=True,
        add_datetime_to_instructions=True,
    )


mac = create_multi_agents_chain()