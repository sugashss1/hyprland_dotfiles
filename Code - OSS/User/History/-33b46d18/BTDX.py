from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_text(prompt: str) -> str:
    """
    Sends a prompt to the LLM and returns the final output text only
    (reasoning is ignored).
    """
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.environ["llm_api"],
    )

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[prompt],
        max_output_tokens=4096,
        top_p=1,
        temperature=1,
        stream=True,
    )

    output_text = []

    for chunk in response:
        if chunk.type == "response.output_text.delta":
            output_text.append(chunk.delta)

    return "".join(output_text)
