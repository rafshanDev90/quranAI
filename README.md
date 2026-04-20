<div align="center">
  <img src="https://img.icons8.com/color/96/000000/quran.png" alt="Bayyan AI Logo" width="80" height="80" />
  <h1>📖 Bayyan AI</h1>
  <p><strong>A Specialized Quranic Scholar Assistant using RAG (Retrieval-Augmented Generation)</strong></p>

  <p>
    <a href="https://github.com/rafshandev/bayyan-ai/stargazers"><img src="https://img.shields.io/github/stars/rafshandev/bayyan-ai?style=for-the-badge" alt="Stars" /></a>
    <a href="https://github.com/rafshandev/bayyan-ai/network/members"><img src="https://img.shields.io/github/forks/rafshandev/bayyan-ai?style=for-the-badge" alt="Forks" /></a>
    <a href="https://github.com/rafshandev/bayyan-ai/issues"><img src="https://img.shields.io/github/issues/rafshandev/bayyan-ai?style=for-the-badge" alt="Issues" /></a>
    <a href="https://github.com/rafshandev/bayyan-ai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/rafshandev/bayyan-ai?style=for-the-badge" alt="License" /></a>
  </p>
</div>

<hr />

## 🌟 Overview

**Bayyan AI** is an intelligent Quranic search and assistant platform built with modern AI technologies. It leverages **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers to questions about the Quran, ensuring every response is backed by authentic verses with citations.

### 🚀 Key Features
- **Semantic Search:** Find verses based on meaning, not just keywords.
- **RAG-Powered Answers:** Get direct answers synthesized from Quranic context using LLMs.
- **Strict Citations:** Every claim includes Surah name, number, and Ayah reference.
- **Multilingual Support:** Displays both Arabic text and English translations.
- **Session Memory:** Remembers conversation history using Redis.

---

## 🛠️ Tech Stack

<table align="center">
  <tr>
    <td align="center" width="150">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
      <br />Python
    </td>
    <td align="center" width="150">
      <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="fastapi" width="60" height="40" style="object-fit: contain;"/>
      <br />FastAPI
    </td>
    <td align="center" width="150">
      <img src="https://avatars.githubusercontent.com/u/104526978?s=200&v=4" alt="chromadb" width="40" height="40"/>
      <br />ChromaDB
    </td>
    <td align="center" width="150">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" alt="mongodb" width="40" height="40"/>
      <br />MongoDB
    </td>
    <td align="center" width="150">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original.svg" alt="redis" width="40" height="40"/>
      <br />Redis
    </td>
  </tr>
</table>

- **Core Framework:** FastAPI (Backend API)
- **Vector Database:** ChromaDB (Vector Search)
- **Primary Database:** MongoDB (Source Quranic Data)
- **LLM Orchestration:** LangChain + Groq (Llama 3.1)
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)

---

## 📁 Project Structure

```text
bayyan-AI/
├── bot/                # Telegram Bot (Node.js)
│   ├── commands/        # Modular command handlers (start, help, query)
│   ├── utils/           # Utility functions (logger, etc.)
│   ├── index.js         # Bot entry point
│   └── package.json     # Node.js dependencies
├── src/
│   ├── main.py          # FastAPI entry point & API routes
│   ├── orchestrator.py  # RAG logic & LLM chain configuration
│   ├── preprocess.py    # Data ingestion from MongoDB to ChromaDB
│   └── search.py        # Vector search implementation
├── quran_vectordb/      # Local vector database storage
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables configuration
```

---

## ⚙️ Getting Started

### 1. Prerequisites
- Python 3.9+
- MongoDB instance
- Redis instance (optional for session history)
- Groq API Key

### 2. Installation
```bash
git clone https://github.com/rafshandev/bayyan-ai.git
cd bayyan-ai
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
# Backend Config
MONGO_URI=your_mongodb_uri
GROQ_API_KEY=your_groq_api_key
REDIS_URL=your_redis_url

# Telegram Bot Config
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
BAYYAN_API_URL=http://localhost:8000
```

### 4. Running the Telegram Bot
In a new terminal:
```bash
cd bot
npm install
node index.js
```

### 4. Data Ingestion
Vectorize the Quranic data from MongoDB:
```bash
python src/preprocess.py
```

### 5. Running the API
```bash
uvicorn src.main:app --reload
```
The API will be available at `http://localhost:8000`.

---

## 🛰️ API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Welcome message |
| `GET` | `/search?q={query}` | Get AI-generated answer and relevant verses |

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the [MIT License](LICENSE).

<div align="center">
  <sub>Built with ❤️ for the Ummah</sub>
</div>
