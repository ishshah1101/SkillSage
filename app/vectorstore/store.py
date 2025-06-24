# app/vectorstore/store.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vectorstore_from_text(text: str):
    # 2. Break text into chunks (for better search and accuracy)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    # 3. Convert chunks into vectors and store in FAISS
    vectorstore = FAISS.from_texts(chunks, embedding=embedding_model)

    return vectorstore
