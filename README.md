# 🤖 GenAI Learning Projects

This repository contains my GenAI learning journey and hands-on projects built while exploring:

* Large Language Models (LLMs)
* LangChain
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* HuggingFace Embeddings
* Google Gemini API
* Mistral AI
* Streamlit
* AI Chatbots
* Information Extraction Systems
* Semantic Search Systems

---

# 🚀 Projects Included

## 1. Basic AI Chatbot

A simple conversational AI chatbot built using LangChain and Gemini API.

### Features

* Conversational AI
* Gemini API integration
* Prompt handling
* Basic chat interaction

---

## 2. Movie Information Extractor

An AI-powered information extraction application that extracts structured movie details from plain text paragraphs.

### Features

* Extracts movie information from unstructured text
* Identifies:

  * Movie Title
  * Genre
  * Release Year
  * Director
  * Cast
  * Story / Plot
  * Main Theme
  * Ratings
  * Notable Features
* Generates concise summaries
* Streamlit UI
* Powered by Gemini 2.5 Flash

---

## 3. 📚 AI PDF Research Assistant (RAG Application)

A professional Retrieval-Augmented Generation (RAG) application that allows users to upload PDFs and ask intelligent questions from the uploaded documents.

### Features

* Upload any PDF document
* Semantic document search
* AI-powered question answering
* ChromaDB vector database integration
* HuggingFace embeddings
* Mistral LLM integration
* Retrieval-Augmented Generation pipeline
* Modern Streamlit UI
* Context-aware responses
* Dynamic document embeddings

### Tech Highlights

* LangChain
* ChromaDB
* HuggingFace Sentence Transformers
* Mistral AI
* Recursive Text Chunking
* Semantic Retrieval
* Vector Embeddings
* Streamlit Frontend

### RAG Workflow

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings Generation
   ↓
Vector Database Storage
   ↓
Semantic Retrieval
   ↓
LLM Response Generation
```

---

# 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Google Gemini API
* Mistral AI
* python-dotenv

---

# 📂 Project Structure

```text
GENAI/
│
├── chatbot/
├── chatmodels/
├── embeddingsmodels/
├── project2/
│   ├── core.py
│   ├── corewithui.py
│
├── RAGProject/
│   ├── app.py
│   ├── create_db.py
│   ├── streamlit_app.py
│   ├── retrievers/
│   ├── document loaders/
│
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
└── main.py
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

---

## 2. Move Into Project Folder

```bash
cd your-repo-name
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
.venv\\Scripts\\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_API_KEY=your_google_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

# ▶️ Run Streamlit Applications

## Movie Information Extractor

```bash
streamlit run project2/corewithui.py
```

---

## AI PDF Research Assistant

```bash
streamlit run RAGProject/streamlit_app.py
```

---

# 🧠 Example Input

```text
Interstellar is a visually stunning science fiction epic directed by Christopher Nolan. Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine.
```

---

# 📄 Example Output

```text
Movie Title: Interstellar
Genre: Science Fiction
Release Year: 2014
Director: Christopher Nolan
Main Cast: Matthew McConaughey, Anne Hathaway
```

---

# 📌 Learning Goals & Future Improvements

* Build advanced RAG applications
* Add hybrid search systems
* Improve prompt engineering
* Create multi-agent AI systems
* Add conversational memory
* Add multi-document RAG support
* Explore open-source LLMs
* Improve Streamlit UI/UX
* Deploy GenAI applications
* Add authentication systems
* Implement source citations
* Build production-ready AI assistants

---

# 👨‍💻 Author

Anshu Varma

---

# ⭐ If You Like This Project

Give it a star on GitHub ⭐
