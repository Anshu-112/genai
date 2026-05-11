# 🤖 GenAI Learning Projects

This repository contains my GenAI learning journey and projects built while exploring:

* Large Language Models (LLMs)
* LangChain
* Google Gemini API
* Streamlit
* Embeddings
* AI Chatbots
* Information Extraction Systems

Currently, this repository includes:

1. Basic AI Chatbot
2. Movie Information Extractor

---

# 🚀 Projects Included

## 1. Basic AI Chatbot

A simple chatbot built using LangChain and Gemini API.

### Features

* Conversational AI
* Gemini integration
* Prompt handling
* Basic chat interaction

---

## 2. Movie Information Extractor

An AI-powered information extraction app that extracts structured movie details from paragraphs.

### Features

* Extracts movie information from plain text
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
* Generates a short summary
* Streamlit UI
* Uses Gemini 2.5 Flash model

---

# 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* python-dotenv

---

# 📂 Project Structure

```bash
GENAI/
│
├── chatbot/
├── chatmodels/
├── embeddingsmodels/
├── project2/
│   ├── core.py
│   ├── corewithui.py
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

## 2. Move Into Project Folder

```bash
cd your-repo-name
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
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
GOOGLE_API_KEY=your_api_key_here
```

---

# ▶️ Run Streamlit App

```bash
streamlit run project2/corewithui.py
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
* Add vector databases
* Improve prompt engineering
* Create multi-agent systems
* Add PDF and document understanding
* Improve Streamlit UI design
* Explore open-source LLMs
* Deploy GenAI applications

---

# 👨‍💻 Author

Anshu Varma

---

# ⭐ If you liked this project

Give it a star on GitHub ⭐
