import os

from langchain_groq import ChatGroq

def load_model(
    temperature: float = 0.1
):

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="qwen/qwen3-32b",
        temperature=temperature,
        max_tokens=4096
    )

    return llm