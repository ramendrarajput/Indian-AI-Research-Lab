from textwrap import dedent
from datetime import datetime
import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.exa import ExaTools

@st.cache_resource
def Research_Agent():
    return Agent(
        model=Gemini(id="gemini-2.5-flash"),
        tools=[
            ExaTools(
                start_published_date=datetime.now().strftime("%Y-%m-%d"),
                type="keyword",
            )
        ],
        description="You are an advanced AI researcher writing a report on a topic.",
        instructions=[
            "For the provided topic, run 3 different searches.",
            "Read the results carefully and prepare a NYT worthy report.",
            "Focus on facts and make sure to provide references.",
        ],
        expected_output=dedent("""
        An engaging, informative, and well-structured report in markdown format:

        ## Engaging Report Title

        ### Overview
        {give a brief introduction}

        ### Section 1
        {facts}

        ### Takeaways

        ### References

        - published on {date}
        """),
        markdown=True,
        show_tool_calls=True,
        add_datetime_to_instructions=True,
        save_response_to_file="tmp/{message}.md",
    )
ra = Research_Agent()