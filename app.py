from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "messages" not in st.session_state:
    st.session_state.messages = []


def document_process(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    # Splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(docs)

    # Embeddings & Vector Store
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vector_db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)

    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True



st.subheader("Document Q&A ChatBot - Ask Anything")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False


# Document upload interface

if not st.session_state.document_uploaded:
    file = st.file_uploader(label="Select Your PDF File", type="pdf")
    if file:
        with open ("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())

        with st.spinner("Proccessing..."):
            document_process("./uploaded_document.pdf")

        st.markdown("Document Proccesssed Successfully...")
        sleep(2)
        st.rerun()       



if st.session_state.document_uploaded and st.session_state.vector_db :
    
    for oneMessage in st.session_state.messages:
        role = oneMessage["role"]
        content = oneMessage["content"]

        st.chat_message(role).markdown(content)

    query = st.chat_input("Ask Anything...")
    if query:
        
        st.session_state.messages.append({"role":"user", "content":query})
        st.chat_message("user").markdown(query)

        documents = st.session_state.vector_db.similarity_search(query, k=2)
        context = ""

        for doc in documents :
            context = context + doc.page_content + "\n\n"


        prompt = f"""
You are an intelligent AI assistant specialized in answering questions from documents.

Your task is to carefully read the provided document context and answer the user's question accurately and clearly.

Instructions:
- Answer ONLY from the provided context.
- If the answer is not available in the context, say:
  "The information is not available in the provided document."
- Keep the answer concise, professional, and well-structured.
- If multiple answers are present, summarize them properly.
- Do not make up information.

Document Context:
{context}

User Question:
{query}

Answer:
"""  
        
        result = llm.invoke(prompt)
        st.session_state.messages.append({"role":"ui", "content":result.content})
        st.chat_message("ai").markdown(result.content)












































# from dotenv import load_dotenv
# load_dotenv()

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_community.vectorstores import InMemoryVectorStore
# import streamlit as st

# # Document Loading
# loader = PyPDFLoader("./Aditya_Munjale_2026.pdf")
# docs = loader.load()


# # Splitting
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# docs = splitter.split_documents(docs)


# # Embeddings & Vector Store
# embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
# vector_db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)

# # User query 
# query = "What is the name of student? & what is his branch?"
# documents = vector_db.similarity_search(query=query, k=2)


# context = ""
# for doc in documents:
#     context = context + doc.page_content + "\n\n"

# prompt = f"""
# You are an intelligent AI assistant specialized in answering questions from documents.

# Your task is to carefully read the provided document context and answer the user's question accurately and clearly.

# Instructions:
# - Answer ONLY from the provided context.
# - If the answer is not available in the context, say:
#   "The information is not available in the provided document."
# - Keep the answer concise, professional, and well-structured.
# - If multiple answers are present, summarize them properly.
# - Do not make up information.

# Document Context:
# {context}

# User Question:
# {query}

# Answer:
# """  

# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# answer = llm.invoke(prompt)




