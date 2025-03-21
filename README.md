# Langchain-Projects
# RAG-Based PDF Reader

## 📌 Project Overview
This project is an **AI-powered PDF Reader** that utilizes **Retrieval-Augmented Generation (RAG)** to extract content from PDF documents and generate intelligent responses to user queries. It leverages **Google Gemini AI** for text generation and **FAISS** for efficient document retrieval.

## 🚀 Features
- 📄 **PDF Upload & Text Extraction** using `PyPDFLoader`
- 🔍 **Semantic Search** with FAISS and Google AI embeddings
- 🤖 **RAG-Based Question Answering** using `gemini-1.5-pro`
- 🎯 **Optimized Chunking** for better document understanding
- 🖥️ **User-friendly Interface** powered by `Streamlit`

## 🛠️ Tech Stack
- **Python** (Primary Language)
- **Streamlit** (Frontend UI)
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
Run the application with:
```bash
streamlit run app.py
```

### 📌 How It Works:
1. Upload a PDF file.
2. The system extracts and chunks the text.
3. Enter a query related to the PDF content.
4. The system retrieves relevant chunks and generates an AI-powered response.

## 📷 Screenshot
![App Screenshot](screenshot.png)

## 💡 Future Enhancements
- 🗂️ **Multi-PDF Support**
- 🔍 **Better Chunking Strategy** (Sliding Window, Sentence Splitting)
- 🌍 **Multilingual Support**
- 🎤 **Voice-based Querying**

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests are welcome! If you have suggestions, please open an issue.

## 📩 Contact
For queries, reach out at [your-email@example.com](mailto:your-email@example.com).


