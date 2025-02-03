# 📄 PDF Chatbot with RAG (Mistral)

This project is a **Streamlit-based PDF Chatbot** that leverages **Retrieval-Augmented Generation (RAG)** using FAISS and **Mistral LLM** to provide intelligent answers based on uploaded PDF documents.

## ✨ Features
- Upload a **PDF** and process it into vector embeddings.
- Use **FAISS** for efficient document retrieval.
- **Mistral LLM** via **Ollama** for intelligent question-answering.
- Streamlit UI for a seamless chatbot experience.

## 📥 Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/pdf-chatbot-rag.git
   cd pdf-chatbot-rag
   ```
2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the chatbot locally using Streamlit:
```sh
streamlit run app.py
```

## 📌 Requirements
- Python 3.8+
- Streamlit
- PyMuPDF
- LangChain
- FAISS
- Sentence Transformers
- Ollama

## 🛠 Tech Stack
- **Streamlit** - For the chatbot UI
- **FAISS** - Vector database for efficient search
- **Mistral (Ollama)** - Language Model for responses
- **LangChain** - Framework for building RAG pipelines

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to open issues or submit pull requests to enhance the chatbot!

---
### 🚀 Future Enhancements
- Support for multiple PDF uploads
- UI improvements
- Fine-tuned LLM models for better responses

