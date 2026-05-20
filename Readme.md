# PDF-QnA-Chatbot-with-Gemini

An end-to-end RAG (Retrieval-Augmented Generation) application that allows users to upload PDF documents and ask questions in natural language. The application extracts context from uploaded files and provides accurate, source-based answers using Google Gemini.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🔍 Intelligent document chunking and semantic retrieval
- 🤖 Context-aware answers using Google Gemini
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- ⚡ Fast similarity search using vector embeddings
- 💬 Interactive Streamlit chat interface
- 🗂️ In-memory vector database for efficient retrieval

---

## 🛠️ Tech Stack

- **Python**
- **LangChain** – RAG pipeline framework
- **Google Gemini API** – LLM & embeddings
- **Streamlit** – Frontend UI
- **PyPDFLoader** – PDF document processing
- **InMemoryVectorStore** – Vector database

---

## 📌 Workflow

1. User uploads a PDF document
2. PDF text is extracted using PyPDFLoader
3. Text is split into smaller chunks
4. Gemini embeddings are generated
5. Chunks are stored in a vector database
6. User asks questions in natural language
7. Relevant chunks are retrieved
8. Gemini generates context-aware answers

---

## 📂 Project Structure

```bash
PDF-QnA-Chatbot-with-Gemini/
│
├── app.py
├── requirements.txt
├── .env
├── uploaded_document.pdf
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/PDF-QnA-Chatbot-with-Gemini.git
cd PDF-QnA-Chatbot-with-Gemini
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Mac/Linux

```bash
source env/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Create `.env` File

Create a `.env` file in the root directory and add:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 Example Use Cases

- Research paper Q&A
- Resume analysis chatbot
- Study material assistant
- Company documentation assistant
- Legal/document summarization

---

## 📸 Screenshots

Add your application screenshots here.

---

## 🔮 Future Improvements

- Chat history memory
- Multiple PDF uploads
- Persistent vector database (FAISS/ChromaDB)
- Source citations in answers
- Authentication system
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

Aditya Munjale

---
