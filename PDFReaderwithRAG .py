from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.schema import HumanMessage, AIMessage, SystemMessage, ChatMessage
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

from langchain.vectorstores import FAISS
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])


def pdfloader(pdf_file):
    if pdf_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.read())

        # Load PDF file using PyPDFLoader
        loader = PyPDFLoader("temp.pdf")
        documents = loader.load()

        # Extract text from documents
        text = "\n".join([doc.page_content for doc in documents])
        return text


# Call the function only if a file is uploaded
if pdf_file:
    text = pdfloader(pdf_file)

    if text:
        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=30,
            chunk_overlap=5
        )
        chunks = splitter.split_text(text)

        # Display chunks
        st.write(chunks)
        # Create embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.from_texts(chunks, embeddings)

        st.success("FAISS index created!")

        # Search interface
        query = st.text_input("Enter a search query:")
        retrived_text=""
        if query:
            search_results = vectorstore.similarity_search(query, k=5)  # Retrieve top 5 matches
            st.write("Result:")
            for result in search_results:
                retrived_text=retrived_text+result.page_content
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful RAG assistant."),
                ("human", f"this is retrived text  {retrived_text}& this is query {query}")
            ])

            formatted_prompt = prompt.format(retrived_text=retrived_text,query=query)
            result=model.invoke(formatted_prompt)
            st.write(result.content)