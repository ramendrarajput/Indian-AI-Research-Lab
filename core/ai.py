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

from core.registry import get_vision_model_instance


def vision(image, prompt):

    model = get_vision_model_instance()

    response = model.generate_content(
        [image, prompt]
    )

    return response.text