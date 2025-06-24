

# app/services/rag.py

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from langchain.vectorstores.base import VectorStore

llm = ChatOllama(model="llama3")


def get_rag_chain(vectorstore: VectorStore):
    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    return qa_chain
