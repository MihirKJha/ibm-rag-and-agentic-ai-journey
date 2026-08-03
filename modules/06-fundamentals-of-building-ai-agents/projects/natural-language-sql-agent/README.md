# 🤖 Natural Language SQL Agent

An AI-powered SQL Agent that enables users to query relational databases using natural language. Built with **IBM watsonx.ai**, **LangChain**, and **MySQL**, the application translates human language into SQL queries, executes them against a database, and returns accurate results without requiring users to write SQL.

This project demonstrates how Large Language Models (LLMs) and AI Agents can simplify database interactions by combining natural language understanding, reasoning, and SQL execution into a seamless workflow.

---

# ✨ Features

- 🤖 Natural Language to SQL conversion
- 🗄️ Query relational databases using plain English
- 🧠 IBM Granite foundation model integration
- 🔄 LangChain SQL Agent
- ⚡ Automatic SQL query generation
- ✅ SQL execution with error recovery
- 📊 Database schema understanding
- 🔍 Multi-step reasoning using AI Agents
- 💬 Interactive command-line interface
- 🏗 Modular and reusable architecture

---

# 📖 Overview

Business users often need valuable insights from relational databases but may not be familiar with SQL syntax. Traditional data analysis requires writing complex SQL queries, understanding database schemas, and manually interpreting results.

This project demonstrates how an AI-powered SQL Agent bridges that gap by allowing users to ask questions in natural language. The LangChain SQL Agent interprets user intent, reasons about the database schema, generates SQL queries, executes them against a MySQL database, and converts the results into natural language responses.

The project uses the **Chinook** sample database, a digital media store containing customers, artists, albums, invoices, employees, playlists, and tracks, making it ideal for demonstrating enterprise database interactions. :contentReference[oaicite:0]{index=0}

---

# 🏗 Solution Architecture

```text
                    User
                      │
                      ▼
         Natural Language Question
                      │
                      ▼
             LangChain SQL Agent
                      │
                      ▼
             Agent Executor (ReAct)
                      │
                      ▼
          IBM Granite Foundation Model
                      │
                      ▼
          SQL Query Generation
                      │
                      ▼
              MySQL Database
                      │
                      ▼
             Query Execution
                      │
                      ▼
            Database Results
                      │
                      ▼
       Natural Language Response
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| AI Platform | IBM watsonx.ai |
| Foundation Model | IBM Granite |
| AI Framework | LangChain |
| Agent | LangChain SQL Agent |
| Database | MySQL |
| ORM / SQL Utility | SQLDatabase |
| Database Connector | mysql-connector-python |

---

# 📂 Project Structure

```text
.
├── llm_agent.py          # Initialize and test the IBM Granite LLM
├── sql_agent.py          # Natural Language SQL Agent
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

### 1. Initialize the Language Model

- Configure IBM Granite using watsonx.ai.
- Define generation parameters.
- Create the LangChain-compatible LLM.

### 2. Connect to the Database

- Configure MySQL connection.
- Connect to the Chinook sample database.

### 3. Create the SQL Agent

- Build a LangChain SQL Agent.
- Enable schema understanding.
- Configure automatic SQL generation and execution.

### 4. Execute Natural Language Queries

- Accept user questions in plain English.
- Generate SQL statements.
- Execute SQL against MySQL.
- Return results as natural language responses.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone <repository-url>

cd natural-language-sql-agent
```

## Create a Virtual Environment

pip install virtualenv 
virtualenv my_env
```

Activate the virtual environment.

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

---

# ⚙ Configure MySQL

Create a MySQL database and import the **Chinook** sample dataset.

Update the database connection details in `sql_agent.py`.

```python
mysql_username = "root"
mysql_password = "<password>"
mysql_host = "<host>"
mysql_port = "3306"
database_name = "Chinook"
```

---

# ▶ Run the Application

## Test the Foundation Model

```bash
python llm_agent.py
```

## Run the SQL Agent

```bash
python sql_agent.py
```

## Query from the Command Line

```bash
python sql_agent.py --prompt "How many albums are there in the database?"
```

```bash
python sql_agent.py --prompt "Which country's customers spent the most by invoice?"
```

---

# 💬 Example Queries

```text
How many albums are there in the database?
```

```text
Describe the PlaylistTrack table.
```

```text
How many employees are there?
```

```text
Which country's customers spent the most by invoice?
```

```text
Can you join the Artist and Album tables and display five artist names with their album IDs?
```

---

# 🎯 Skills Demonstrated

- AI Agents
- Natural Language to SQL (NL2SQL)
- LangChain SQL Agent
- IBM watsonx.ai
- IBM Granite
- Prompt Engineering
- ReAct Agent Pattern
- SQL Query Generation
- Database Integration
- MySQL
- Python Development

---

# 🌟 Key Concepts

- Natural Language Processing
- AI Agents
- Text-to-SQL
- ReAct Reasoning
- SQLDatabase
- Agent Executor
- Enterprise Database Querying
- Large Language Models
- LangChain Agent Framework

---

# 🔮 Future Enhancements

- Support PostgreSQL and SQL Server
- Interactive web interface using Gradio or Streamlit
- Visualize query results with charts and dashboards
- Conversation memory for multi-turn database interactions
- SQL query explanation and optimization suggestions
- Database schema visualization
- Authentication and role-based access control
- Support multiple databases simultaneously
- REST API for external integrations
- Deploy as a cloud-native AI database assistant

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

