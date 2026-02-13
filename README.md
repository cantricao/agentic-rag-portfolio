# 🤖 Autonomous Agentic RAG & Advanced AI Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Orchestration](https://img.shields.io/badge/Orchestration-CrewAI%20%7C%20LangGraph-orange)](https://www.crewai.com/)
[![Optimization](https://img.shields.io/badge/Fine--Tuning-Unsloth%20%7C%20QLoRA-red)](https://github.com/unslothai/unsloth)
[![Vector DB](https://img.shields.io/badge/Vector%20DB-ChromaDB%20%7C%20SQLite-green)](https://www.trychroma.com/)
[![Status](https://img.shields.io/badge/Status-Production%20Grade-brightgreen)]()

## 📋 Overview
This repository hosts a suite of **Autonomous Agentic RAG (Retrieval-Augmented Generation)** systems and **Advanced LLM Engineering** projects.

Moving beyond simple chatbots, these projects demonstrate **Enterprise-grade AI** capabilities: from optimizing Large Language Models (LLMs) with **Unsloth**, parsing complex documents with **Docling**, to deploying autonomous multi-agent squads (Clinical & Banking) that possess reasoning, memory, and safety checks.

## 🚀 Key Features

* **🧠 Multi-Agent Orchestration:** Deployed autonomous squads (e.g., Banking System, Clinical Team) using **CrewAI** where agents perform specialized roles (Analyst, Risk Manager, Researcher).
* **📚 Advanced Document ETL:** Implemented state-of-the-art parsing using **Docling** to extract complex table structures from PDFs, ensuring high-quality data ingestion for RAG.
* **🛡️ Clinical-Grade Safety:** Engineered a **Multi-layer Memory System** (Memori + SQLite) for healthcare agents to prevent contraindications (e.g., Drug Allergy Checks) and ensure patient data privacy.
* **⚡ Performance Optimization:** Utilized **Semantic Caching** to reduce API latency by 90% and **Unsloth/QLoRA** to fine-tune models on consumer hardware (reduced VRAM by 70%).
* **🌐 Hybrid Information Retrieval:** Seamlessly switches between Internal Knowledge Bases (ChromaDB) and External Tools (Web Search, Calculator).

## 📂 Project Showcase

| File | Project Name | Description |
| :--- | :--- | :--- |
| `05` | **Clinical Decision Support Agent** | 🏥 **Flagship:** A medical agent with **Long-term Memory** & **Semantic Caching** that prevents drug allergies and reduces latency. |
| `01` | **Multi-Agent Banking System** | 🏦 A simulation of autonomous agents (Teller, Risk Officer) coordinating to process loans and detect fraud. |
| `04` | **LLM Finetuning Optimization** | ⚙️ Using **Unsloth & QLoRA** to fine-tune Llama/Gemma models, speeding up training by 2x. |
| `03` | **Advanced PDF Parsing** | 📄 Integrating **Docling** to extract complex table structures/layouts from PDFs for cleaner RAG data. |
| `02` | **RAG Vector Search** | 🔍 A robust baseline for Semantic Search using **ChromaDB** and Embedding models. |

## 🛠️ Tech Stack

* **Core Framework:** Python, CrewAI, LangChain, LangGraph
* **LLM:** Google Gemini 2.5 Flash Lite, Llama 3, Gemma 2
* **Vector Database:** ChromaDB, Custom SQLite (for Caching)
* **Tools:** Unsloth (Fine-tuning), Docling (ETL), Memori (Memory Graph)
* **Environment:** Google Colab / Streamlit

## ⚙️ Architecture (Clinical Agent Example)

The system follows a cyclic, safety-first workflow:

`User Query` -> `Check Semantic Cache` -> `Retrieve Patient Memory` -> `Agent Reasoning (Safety Check)` -> `Generate Answer` -> `Update Memory`

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/cantricao/agentic-rag-portfolio.git](https://github.com/cantricao/agentic-rag-portfolio.git)
    cd agentic-rag-portfolio
    ```

2.  **Install dependencies:**
    ```bash
    pip install crewai chromadb unsloth docling streamlit sentence-transformers
    ```

3.  **Set up Environment Variables:**
    Create a `.env` file or set Colab Secrets:
    ```env
    GEMINI_API_KEY=your_gemini_key
    HF_TOKEN=your_huggingface_token
    ```

4.  **Run the Projects:**
    Open any `.ipynb` file in Jupyter or Google Colab and run the cells.

## 📊 Example Usage (Clinical Scenario)

**Context:** Patient 123 has a recorded history of "Severe Penicillin Allergy".

**Query:** *"Draft a prescription for Amoxicillin 500mg."*

**Agent Workflow:**
1.  *Cache:* Checks for existing protocols (Miss).
2.  *Memory:* Retrieves patient graph: `Allergy: Penicillin`.
3.  *Reasoning:* Identifies Amoxicillin as a Penicillin derivative.
4.  *Output:* **"CONTRAINDICATION WARNING: Patient is allergic to Penicillin. Do not prescribe."**

## 🔮 Future Improvements

* [ ] **Dockerization:** Containerize the Clinical Agent for hospital on-premise deployment.
* [ ] **Voice Interface:** Integrate **VoxCPM** for hands-free doctor notes dictation.
* [ ] **Local Inference:** Optimize the Banking Agent to run entirely offline using **Ollama** on RTX 4090.

## 👨‍💻 About the Author

**Tri**
*Master of Data Analytics (Biomedical Specialization)*

I specialize in building intelligent data pipelines and AI agents that solve real-world problems. With a strong background in data analytics, I focus on **accuracy**, **privacy**, and **scalability** in AI implementation.

---
*Note: This project serves as a portfolio demonstration of Agentic AI capabilities.*