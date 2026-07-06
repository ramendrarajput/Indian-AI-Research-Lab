"""
Project BRAHMA

Public AI Interface
"""

from core.registry import get_chat_model


def chat(
    prompt: str,
    system_prompt: str | None = None,
):
    """
    Generate text response.
    """

    model = get_chat_model()

    inputs = []

    if system_prompt:
        inputs.append(system_prompt)

    inputs.append(prompt)

    response = model.generate_content(inputs)

    return response.text