# 🚀 GenAI Multi LLM Assistant

A modular Generative AI web application that provides a unified interface for interacting with multiple Large Language Models (LLMs). Built with **Flask**, **LangChain**, and **IBM watsonx.ai**, the application demonstrates how modern AI applications can abstract different foundation models behind a common interface while producing structured, reliable outputs.

Instead of coupling the application to a single model, users can seamlessly switch between **IBM Granite**, **Meta Llama**, and **Mistral** to compare response quality, latency, and model behavior without changing application logic.

---

## ✨ Features

- 🤖 Multi-LLM support
  - IBM Granite
  - Meta Llama
  - Mistral
- 🌐 Interactive Flask web application
- 🧠 Prompt engineering with model-specific prompt templates
- 🔄 Unified interface for multiple foundation models
- 📄 Structured JSON responses using LangChain Output Parsers
- ✅ Response validation using Pydantic
- ⚡ Response latency measurement
- 🏗 Modular and extensible architecture
- 🎨 Clean web interface for model comparison

---

# 📖 Overview

Modern AI applications rarely rely on a single foundation model. Different models excel at different tasks such as reasoning, summarization, coding, or conversational AI.

This project demonstrates a clean architectural approach where multiple LLMs are abstracted behind a reusable AI service layer.

The application allows users to:

- Select a foundation model.
- Submit natural language prompts.
- Generate structured AI responses.
- Compare outputs from multiple LLMs.
- Build reusable AI workflows using LangChain.

The project also demonstrates best practices for building maintainable GenAI applications, including modular code organization, reusable prompt templates, and structured response parsing.

---

# 🏗 Solution Architecture

```text
                        User
                          │
                          ▼
                 Flask Web Interface
                          │
                          ▼
                  AI Service Layer
                          │
                Prompt Engineering
                          │
                          ▼
                   LangChain Chain
                          │
                          ▼
                IBM watsonx.ai Platform
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   IBM Granite       Meta Llama        Mistral
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
             Structured JSON Output Parser
                          │
                          ▼
                   Response to User
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Backend | Flask |
| AI Framework | LangChain |
| AI Platform | IBM watsonx.ai |
| Foundation Models | IBM Granite, Meta Llama, Mistral |
| Prompt Management | LangChain PromptTemplate |
| Output Parsing | JsonOutputParser |
| Validation | Pydantic |
| Frontend | HTML, CSS, JavaScript |

---

# 📂 Project Structure

```text
.
├── app.py
├── config.py
├── model.py
├── llm_test.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   └── script.js
│
└── README.md
```

---

# 🔄 Application Workflow

1. User selects an LLM from the web interface.
2. User submits a prompt.
3. Flask forwards the request to the AI service layer.
4. LangChain formats the prompt using a model-specific template.
5. The selected foundation model generates a response.
6. LangChain validates and parses the response into structured JSON.
7. The formatted response is returned to the user.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone 'repo_url'

cd genai-multi-llm-assistant
```

## Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

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

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

# 💡 AI Concepts Demonstrated

- Large Language Models (LLMs)
- Multi-Model AI Integration
- Prompt Engineering
- Structured AI Outputs
- JSON Response Parsing
- Model Abstraction Layer
- LangChain Chains
- AI Service Architecture

---

# 🎯 Skills Demonstrated

- Generative AI Application Development
- Flask
- LangChain
- IBM watsonx.ai
- Prompt Engineering
- Multi-LLM Integration
- Pydantic
- JSON Parsing
- REST API Development
- Python

---

# 🔮 Future Enhancements

- Conversation memory
- Retrieval-Augmented Generation (RAG)
- Function Calling
- Tool Calling
- Streaming responses
- Authentication & Authorization
- Docker support
- Kubernetes deployment
- Cloud deployment
- LLM benchmarking dashboard
- Conversation analytics

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