from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

def get_vector_store(chunks,embeddings):
    pc = Pinecone(
        api_key = os.getenv("PINECONE_API_KEY")
    )
    index_name = os.getenv("PINECONE_INDEX_NAME")

    vector_store = PineconeVectorStore.from_documents(
        documents = chunks,
        embedding = embeddings,
        index_name = index_name
    )

    return vector_store

