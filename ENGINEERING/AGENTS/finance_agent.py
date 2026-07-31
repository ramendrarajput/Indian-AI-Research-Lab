## Financial agent
import streamlit as st

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools


@st.cache_resource
def create_finance_agent():
    return Agent(
        name="Finance AI Agent",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
            )
        ],
        instructions=[
            "Use tables to display the data"
        ],
        show_tool_calls=True,
        markdown=True,
    )


finance_agent = create_finance_agent()