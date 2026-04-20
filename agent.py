from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_ollama import ChatOllama
from tools import get_sql_tool, get_rag_tool

def create_agent():
    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )

    sql_tool = get_sql_tool()
    rag_tool = get_rag_tool(llm)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    agent = initialize_agent(
        tools=[sql_tool, rag_tool],
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,
    )

    return agent