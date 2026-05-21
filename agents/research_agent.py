from langchain_classic.agents.agent import AgentExecutor
from langchain_classic.agents import create_tool_calling_agent

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

from agents.model_loader import load_model
from agents.tool_router import get_tools

from memory.memory_manager import get_memory

SYSTEM_PROMPT = """
You are an advanced AI Research Assistant.

RULES:
- ALWAYS use tools before answering.
- NEVER answer directly from memory.
- ALWAYS search the web first.
- ALWAYS provide citations.
"""

def create_research_agent(
    temperature: float = 0.1
):

    llm = load_model(
        temperature=temperature
    )

    tools = get_tools()

    memory = get_memory()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),

            MessagesPlaceholder(
                variable_name="chat_history"
            ),

            ("human", "{input}"),

            MessagesPlaceholder(
                variable_name="agent_scratchpad"
            )
        ]
    )

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

    return agent_executor