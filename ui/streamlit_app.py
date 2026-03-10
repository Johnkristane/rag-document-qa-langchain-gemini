import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from rag.doc_loader import load_docs
from rag.text_splitter import split_docs
from rag.embeddings import get_embeddings
from rag.vector_stores import get_vector_store
from rag.retriever import get_retriever
from rag.qa_chain import build_qa_chain

st.title("AI based Docs Q&A")
uploaded_file = st.file_uploader("Upload pdf")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_docs("temp.pdf")
    chunks = split_docs(docs)
    embeds = get_embeddings()
    vector_store = get_vector_store(chunks, embeds)
    retriever = get_retriever(vector_store)
    qa_chain = build_qa_chain(retriever)

    question = st.text_input("Ask A Question from the uploaded doc")

    if question:
         response = qa_chain.invoke(
             {"input": question}
         )

         st.write(response["answer"])