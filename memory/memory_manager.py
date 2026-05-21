from langchain_classic.memory import ConversationBufferWindowMemory

def get_memory():

    return ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        k=3
    )