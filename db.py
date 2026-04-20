from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_ollama import ChatOllama
from config import DB_URI

def get_database():
    return SQLDatabase.from_uri(DB_URI)

def get_sql_chain():
    db = get_database()

    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )

    db_chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True
    )

    return db_chain