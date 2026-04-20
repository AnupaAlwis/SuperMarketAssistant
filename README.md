# 🛒 Supermarket Agentic AI Chatbot

## 📌 Description

This project is an **Agentic AI-powered chatbot** designed for a supermarket web application.
It allows users to ask natural language questions about products, and the system intelligently retrieves answers using both structured and semantic data.

The chatbot is built using a **hybrid architecture** combining:

* SQL-based querying (for precise data like price and stock)
* Retrieval-Augmented Generation (RAG) (for semantic understanding and recommendations)
* Local Large Language Models (LLMs) running via Ollama (no API cost)

---

## 🚀 What This Project Does

This chatbot acts as an **AI shopping assistant** that can:

### 🟢 Handle structured queries (via SQL)

* Get product prices
* Check stock availability
* Filter products by supplier
* Answer database-specific questions

**Example:**

> What is the price of Anchor milk?

---

### 🔵 Handle semantic queries (via RAG)

* Recommend products
* Answer based on descriptions
* Understand fuzzy queries

**Example:**

> Suggest healthy snacks

---

### 🟣 Handle hybrid queries (SQL + RAG)

* Combine reasoning and filtering

**Example:**

> Suggest healthy snacks under Rs. 300

---

### 🧠 Maintain conversation memory

* Understand follow-up questions

**Example:**

> Do you have milk?
> What is the price?

---

## 🏗️ Architecture

```
User Query
    ↓
Agent (LLM - Ollama)
    ↓
Tools:
   ├── SQL Tool (MySQL)
   └── RAG Tool (Chroma Vector DB)
    ↓
Memory (Conversation History)
    ↓
Final Response
```

---

## 🧰 Tech Stack

* **LLM:** Ollama (LLaMA 3)
* **Framework:** LangChain
* **Database:** MySQL
* **Vector Database:** Chroma
* **Embeddings:** Sentence Transformers
* **Language:** Python

---

## 📁 Project Structure

```
supermarket-agent/
│
├── main.py          # Entry point
├── agent.py         # Agent setup
├── tools.py         # Tool definitions (SQL + RAG)
├── db.py            # MySQL connection & SQL chain
├── rag.py           # RAG pipeline (Chroma)
├── config.py        # Configurations
├── requirements.txt
└── chroma_db/       # Vector DB (auto-generated)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/supermarket-agent.git
cd supermarket-agent
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama (required)

Download and install from:
👉 https://ollama.com

Then pull the model:

```bash
ollama pull llama3
```

---

### 4️⃣ Configure MySQL

Update `config.py`:

```python
DB_URI = "mysql+pymysql://username:password@localhost/supermarket"
```

Make sure your database has a table like:

| id | name | price | stock | supplier | description |

---

### 5️⃣ Run the project

```bash
python main.py
```

---

### ⚠️ First Run Only

On the first run, the system builds the vector database:

```python
setup()
```

After that:
👉 Comment it out in `main.py` to improve performance.

---

## 🧪 Example Queries

Try asking:

* What is the price of milk?
* Do you have rice in stock?
* Suggest healthy snacks
* Cheap drinks under 300

---

## 💡 Features

* ✅ Fully local (no API cost)
* ✅ Agentic AI (tool-based reasoning)
* ✅ Hybrid SQL + RAG system
* ✅ Persistent vector database (Chroma)
* ✅ Conversational memory

---

## ⚠️ Limitations

* Local LLMs may be slower than cloud models
* SQL generation may require prompt tuning
* Requires proper database schema design

---

## 🚀 Future Improvements

* Web frontend integration (React)
* Add shopping cart functionality
* Improve recommendation accuracy
* Deploy as an API (FastAPI)
* Add multilingual support

---

## 📄 License

This project is for educational and development purposes.

---

## 🙌 Acknowledgements

* LangChain
* Ollama
* Sentence Transformers
* Chroma

---
