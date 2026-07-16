# 🤖 GenAI Chat Assistant

A Generative AI chatbot built using **Gradio**, **LangChain**, and **IBM watsonx.ai**. The application provides an intuitive web interface for interacting with Large Language Models (LLMs), demonstrating how to build AI-powered applications with a clean, modular architecture.

The project showcases how modern AI applications combine a lightweight frontend with enterprise-grade foundation models to deliver real-time conversational experiences.

---

## ✨ Features

- 🤖 AI-powered chatbot
- 🌐 Interactive Gradio web interface
- 🧠 IBM Granite foundation model integration
- 🔄 Easy model configuration
- ⚡ Real-time AI responses
- 🔗 LangChain-powered LLM integration
- 🏗 Modular and extensible architecture
- 🚀 Local deployment

---

## 📖 Overview

Large Language Models (LLMs) are transforming how users interact with applications by enabling natural language conversations.

This project demonstrates how to build an AI chatbot that integrates **IBM watsonx.ai** foundation models with a simple Gradio interface. The application accepts user prompts, forwards them to the configured LLM through LangChain, and returns AI-generated responses in real time.

It serves as a practical example of integrating enterprise AI services into modern Python web applications.

---

## 🏗 Solution Architecture

```text
                   User
                     │
                     ▼
            Gradio Web Interface
                     │
                     ▼
             Prompt Processing
                     │
                     ▼
             LangChain WatsonxLLM
                     │
                     ▼
             IBM watsonx.ai API
                     │
                     ▼
         IBM Granite Foundation Model
                     │
                     ▼
           AI Generated Response
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
| LLM Wrapper | WatsonxLLM |
| Web Server | FastAPI, Uvicorn |

---

## 📂 Project Structure

```text
.
├── llm_chat.py
├── simple_llm.py
├── gradio_demo.py
├── common_input_types.py
├── requirements.txt
└── README.md
```

---

## 🔄 Application Workflow

1. Launch the Gradio web application.
2. Enter a question in the chatbot interface.
3. The prompt is sent to LangChain.
4. LangChain invokes the configured IBM Granite foundation model through watsonx.ai.
5. The generated response is returned and displayed in the chatbot interface.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>

cd genai-multi-llm-assistant
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
python llm_chat.py
```

Open your browser:

```
http://127.0.0.1:7860
```

---

## 💬 Example

**User**

```text
What is Retrieval-Augmented Generation (RAG)?
```

**Assistant**

```text
Retrieval-Augmented Generation (RAG) combines information retrieval with
Large Language Models, allowing responses to be generated using relevant
external knowledge in addition to the model's pretrained knowledge.
```

---

## 🎯 Skills Demonstrated

- Generative AI Application Development
- Large Language Models (LLMs)
- LangChain
- IBM watsonx.ai
- Gradio
- Prompt Engineering
- Python Development
- AI API Integration

---

## 🔮 Future Enhancements

- Conversation memory
- Streaming responses
- Multi-model support
- Retrieval-Augmented Generation (RAG)
- Document chat
- Docker support
- Cloud deployment
- Authentication

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