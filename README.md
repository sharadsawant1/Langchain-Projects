

# PDF QA System with RAG

## 📌 Project Overview
This project is a **PDF QA System** that leverages **Retrieval-Augmented Generation (RAG)** to extract content from PDF documents and provide intelligent answers to user questions. It integrates **Google Gemini AI** for text generation and **FAISS** for efficient document retrieval.

## 🚀 Features
- 📄 **PDF Upload & Text Extraction** using `PyPDFLoader`
- 🔍 **Semantic Search** powered by FAISS and Google AI embeddings
- 🤖 **RAG-Based Question Answering** with `gemini-1.5-pro`
- 🎯 **Optimized Chunking** for enhanced document comprehension
- 🖥️ **User-Friendly Interface** built with `Streamlit`

## 🛠️ Tech Stack
- **Python** (Core Language)
- **Streamlit** (Frontend Interface)
- **LangChain** (AI Framework)
- **Google Generative AI** (`gemini-1.5-pro` for LLM, `embedding-001` for embeddings)
- **FAISS** (Vector Database)
- **PyPDFLoader** (PDF Text Extraction)
- **dotenv** (Environment Variable Management)

## 📥 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/rag-pdf-reader.git
cd rag-pdf-reader
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your-google-api-key
```

## ▶️ Usage
Launch the application with:
```bash
streamlit run app.py
```

### 📌 How It Works:
1. Upload a PDF file.
2. The system extracts and segments the text into chunks.
3. Ask a question related to the PDF content.
4. The system retrieves relevant text chunks and delivers an AI-generated response.

## 💡 Future Enhancements
- 🗂️ **Support for Multiple PDFs**
- 🔍 **Improved Chunking Techniques** (e.g., Sliding Window, Sentence Splitting)
- 🌍 **Multilingual Capabilities**
- 🎤 **Voice-Activated Queries**

## 🤝 Contributing
Contributions are encouraged! Feel free to submit pull requests or open issues for suggestions.

## 📩 Contact
For questions, contact [your-email@example.com](mailto:swntshrd1@gmail.com).

---
