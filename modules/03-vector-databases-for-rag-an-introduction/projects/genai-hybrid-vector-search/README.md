# 🔍 GenAI Hybrid Vector Search

A Python application that demonstrates **Hybrid Vector Search** using **ChromaDB** and **Sentence Transformers**. The project showcases how semantic similarity search and metadata filtering can be combined to retrieve highly relevant employee records from a vector database.

This project highlights one of the core retrieval techniques used in modern AI applications, including **Retrieval-Augmented Generation (RAG)**, enterprise search, recommendation systems, and talent search platforms.

---

# ✨ Features

- 🔍 Semantic similarity search using vector embeddings
- 🧠 Sentence Transformer embeddings
- ⚡ ChromaDB vector database
- 🏷 Metadata-based filtering
- 🔄 Hybrid search (Semantic Search + Metadata Filtering)
- 👥 Employee profile retrieval
- 📊 Rich metadata indexing
- 🏗 Modular Python implementation

---

# 📖 Overview

Traditional keyword search often struggles to understand the intent behind user queries. Hybrid Vector Search addresses this limitation by combining semantic understanding with structured metadata filtering.

In this project, employee profiles are converted into vector embeddings using a Sentence Transformer model and stored in ChromaDB. User queries are embedded into the same vector space, enabling semantic retrieval based on meaning rather than exact keywords.

To improve search precision, metadata filters such as department, location, and years of experience can be applied alongside semantic similarity, resulting in more accurate and context-aware search results.

---

# 🏗 Solution Architecture

```text
                    Employee Records
                           │
                           ▼
                 Text Preprocessing
                           │
                           ▼
             Sentence Transformer Model
                  (all-MiniLM-L6-v2)
                           │
                           ▼
                  Vector Embeddings
                           │
                           ▼
                  ChromaDB Collection
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
 Semantic Similarity Search         Metadata Filtering
          │                                 │
          └────────────────┬────────────────┘
                           ▼
                  Hybrid Vector Search
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
| Machine Learning | PyTorch |
| Search Technique | Semantic Search + Metadata Filtering |

---

# 📂 Project Structure

```text
.
├── similarity_employeedata.py
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

1. Create a ChromaDB collection.
2. Load employee profile data.
3. Generate vector embeddings using Sentence Transformers.
4. Store embeddings and metadata in ChromaDB.
5. Perform semantic similarity search using natural language queries.
6. Apply metadata filters to refine search results.
7. Combine semantic similarity and metadata filtering for hybrid retrieval.
8. Return ranked employee profiles based on relevance.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone <repository-url>

cd genai-hybrid-vector-search
```

## Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Linux / macOS**

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

## Run the Application

```bash
python similarity_employeedata.py
```

---

# 💬 Search Examples

### Semantic Search

```text
Python developer with backend experience
```

Returns employees with semantically similar skills and experience.

---

### Metadata Filtering

```text
Department = Engineering
Experience >= 10 years
Location = San Francisco
```

Returns only employees matching the specified metadata.

---

### Hybrid Search

```text
Query:
Senior Python developer

Filters:
• Department = Engineering
• Experience >= 8 years
• Location = San Francisco
```

Returns employees that satisfy both semantic similarity and metadata constraints.

---

# 🎯 Skills Demonstrated

- Hybrid Vector Search
- Semantic Search
- Metadata Filtering
- Vector Databases
- ChromaDB
- Sentence Transformers
- Vector Embeddings
- Information Retrieval
- AI Search Systems
- Python Development

---

# 🌟 Key Concepts

- Vector Embeddings
- Semantic Similarity
- Nearest Neighbor Search
- Metadata Filtering
- Hybrid Search
- Cosine Similarity
- Enterprise Search
- Talent Search
- AI-Powered Information Retrieval

---

# 🔮 Future Enhancements

- Support larger employee datasets
- Persist ChromaDB collections for long-term storage
- Evaluate different embedding models for retrieval quality
- Compare cosine similarity with alternative distance metrics
- Implement hybrid keyword (BM25) + vector search
- Build an interactive Gradio-based search interface
- Expose search functionality through a REST API
- Integrate Retrieval-Augmented Generation (RAG) for natural language question answering
- Benchmark retrieval accuracy and search latency
- Deploy the application as a cloud-native search service

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

