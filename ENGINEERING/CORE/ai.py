"""
Project BRAHMA

Public AI Interface
"""

from ENGINEERING.CORE.registry import get_chat_model
#from .registry import get_chat_model

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

from ENGINEERING.CORE.registry import get_vision_model_instance

def vision(
    image,
    prompt: str,
    system_prompt: str | None = None,
):

    model = get_vision_model_instance()

    inputs = []

    if system_prompt:
        inputs.append(system_prompt)

    inputs.append(image)
    inputs.append(prompt)

    response = model.generate_content(inputs)

    return response.text