# 🧠 AskMyDocs  
### Your intelligent document assistant powered by RAG + LangChain

---

## ✨ Overview

**AskMyDocs** is an AI-powered assistant that answers questions based on your own documents.

Instead of relying on generic knowledge, it uses a **Retrieval-Augmented Generation (RAG)** pipeline to search through a custom knowledge base and generate grounded, context-aware responses.

💡 Think of it as:
> “ChatGPT, but trained on your documents — instantly and without fine-tuning.”

---

## 🚀 What this project does

- 📂 Loads documents from multiple formats (TXT, PDF, DOCX)  
- ✂️ Splits content into smaller chunks for better understanding  
- 🧠 Converts text into embeddings (vector representations)  
- 🗃️ Stores embeddings in a vector database (Chroma)  
- 🔍 Retrieves the most relevant information based on a query  
- 💬 Generates answers using an LLM grounded in retrieved context  

---

## 🧩 How it works (RAG Pipeline)

```text
User Question
      ↓
Embedding
      ↓
Vector Search (Chroma)
      ↓
Top-K Relevant Chunks
      ↓
LLM (with context)
      ↓
Final Answer
```

---

## 🏗️ Project Structure

```text
ask-my-docs/
│
├── app/
│   ├── loaders.py        # Load documents (TXT, PDF, DOCX)
│   ├── splitter.py       # Split documents into chunks
│   ├── embeddings.py     # Embeddings model (Azure OpenAI)
│   ├── vectorstore.py    # Vector database (Chroma)
│   ├── retriever.py      # Search logic (similarity / MMR)
│   ├── prompts.py        # Prompt templates
│   ├── chains.py         # LCEL pipelines
│   ├── parsers.py        # Output formatting
│   └── config.py         # Environment/config handling
│
├── data/
│   ├── raw/              # Source documents
│   └── chroma/           # Persisted vector database
│
├── scripts/
│   ├── run_indexing.py   # Build vector index
│   └── run_query.py      # Ask questions
│
├── tests/
│   └── test_queries.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

* 🐍 **Python**
* 🔗 **LangChain (LCEL)**
* 🧠 **Azure OpenAI (Embeddings + LLM)**
* 🗃️ **Chroma Vector Database**
* 📄 **PyPDFLoader / Docx2txtLoader**
* 📦 **dotenv**

---

## 🧠 Key Concepts Applied

* Retrieval-Augmented Generation (RAG)
* Semantic Search with Embeddings
* Vector Databases
* Prompt Engineering
* Structured Outputs (Parsers)
* LCEL (LangChain Expression Language)
* Modular AI Pipelines

---

## 📂 Supported Document Types

* `.txt`
* `.pdf`
* `.docx`

---

## ☁️ Azure OpenAI Service (costs) + Free alternatives

This project is configured to use **Azure OpenAI Service** for both embeddings and answer generation. In practice, **Azure OpenAI is typically a paid, usage-based service** (token-based billing), so you should expect costs when indexing documents and querying.

If you want a **free** option, the most common approach is to run everything **locally** with open-source models:

### Option A: 100% local RAG with Ollama (free)

Run the entire RAG pipeline locally, without external APIs.

- **LLM**: local chat model (e.g., Llama 3, Mistral)
- **Embeddings**: local embedding model (e.g., `nomic-embed-text`)
- **Vector DB**: Chroma (local)

Example setup:

```bash
# Install Ollama (see Ollama docs for your OS), then pull models:
ollama pull nomic-embed-text
ollama pull llama3
```

### Option B: Local embeddings with Sentence-Transformers

Use local embedding models while keeping your LLM provider flexible.

- **Embeddings**: Sentence-Transformers (e.g., BGE, MiniLM)
- **LLM**: Azure OpenAI, OpenAI, or local (Ollama)
- **Vector DB**: Chroma

This setup reduces costs while maintaining good retrieval quality.
---

## ▶️ How to run (coming soon)

Steps will include:

1. Add documents to `data/raw/`
2. Run indexing script
3. Ask questions via CLI or API

---

## 💡 Why this matters

Large Language Models are powerful — but limited by static knowledge.

This project demonstrates how to:

* connect LLMs to real, dynamic data
* reduce hallucinations
* build production-ready AI systems
* structure scalable RAG pipelines

---

## 🛣️ Future Improvements

* 🔄 Streaming responses
* 📊 Retrieval comparison (Similarity vs MMR)
* 🧾 Structured JSON outputs
* 🌐 API with FastAPI
* 🖥️ UI (Streamlit or Web App)
* 🔍 Metadata filtering

---

## 📌 Final Note

This project focuses on building a **clean, modular, and extensible RAG architecture**, following modern best practices used in real-world AI applications.

---

💬 *“Good AI doesn't just generate answers — it knows where they come from.”*

