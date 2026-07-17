# 🔍 GenAI Text Similarity Search

A semantic search application that demonstrates how vector embeddings and ChromaDB can be used to perform similarity search over text documents. Built using **ChromaDB**, **Sentence Transformers**, and **Python**, the project showcases how modern AI applications retrieve semantically relevant information using vector embeddings instead of traditional keyword matching.

---

## ✨ Features

- 🔍 Semantic similarity search
- 📚 Vector embedding generation
- ⚡ ChromaDB vector database
- 🧠 Sentence Transformer embeddings
- 📄 Automatic document indexing
- 🚀 Fast nearest-neighbor retrieval
- 🏗 Simple and modular implementation

---

# 📖 Overview

Traditional search relies on exact keyword matching, which often fails to capture semantic meaning.

This project demonstrates semantic search by converting text into vector embeddings using a Sentence Transformer model and storing those embeddings in ChromaDB. User queries are embedded in the same vector space, allowing the application to retrieve documents based on meaning rather than exact words.

---

# 🏗 Solution Architecture

```text
              Text Documents
                     │
                     ▼
       Sentence Transformer Model
                     │
                     ▼
            Vector Embeddings
                     │
                     ▼
              ChromaDB Collection
                     │
                     ▼
              Similarity Search
                     │
                     ▼
            Ranked Search Results
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Vector Database | ChromaDB |
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Framework | Sentence Transformers |
| ML Framework | PyTorch |

---

# 📂 Project Structure

```text
.
├── similarity_search.py
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

1. Create a ChromaDB collection.
2. Generate embeddings for text documents.
3. Store embeddings in the vector database.
4. Convert user queries into embeddings.
5. Perform nearest-neighbor similarity search.
6. Return the most relevant documents.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone <repository-url>

cd genai-semantic-search
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python similarity_search.py
```

---

# 💬 Example

**Query**

```text
apple
```

**Results**

```text
fresh red apples
golden apple
red fruit
```

---

# 🎯 Skills Demonstrated

- Semantic Search
- Vector Databases
- ChromaDB
- Sentence Transformers
- Embeddings
- Similarity Search
- Python

---

# 🔮 Future Enhancements

- Persistent ChromaDB storage
- PDF document search
- Hybrid search (BM25 + Vector Search)
- Web interface
- REST API
- RAG integration

---

# 📄 License

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
