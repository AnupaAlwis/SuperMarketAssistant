from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_ollama import ChatOllama
from tools import get_sql_tool, get_rag_tool

def create_agent():
    llm = ChatOllama(
        model="llama3",
        temperature=0.3
    )

    sql_tool = get_sql_tool()
    rag_tool = get_rag_tool(llm)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    system_prompt = """
You are an intelligent supermarket assistant.

Rules:
- Use Database Tool for prices, stock, supplier
- Use Product Knowledge Base for recommendations
- Use both tools if needed
- Always give clear answers
"""

    agent = initialize_agent(
        tools=[sql_tool, rag_tool],
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory,
        verbose=True,
        agent_kwargs={"system_message": system_prompt}
    )

    return agent