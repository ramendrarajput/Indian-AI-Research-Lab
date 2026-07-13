import streamlit as st

from phi.agent import Agent
from phi.model.google import Gemini

from agents.web_search_agent import web_search_agent
from agents.finance_agent import finance_agent
from agents.research_agent import ra as research_Agent
from agents.arxiv_agent import Arxiv_paper_agent
#from agents.email_agent import Email_agent
#from agents.calculator_agent import Calculator_agent


@st.cache_resource
def create_multi_agents_chain():
    return Agent(
        team=[
            web_search_agent,
            finance_agent,
            research_Agent,
            Arxiv_paper_agent,
            #Email_agent,
            #Calculator_agent,
        ],
        model=Gemini(id="gemini-2.5-flash"),
        instructions=[
            "Always include sources and provide reference web links",
            "Use tables to display the data",
            "For the provided topic, run 3 different searches. Read the results carefully and prepare a NYT worthy report. Focus on facts and make sure to provide references.",
            "Always send email to given user",
            "Always do calculation according to user",
        ],
        show_tool_calls=True,
        markdown=True,
        add_datetime_to_instructions=True,
        save_response_to_file="venv/output/{user_query}.md",
    )


mac = create_multi_agents_chain()