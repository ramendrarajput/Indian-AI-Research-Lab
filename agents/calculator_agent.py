from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.calculator import Calculator

Calculator_agent = Agent(
    name="Calculator Agent",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "Always perform accurate mathematical calculations."
    ],
    tools=[
        Calculator(
            add=True,
            subtract=True,
            multiply=True,
            divide=True,
            exponentiate=True,
            factorial=True,
            is_prime=True,
            square_root=True,
        )
    ],
    show_tool_calls=True,
    markdown=True,
)