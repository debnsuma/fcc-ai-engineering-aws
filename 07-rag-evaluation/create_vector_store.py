from langchain_community.document_loaders import BSHTMLLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
import os

def create_vector_store():
    # Create output directory if it doesn't exist
    os.makedirs("07-rag-evaluation/vector_store", exist_ok=True)
    
    # Load the HTML file
    loader = BSHTMLLoader("07-rag-evaluation/data/2023WC.html")
    data = loader.load()
    
    # Split the text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(data)
    
    # Initialize embeddings
    embeddings = BedrockEmbeddings(model_id='amazon.titan-embed-text-v2:0')
    
    # Create FAISS vector store
    db = FAISS.from_documents(chunks, embeddings)
    
    # Save the vector store
    db.save_local("07-rag-evaluation/vector_store", "CWC_index")
    print("Vector store created successfully!")

if __name__ == "__main__":
    create_vector_store() 