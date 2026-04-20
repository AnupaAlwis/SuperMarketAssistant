from langchain.tools import Tool
from db import get_sql_chain, get_database
from rag import get_retriever

# SQL TOOL
def get_sql_tool():
    sql_chain = get_sql_chain()

    return Tool(
        name="Database Tool",
        func=sql_chain.run,
        description="""
        Use this tool for:
        - product prices
        - stock availability
        - supplier info
        - filtering items
        """
    )

# RAG TOOL
def get_rag_tool(llm):
    db = get_database()
    retriever = get_retriever(db)

    def rag_search(query):
        docs = retriever.get_relevant_documents(query)

        context = "\n".join([
            f"{doc.metadata.get('name', '')}: {doc.page_content}"
            for doc in docs
        ])

        response = llm.invoke(f"""
You are a supermarket assistant.

Use ONLY the context below to answer.

Context:
{context}

Question: {query}
""")

        return response.content

    return Tool(
        name="Product Knowledge Base",
        func=rag_search,
        description="""
        Use this for:
        - product descriptions
        - recommendations
        - semantic queries (healthy, cheap, best)
        """
    )