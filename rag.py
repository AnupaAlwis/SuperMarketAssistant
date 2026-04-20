import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import CHROMA_DIR

def build_vectorstore(db):
    query = "SELECT name, description FROM items"
    df = pd.read_sql(query, db.engine)

    docs = []
    for _, row in df.iterrows():
        docs.append({
            "page_content": row["description"],
            "metadata": {"name": row["name"]}
        })

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    vectorstore.persist()
    return vectorstore

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

def get_retriever(db, rebuild=False):
    if rebuild:
        vectorstore = build_vectorstore(db)
    else:
        vectorstore = load_vectorstore()

    return vectorstore.as_retriever(search_kwargs={"k": 3})