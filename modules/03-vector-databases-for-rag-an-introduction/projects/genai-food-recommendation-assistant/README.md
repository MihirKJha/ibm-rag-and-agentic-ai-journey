# 🍽️ GenAI Food Recommendation Assistant

A Retrieval-Augmented Generation (RAG) application that demonstrates how **semantic search**, **hybrid vector search**, and **Large Language Models (LLMs)** can be combined to build an intelligent food recommendation system.

Built using **IBM watsonx.ai**, **ChromaDB**, **Sentence Transformers**, and **Python**, the project showcases modern AI retrieval techniques that power recommendation systems, conversational assistants, and enterprise AI search applications.

---

# ✨ Features

- 🍽️ AI-powered food recommendation assistant
- 🔍 Interactive semantic search
- 🏷 Advanced metadata filtering
- 🔄 Hybrid vector search
- 🤖 Retrieval-Augmented Generation (RAG)
- 🧠 IBM Granite foundation model integration
- ⚡ ChromaDB vector database
- 📚 Sentence Transformer embeddings
- 💬 Conversational AI chatbot
- 📊 Search strategy comparison
- 🏗 Modular and reusable architecture

---

# 📖 Overview

Traditional recommendation systems often rely on keyword matching or predefined filters, limiting their ability to understand user intent.

This project demonstrates how modern AI techniques improve recommendation quality by combining **vector embeddings**, **semantic retrieval**, **metadata filtering**, and **Retrieval-Augmented Generation (RAG)**.

Food descriptions are transformed into vector embeddings using Sentence Transformers and stored in **ChromaDB**. When a user submits a natural language query, the application retrieves the most relevant food items using semantic similarity and optional metadata filters. The retrieved context is then provided to **IBM Granite**, which generates personalized food recommendations.

The repository contains multiple implementations that progressively demonstrate modern AI retrieval techniques:

- Interactive Semantic Search
- Advanced Hybrid Vector Search
- AI-powered RAG Chatbot
- Search Strategy Comparison

---

# 🏗 Solution Architecture

```text
                      User
                        │
                        ▼
             Natural Language Query
                        │
                        ▼
               Query Preprocessing
                        │
                        ▼
        Sentence Transformer Embeddings
                        │
                        ▼
               ChromaDB Vector Store
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 Semantic Search  Metadata Filters  Hybrid Search
        │               │                │
        └───────────────┼────────────────┘
                        ▼
          Retrieved Food Documents
                        │
                        ▼
       IBM Granite Foundation Model
                        │
                        ▼
      Personalized Food Recommendations
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| AI Platform | IBM watsonx.ai |
| Foundation Model | IBM Granite |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers |
| Machine Learning | PyTorch |
| AI Pattern | Retrieval-Augmented Generation (RAG) |
| Search Techniques | Semantic Search, Hybrid Search, Metadata Filtering |

---

# 📂 Project Structure

```text
.
├── advanced_search.py          # Hybrid vector search with metadata filtering
├── interactive_search.py       # Interactive semantic search application
├── enhanced_rag_chatbot.py     # RAG-powered food recommendation chatbot
├── shared_functions.py         # Shared utilities for embeddings and vector search
├── system_comparison.py        # Compare search strategies and performance
├── FoodDataSet.json            # Food dataset
├── food_with_category.json     # Categorized food dataset
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

### 1. Data Preparation

- Load food datasets from JSON files.
- Process food descriptions and metadata.
- Generate vector embeddings using Sentence Transformers.

### 2. Vector Indexing

- Store embeddings and metadata in ChromaDB.
- Build searchable vector collections.

### 3. Search & Retrieval

The project demonstrates three retrieval strategies:

- **Interactive Search** – Perform semantic similarity search using natural language queries.
- **Advanced Search** – Combine semantic similarity with metadata filtering for more precise recommendations.
- **Enhanced RAG Chatbot** – Retrieve relevant food items and generate AI-powered recommendations using IBM Granite.

### 4. AI Response Generation

- Retrieve relevant food documents.
- Supply retrieved context to the LLM.
- Generate personalized recommendations using Retrieval-Augmented Generation (RAG).

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone <repository-url>

cd genai-food-recommendation-assistant
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

## Run the Applications

### Interactive Semantic Search

```bash
python interactive_search.py
```

### Advanced Hybrid Search

```bash
python advanced_search.py
```

### Enhanced RAG Chatbot

```bash
python enhanced_rag_chatbot.py
```

### Compare Search Strategies

```bash
python system_comparison.py
```

---

# 💬 Example Queries

### Semantic Search

```text
Healthy high-protein breakfast
```

---

### Hybrid Search

```text
Query:
Spicy vegetarian dinner

Filters:
• Category = Vegetarian
• Calories < 500
```

---

### RAG Chatbot

```text
Recommend a high-protein vegetarian lunch under 600 calories.
```

**Sample Response**

```text
Based on your preferences, I recommend:

• Grilled Paneer Salad
• Chickpea Buddha Bowl
• Lentil Quinoa Bowl

These meals are high in protein, nutritionally balanced, and meet your calorie requirements.
```

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- IBM watsonx.ai
- IBM Granite
- ChromaDB
- Sentence Transformers
- Vector Databases
- Semantic Search
- Hybrid Vector Search
- Metadata Filtering
- Information Retrieval
- Prompt Engineering
- AI Application Development
- Python Development

---

# 🌟 Key Concepts

- Vector Embeddings
- Semantic Similarity
- Hybrid Search
- Metadata Filtering
- ChromaDB Collections
- Retrieval-Augmented Generation
- Information Retrieval
- Recommendation Systems
- AI-Powered Search
- Enterprise AI Applications

---

# 🔮 Future Enhancements

- Expand support for larger food and recipe datasets
- Persist ChromaDB collections for long-term storage
- Evaluate alternative embedding models
- Compare different similarity metrics for retrieval quality
- Enhance hybrid search with keyword (BM25) + vector search
- Build a Gradio or Streamlit web interface
- Expose recommendation services through REST APIs
- Add conversational memory for multi-turn interactions
- Benchmark retrieval accuracy and response latency
- Deploy as a cloud-native AI recommendation service

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