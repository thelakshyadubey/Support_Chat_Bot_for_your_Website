# Support Chatbot for your Website

**A smart Streamlit web application that uses Sitemap URLs to fetch website data, generate vector embeddings, and enable intelligent querying using LangChain and Pinecone.**

---
---

## 📌 Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [How It Works](#how-it-works)  
- [Author](#author)

---

## 📘 Project Overview

This project enables users to:

- Enter a sitemap-style URL (`sitemap.xml`) of a website.
- Automatically fetch and chunk content using LangChain’s `SitemapLoader`.
- Generate embeddings using **Sentence Transformers**.
- Store and retrieve embeddings using **Pinecone**.
- Ask natural language queries about the website content.
- Get relevant document snippets and links powered by semantic search.

---

## ✨ Features

- 🌐 **Sitemap URL Input** with an example helper button
- 🧠 **Embeddings with Hugging Face Sentence Transformers**
- 🗃️ **Vector Storage with Pinecone**
- 🔍 **Semantic Search** from user-entered queries
- 🧾 **Relevant Document Snippet Display**
- 🎨 **Custom Styled UI** using `style.css` and Streamlit

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/) - UI framework
- [LangChain](https://www.langchain.com/) - LLM orchestration
- [Pinecone](https://www.pinecone.io/) - Vector DB
- [Hugging Face Transformers](https://huggingface.co/) - Sentence Embeddings
- [dotenv](https://pypi.org/project/python-dotenv/) - Environment variable loader

---

## 🧩 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/thelakshyadubey/Support_Chat_Bot_for_your_Website.git
cd Support_Chat_Bot_for_your_Website
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables in a .env file:**
```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name
```

## Usage

1. **Run the app:**
```bash
streamlit run app.py
```

2. **Steps in the app:**
- Enter your sitemap URL (e.g., ```https://www.coursera.org/sitemap~www~resources.xml```)
- Click “Load Data to Pinecone” to process and store vectors.
- Ask a question like: ```What is Coursera's AI course?```
- View the AI-generated response with source links.
   
 ## Folder Structure
 ```text
ai-site-assistant/
├── app.py                # Main Streamlit application
├── utils.py              # Helper functions for loading/splitting/querying
├── style.css             # Custom CSS styles (gradient background, etc.)
├── requirements.txt      # Python dependencies
└── .env                  # Environment variable storage (not committed)
```

## ⚙️ How It Works
1. Data Loading
- SitemapLoader reads links from the sitemap URL and downloads webpage text.

2. Chunking & Embeddings
- LangChain splits the content into manageable chunks.
- Embeddings are created using Hugging Face’s MiniLM model.

3. Vector Indexing
- Embeddings are stored in Pinecone under a defined index name.

4. Semantic Retrieval
- When a user enters a prompt, the top-k relevant document chunks are retrieved from Pinecone.
- Snippets and original source links are displayed.

## 👤 Author
Lakshya Dubey

## Preview
![image](https://github.com/user-attachments/assets/59e58158-6f50-4383-b74a-954faf35eebc)
![image](https://github.com/user-attachments/assets/114d9da6-22bb-43a5-851e-4bb717707f5c)
