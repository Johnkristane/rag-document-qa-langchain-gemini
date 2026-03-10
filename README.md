# AI Document Question Answering System (RAG)

An end-to-end Retrieval Augmented Generation (RAG) application that allows users to upload documents and ask questions in natural language.  
The system retrieves relevant document chunks using vector search and generates answers using a Large Language Model.

---

# Problem

Organizations often store information in large documents such as PDFs, reports, manuals, or research papers.

Finding specific answers inside these documents is:

- Time-consuming
- Inefficient
- Hard to scale

Traditional keyword search cannot understand context or meaning.

---

# Solution

This project builds an **AI-powered Document Question Answering System** using Retrieval Augmented Generation (RAG).

The system:

1. Loads documents
2. Splits them into smaller chunks
3. Converts chunks into embeddings
4. Stores embeddings in a vector database
5. Retrieves relevant context for a question
6. Uses an LLM to generate answers

---

# Architecture
User Question

↓

Retriever

↓

Vector Database

↓

Relevant Chunks

↓

LLM

↓

Final Answer

----


Pipeline:

Document → Chunking → Embeddings → Vector DB → Retrieval → LLM → Answer

---

# Tech Stack

Python  
LangChain  
Pinecone Vector Database  
Google Gemini LLM  
HuggingFace Embeddings
Streamlit UI  

---

# Features

- Document ingestion
- Text chunking
- Semantic search using vector embeddings
- Retrieval Augmented Generation
- Natural language question answering
- Interactive web interface

---

# Project Structure
rag-document-qa/

rag/

    doc_loader.py

    text_splitter.py

    embeddings.py

    vector_store.py

    qa_chain.py


ui/

    streamlit_app.py

data/

    sample.pdf

screenshots/

    app_interface.png

.env.example

requirements.txt

README.md


---

# Installation

Clone the repository
git clone

https://github.com/Johnkristane/rag-document-qa-langchain-gemini.git

cd rag-document-qa

Install dependencies

pip install -r requirements.txt

Create environment variables

GOOGLE_API_KEY=your_key

PINECONE_API_KEY=your_key

Run the application

streamlit run ui/streamlit_app.py


---

# Example Usage

Upload a document and ask questions like:

What are the key points discussed in this document?

The system retrieves relevant sections and generates a contextual answer.

---

# Example Workflow

1. Upload PDF
2. Document is chunked
3. Embeddings are generated
4. Stored in Pinecone
5. Question is asked
6. Relevant chunks retrieved
7. Gemini LLM generates answer

---

# What I Learned From This Project

- Building a Retrieval Augmented Generation pipeline
- Using vector databases for semantic search
- Prompt engineering
- Integrating LLM APIs
- Designing modular AI systems
- Creating interactive AI applications

---

# Current Limitations

This project was built as a **beginner-level implementation of a RAG system** to understand the core concepts.

Some limitations currently exist:

### 1. No Persistent Index Management
The system may recreate embeddings when the app restarts.

Improvement:

Persist vector indexes and avoid recomputing embeddings.

---

### 2. Single Document Support
Currently optimized for small numbers of documents.

Improvement:

Add multi-document ingestion and indexing.

---

### 3. No Conversation Memory
Each question is independent.

Improvement:

Add conversational memory for chat-style interaction.

---

### 4. No Advanced Retrieval Techniques

The retriever currently uses basic similarity search.

Improvement:

Use techniques like:

- Hybrid search
- Reranking
- Multi-query retrieval

---

### 5. Basic Prompt Design

Prompt is simple and not optimized.

Improvement:

Use structured prompts and guardrails for better accuracy.

---

# Future Improvements (Next Version)

Planned upgrades:

- Multi-document ingestion
- Metadata filtering
- Chat history memory
- Source citations
- Reranking models
- Hybrid search (keyword + vector)
- LangGraph based agent workflows

These features will transform this project into a **production-ready AI knowledge assistant**.

---

# Author

Sunil Kumar Nallabothula

AI Engineer | Data Scientist | GenAI Engineer

---




