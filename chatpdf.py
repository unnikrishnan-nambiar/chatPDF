import streamlit as st
import fitz  # PyMuPDF
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyMuPDFLoader

# Configure Streamlit UI
st.set_page_config(page_title="PDF Bot with RAG", layout="wide")
st.title("📄 PDF Chatbot with RAG (Mistral)")

# Initialize session state
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

# File Upload Section
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.subheader("Processing PDF... ⏳")

    # Save PDF to a temp file
    pdf_path = f"temp_{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load PDF and extract text
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    # Text Chunking
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # Convert to embeddings
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(docs, embeddings)

    # Store vector DB in session
    st.session_state.vector_db = vector_db
    os.remove(pdf_path)  # Cleanup temp file
    st.success("PDF processed successfully! ✅ You can now ask questions.")

# Question Input Section
query = st.text_input("🔎 Ask a question about the PDF:")
if query and st.session_state.vector_db:
    # Load Local LLM via Ollama
    llm = Ollama(model="mistral")

    # Retrieval-based QA
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=st.session_state.vector_db.as_retriever())
    response = qa_chain.run(query)

    st.subheader("🤖 Answer:")
    st.write(response)
