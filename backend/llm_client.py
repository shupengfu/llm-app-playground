from openai import OpenAI

from backend.config import (
    LLM_BACKEND,
    LLM_BASE_URL,
    LLM_API_KEY,
    LLM_MODEL,
    LLM_REQUEST_TIMEOUT,
)


client = OpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY,
    timeout=LLM_REQUEST_TIMEOUT,
)


def get_backend_info() -> dict:
    return {
        "backend": LLM_BACKEND,
        "base_url": LLM_BASE_URL,
        "model": LLM_MODEL,
        "timeout": LLM_REQUEST_TIMEOUT,
    }


def chat_with_llm(prompt: str, temperature: float = 0.7, max_tokens: int = 800) -> str:
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "你是一个严谨、清晰、实用的大模型应用助手。",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content