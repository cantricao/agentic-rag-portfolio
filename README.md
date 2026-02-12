# 🤖 Autonomous Agentic RAG System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange)](https://langchain-ai.github.io/langgraph/)
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)](https://www.trychroma.com/)
[![Status](https://img.shields.io/badge/Status-Prototype-yellow)]()

## 📋 Overview
This project implements an **Autonomous Agentic RAG (Retrieval-Augmented Generation)** system designed to handle complex queries that require multi-step reasoning. Unlike traditional chatbots, this agent can autonomously decide whether to retrieve internal documents, search the web for real-time information, or perform calculations before answering.

The system is built with **LangGraph** for stateful orchestration and uses **ChromaDB** for semantic search, ensuring high precision in information retrieval.

## 🚀 Key Features

* **🧠 Agentic Reasoning:** Utilizes a graph-based architecture (LangGraph) allowing the AI to loop, reason, and self-correct rather than following a linear chain.
* **📚 Advanced RAG:** Implements semantic search over unstructured data (PDFs/Text) using **ChromaDB** vector storage.
* **🌐 Hybrid Information Retrieval:**
    * *Internal Knowledge:* Queries local vector database for proprietary data.
    * *External Knowledge:* Fallback to Web Search when internal data is insufficient.
    * *Function Calling:* Call tools in pre-defined cases.
* **💾 Long-term Memory:** Integrated Mem0 for persistent, long-term user context retention (personalized patient history).
* **🗣️ Voice Interface (Optional):** Modular support for **VoxCPM** for Vietnamese Voice Cloning and Text-to-Speech (TTS).

## 🛠️ Tech Stack

* **Core Framework:** Python, LangChain, LangGraph
* **LLM:** Google Gemini and Grod (Configurable)
* **Vector Database:** ChromaDB
* **Tools:** Python REPL (for math/logic)
* **Environment:** Google Colab

## ⚙️ Architecture

The system follows a cyclic graph workflow:
`User Query` -> `Router` -> `Retrieve (Vector DB)` -> `Grade Documents` -> `Generate Answer` -> `(Loop if Hallucination Detected)` -> `Final Output`

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/cantricao/agentic-rag-portfolio.git](https://github.com/cantricao/agentic-rag-portfolio.git)
    cd agentic-rag-portfolio
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
    Create a `.env` file and add your API keys:
    ```env
    GEMINI_API_KEY=your_gemini_key
    LANGCHAIN_API_KEY=your_langsmith_key  # Optional for tracing
    ```

4.  **Run the Agent:**
    ```bash
    python main.py
    ```

## 📊 Example Usage

**Query:** *"What are the current interest rates in Australia and how do they compare to 2023?"*

**Agent Workflow:**
1.  *Search:* Agent identifies missing internal data.
2.  *Action:* Triggers Web Search tool for "Australia interest rates 2024 vs 2023".
3.  *Reasoning:* Compares retrieved data.
4.  *Output:* Generates a comparative analysis with citations.

## 🔮 Future Improvements

* [ ] **Dockerization:** Containerize the application for easy deployment (in progress).
* [ ] **UI/UX:** Build a frontend interface using **Streamlit**.
* [ ] **Local LLM:** Optimize for offline inference using **Ollama/DeepSeek** on RTX 4090.

## 👨‍💻 About the Author

**Tri**
*Master of Data Analytics (Biomedical Specialization)*

I specialize in building intelligent data pipelines and AI agents that solve real-world problems. With a strong background in data analytics, I focus on accuracy, privacy, and scalability in AI implementation.

---
*Note: This project serves as a portfolio demonstration of Agentic AI capabilities.*
