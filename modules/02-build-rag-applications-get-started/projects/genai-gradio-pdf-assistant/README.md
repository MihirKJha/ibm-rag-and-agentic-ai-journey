# 📄 GenAI Gradio QA Bot

A Generative AI-powered Question Answering (QA) application that enables users to upload PDF documents and ask natural language questions about their contents. Built using **Gradio**, **LangChain**, **IBM watsonx.ai**, and **ChromaDB**, the application implements a Retrieval-Augmented Generation (RAG) pipeline to deliver accurate, context-aware answers from uploaded documents.

---

## ✨ Features

- 📄 Upload and analyze PDF documents
- 🤖 AI-powered document question answering
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ ChromaDB vector database
- 📚 IBM Granite foundation model
- 🔗 LangChain RetrievalQA pipeline
- ✂️ Automatic document chunking
- 🌐 Interactive Gradio web interface
- 🏗 Modular and extensible architecture

---

## 📖 Overview

Finding relevant information in lengthy documents can be time-consuming. This project simplifies document exploration by combining semantic search with Large Language Models (LLMs).

The application processes uploaded PDF documents by extracting text, splitting it into manageable chunks, generating vector embeddings, and storing them in a Chroma vector database. When a user submits a question, the application retrieves the most relevant document chunks and provides an AI-generated answer using IBM Granite through LangChain.

This project demonstrates the complete workflow of building a Retrieval-Augmented Generation (RAG) application using modern AI engineering practices.

---

## 🏗 Solution Architecture

```text
                     User
                       │
                       ▼
              Gradio Web Interface
                       │
                       ▼
               Upload PDF Document
                       │
                       ▼
                  PyPDFLoader
                       │
                       ▼
      RecursiveCharacterTextSplitter
                       │
                       ▼
          Watsonx Embedding Model
                       │
                       ▼
              Chroma Vector Store
                       │
                       ▼
                  Retriever
                       │
                       ▼
           LangChain RetrievalQA
                       │
                       ▼
         IBM Granite Foundation Model
                       │
                       ▼
          Context-Aware AI Response
```

---

## ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Frontend | Gradio |
| AI Framework | LangChain |
| AI Platform | IBM watsonx.ai |
| Foundation Model | IBM Granite |
| Embeddings | Watsonx Embeddings |
| Vector Database | ChromaDB |
| Document Loader | PyPDFLoader |
| PDF Processing | PyPDF |

---

## 📂 Project Structure

```text
.
├── qabot.py                 # Main application
├── requirements.txt
├── README.md
└── sample_pdfs/             # Sample documents (optional)
```

---

## 🔄 Application Workflow

1. Upload a PDF document.
2. Extract document content using **PyPDFLoader**.
3. Split the document into smaller chunks.
4. Generate vector embeddings for each chunk.
5. Store embeddings in **ChromaDB**.
6. Retrieve the most relevant document chunks based on the user's query.
7. Send the retrieved context to the LLM.
8. Generate and display a context-aware response.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>

cd genai-gradio-pdf-assistant
```

### Create a Virtual Environment

**Linux / macOS**

```bash
python -m venv my_env
source my_env/bin/activate
```

**Windows**

```bash
python -m venv my_env
my_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python qabot.py
```

Open your browser:

```
http://127.0.0.1:7860
```

---

## 💬 Example

**User Query**

```text
Summarize the uploaded document.
```

**AI Response**

```text
The document discusses...
```

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- LangChain
- Semantic Search
- Vector Databases
- Embedding Models
- Document Processing
- Prompt Engineering
- AI Application Development
- Python

---

## 🔮 Future Enhancements

- Multi-document knowledge base
- Persistent vector storage
- Conversation memory
- Source citations
- Streaming responses
- Hybrid Search (BM25 + Vector Search)
- OCR support for scanned PDFs
- Docker support
- Cloud deployment
- Authentication & authorization

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 👨‍💻 Author

**Mihir Jha**

**Software Architect | AI Engineering | Multi-Cloud Solutions**

Passionate about designing intelligent, scalable, and resilient applications that combine cloud-native architecture with modern Generative AI technologies.

If you're interested in **Enterprise AI Engineering**, **Cloud Architecture**, **Large Language Models**, **RAG**, **AI Agents**, or **Production AI Systems**, feel free to explore the repository, share feedback, or connect with me.

## GitHub

**https://github.com/MihirKJha**

## LinkedIn

**https://www.linkedin.com/in/mihirkrjha/**

## Newsletter

**Enterprise AI Engineering**

**https://www.linkedin.com/newsletters/enterprise-ai-engineering-7479222208079319041/**

Sharing practical insights on Enterprise AI, Cloud Architecture, Backend Engineering, Large Language Models, RAG, AI Agents, and production-ready AI systems.