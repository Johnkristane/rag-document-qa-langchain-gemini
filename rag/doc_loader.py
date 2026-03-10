from langchain_community.document_loaders import PyPDFLoader

def load_docs(filepath):
    loader = PyPDFLoader(filepath)
    docs = loader.load()
    return docs