# 💼 GenAI Networking Assistant

An AI-powered networking assistant that generates personalized conversation starters and professional insights from profile data using **LlamaIndex**, **IBM watsonx.ai**, and **Gradio**. The application demonstrates how Retrieval-Augmented Generation (RAG) can transform professional profile information into meaningful networking conversations.

---

## ✨ Features

- 💼 Analyze professional profile information
- 🤖 Generate personalized networking icebreakers
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Semantic indexing with LlamaIndex
- ⚡ IBM Granite foundation model integration
- 🔍 Vector-based semantic retrieval
- 🌐 Interactive Gradio web interface
- 🏗 Modular and extensible architecture

---

# 📖 Overview

Building meaningful professional relationships often starts with a great conversation. However, researching someone's background before a networking event or interview can be time-consuming.

This application demonstrates how Generative AI can automate that process by analyzing professional profile information and generating personalized conversation starters, interesting facts, and contextual responses.

The application processes profile data, builds a semantic index using **LlamaIndex**, retrieves relevant information through vector search, and uses **IBM Granite** to generate engaging networking icebreakers.

> **Note:** This project uses mock profile data for demonstration purposes. The original LinkedIn data extraction approach has been replaced because third-party profile extraction services used in earlier versions are no longer supported.

---

# 🏗 Solution Architecture

```text
                    User
                      │
                      ▼
             Gradio Web Interface
                      │
                      ▼
          Professional Profile Data
                (Mock Dataset)
                      │
                      ▼
          LlamaIndex Document Loader
                      │
                      ▼
         Text Chunking & Processing
                      │
                      ▼
        Watsonx Embedding Generation
                      │
                      ▼
          LlamaIndex Vector Index
                      │
                      ▼
              Semantic Retrieval
                      │
                      ▼
      IBM Granite Foundation Model
                      │
                      ▼
 Personalized Networking Suggestions
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Frontend | Gradio |
| AI Framework | LlamaIndex |
| AI Platform | IBM watsonx.ai |
| Foundation Model | IBM Granite |
| Embeddings | Watsonx Embeddings |
| Retrieval Engine | LlamaIndex Query Engine |
| AI Pattern | Retrieval-Augmented Generation (RAG) |

---

# 📂 Project Structure

```text
.
├── app.py                     # Gradio application
├── main.py                    # Command-line interface
├── config.py                  # Application configuration
├── requirements.txt
│
├── modules/
│   ├── data_extraction.py     # Profile data extraction
│   ├── data_processing.py     # Chunking & indexing
│   ├── llm_interface.py       # LLM & embedding initialization
│   └── query_engine.py        # RAG query engine
│
└── README.md
```

---

# 🔄 Application Workflow

1. Load professional profile data.
2. Process and split profile information into chunks.
3. Generate vector embeddings using IBM Watsonx Embeddings.
4. Build a semantic vector index with LlamaIndex.
5. Retrieve relevant profile information based on user queries.
6. Generate personalized networking icebreakers using IBM Granite.
7. Display AI-generated responses through the Gradio interface.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone <repository-url>

cd genai-networking-assistant
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

### Command-Line Interface

```bash
python main.py
```

### Launch the Gradio Interface

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:7860
```

---

# 💬 Example

### User Request

```text
Generate networking icebreakers for Sarah Johnson.
```

### AI Response

```text
• I noticed you've transitioned from software engineering into AI. What inspired that shift?

• Your experience designing cloud-native applications is impressive. Which project taught you the most?

• I saw your work in Generative AI. Which recent advancement has excited you the most?
```

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- LlamaIndex
- Large Language Models (LLMs)
- Semantic Search
- Vector Embeddings
- IBM watsonx.ai
- Prompt Engineering
- AI Application Development
- Python
- Gradio

---

# 🔮 Future Enhancements

- LinkedIn API integration
- Resume analysis
- GitHub profile analysis
- Portfolio summarization
- Conversation memory
- Multi-profile comparison
- AI-generated outreach messages
- Docker support
- Cloud deployment
- Authentication & user management

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