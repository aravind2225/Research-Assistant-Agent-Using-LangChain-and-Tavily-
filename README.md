# Research Assistant Agent using LangChain & Tavily

A powerful AI-driven Research Assistant Agent built using LangChain and Tavily that performs intelligent web research, retrieves relevant information in real time, and generates structured responses using Large Language Models (LLMs).

This project demonstrates how autonomous AI agents can combine:
- Web Search
- Real-time Information Retrieval
- Tool Calling
- Multi-step Reasoning
- Execution Tracing
- LangChain Agents
- Tavily Search APIs

to create an advanced research workflow.

Repository:  
https://github.com/aravind2225/Research-Assistant-Agent-Using-LangChain-and-Tavily-

---

# Features

- AI-powered Research Assistant
- Real-time Web Search using Tavily
- Intelligent Query Understanding
- LangChain Agent Architecture
- Tool Calling Support
- Streaming Responses
- Execution Trace Visualization
- Structured Research Output
- Modular and Scalable Codebase
- Beginner-Friendly Project Structure

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| LangChain | Agent Orchestration |
| Tavily | Real-time Web Search |
| OpenAI / Groq / Gemini | Large Language Models |
| Streamlit | Frontend UI |
| dotenv | Environment Variable Management |

---

# Project Architecture

```text
User Query
     ↓
LangChain Agent
     ↓
Tavily Search Tool
     ↓
Web Retrieval
     ↓
LLM Reasoning
     ↓
Structured Research Response
```

---

# Project Structure

```text
Research-Assistant-Agent-Using-LangChain-and-Tavily/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── agents/
│   ├── research_agent.py
│   └── tools.py
│
├── utils/
│   ├── prompts.py
│   ├── helper.py
│   └── tracing.py
│
├── execution_traces/
│
└── assets/
```

---

# How the System Works

The workflow follows an agentic AI architecture:

## Step 1 — User Input

The user asks a research-related question.

Example:

```text
"What are the latest advancements in Generative AI?"
```

---

## Step 2 — LangChain Agent Planning

The LangChain agent:
- Understands the query
- Determines whether web search is needed
- Decides which tool to invoke

---

## Step 3 — Tavily Search Execution

The agent invokes the Tavily Search Tool to retrieve:
- Latest articles
- Trusted sources
- Relevant documents
- Summarized web content

Tavily is specifically designed for AI agents and research workflows.

---

## Step 4 — LLM Reasoning

The LLM:
- Reads retrieved content
- Synthesizes information
- Produces a structured response

---

## Step 5 — Final Research Output

The user receives:
- Well-structured insights
- Context-aware explanations
- Summarized research findings

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/aravind2225/Research-Assistant-Agent-Using-LangChain-and-Tavily-.git
```

```bash
cd Research-Assistant-Agent-Using-LangChain-and-Tavily-
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# Getting API Keys

## OpenAI API Key

Get your API key from:

https://platform.openai.com/api-keys

---

## Tavily API Key

Get your API key from:

https://tavily.com/

---

# Running the Application

## Streamlit App

```bash
streamlit run app.py
```

The application will launch at:

```text
http://localhost:8501
```

---

# Example Queries

You can ask questions like:

```text
What are the latest AI trends in 2026?
```

```text
Summarize recent advancements in Quantum Computing.
```

```text
What are the best open-source LLMs currently available?
```

```text
Research the impact of AI on healthcare.
```

---

# Execution Trace Feature

One of the key highlights of this project is execution tracing.

The tracing system helps developers:
- Monitor tool calls
- Understand agent reasoning
- Debug workflows
- Analyze intermediate steps
- Improve transparency in AI systems

This is especially useful while building:
- Multi-agent systems
- Autonomous AI applications
- Deep research workflows
- Tool-calling architectures

---

# Why Tavily?

Tavily is optimized specifically for AI agents and LLM workflows. It provides:
- AI-friendly search results
- Structured outputs
- Fast retrieval
- Reliable information sources
- Agent-focused APIs

Unlike traditional search engines, Tavily is designed for autonomous reasoning systems.

---

# Why LangChain?

LangChain simplifies:
- Tool calling
- Agent orchestration
- Prompt chaining
- Memory handling
- Multi-step reasoning

It acts as the backbone of the agent workflow.

---

# Future Improvements

Possible enhancements for this project:

- Multi-Agent Collaboration
- Memory-based Conversations
- PDF Report Generation
- RAG (Retrieval-Augmented Generation)
- Vector Database Integration
- LangGraph Integration
- Research Report Export
- Citation Generation
- Voice-based Queries
- Autonomous Research Loops
- Browser Automation
- Knowledge Graph Support

---

# Use Cases

This project can be extended for:

- AI Research Assistants
- Academic Research Tools
- Enterprise Knowledge Systems
- Automated Report Generation
- Market Research Platforms
- Financial Research Agents
- Legal Research Assistants
- Healthcare Information Systems

---

# Learning Outcomes

By building this project, developers can learn:

- LangChain Agents
- Tool Calling
- AI Search Systems
- Prompt Engineering
- LLM Integration
- Autonomous AI Workflows
- Streamlit Development
- AI Agent Architecture
- Execution Tracing
- Real-time Web Retrieval

---

# Screenshots

You can add screenshots inside:

```text
/assets
```

Suggested screenshots:
- Main UI
- Agent Workflow
- Execution Trace
- Search Results
- Final Response Output

---

# Sample Workflow Diagram

```text
+-------------------+
|   User Question   |
+-------------------+
          ↓
+-------------------+
| LangChain Agent   |
+-------------------+
          ↓
+-------------------+
| Tavily Search API |
+-------------------+
          ↓
+-------------------+
| Web Information   |
+-------------------+
          ↓
+-------------------+
| LLM Reasoning     |
+-------------------+
          ↓
+-------------------+
| Final Answer      |
+-------------------+
```

---

# Requirements

Example `requirements.txt`

```txt
langchain
langchain-community
langchain-openai
langchain-core
tavily-python
streamlit
python-dotenv
openai
```

---

# Best Practices

- Keep API keys secure
- Use `.env` files
- Add tracing for debugging
- Modularize agent logic
- Separate prompts from business logic
- Implement caching for repeated searches
- Validate external search results

---

# Troubleshooting

## ModuleNotFoundError

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

## API Key Errors

Ensure:
- API keys are correct
- `.env` file exists
- Environment variables are loaded properly

---

## Streamlit Not Opening

Run:

```bash
streamlit run app.py
```

and manually open:

```text
http://localhost:8501
```

---

# Contributing

Contributions are welcome.

You can contribute by:
- Improving prompts
- Adding new tools
- Enhancing UI
- Optimizing agent workflows
- Adding memory support
- Implementing RAG pipelines

---

# License

This project is licensed under the MIT License.

---

# Author

Developed by:

**Aravind Udiyana**

GitHub:  
https://github.com/aravind2225

---

# References

- https://python.langchain.com/docs/introduction/
- https://docs.tavily.com/
- https://docs.streamlit.io/

---

# Star the Repository

If you found this project useful, consider starring the repository on GitHub.

⭐