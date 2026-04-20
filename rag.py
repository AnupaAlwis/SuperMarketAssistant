import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Force CPU mode

import pandas as pd
from langchain.schema import Document
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import CHROMA_DIR

def _get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

def build_vectorstore(db):
    query = "SELECT name, description FROM Products"
    df = pd.read_sql(query, db._engine)

    docs = []
    for _, row in df.iterrows():
        docs.append(Document(
            page_content=row["description"],
            metadata={"name": row["name"]}
        ))

    embeddings = _get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    return vectorstore

def load_vectorstore():
    embeddings = _get_embeddings()

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