import os
from dotenv import load_dotenv

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.email import EmailTools

load_dotenv()

Email_agent = Agent(
    name="Email Agent",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Always send emails professionally."
    ],
    tools=[
        EmailTools(
            receiver_email=os.getenv("EMAIL_RECEIVER"),
            sender_email=os.getenv("EMAIL_SENDER"),
            sender_name=os.getenv("EMAIL_NAME"),
            sender_passkey=os.getenv("EMAIL_PASSKEY"),
        )
    ],
    show_tool_calls=True,
    markdown=True,
)