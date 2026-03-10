import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def build_qa_chain(retriever):
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0.3
    )
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question based only on the provided context
        
        Context:
        {context}
        
        Question:
        {input}
        
        Return JSON like this:

        {{
        "answer": "...",
        "source": "..."
        }}
        """
    )
    document_chain = create_stuff_documents_chain(llm = llm, prompt = prompt)
    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain