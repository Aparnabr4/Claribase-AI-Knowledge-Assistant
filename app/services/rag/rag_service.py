# app/services/rag/rag_service.py
import pickle
from pathlib import Path
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


# Paths for saving vector store + docs
INDEX_PATH = Path("vector_store/faiss_index")
DOCS_PATH = Path("vector_store/documents.pkl")

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Globals
vectorstore: FAISS | None = None
documents: list[str] = []

def load_or_create_index():
    global vectorstore
    if (INDEX_PATH / "index.faiss").exists() and (INDEX_PATH / "index.pkl").exists():
        vectorstore = FAISS.load_local(
            str(INDEX_PATH),
            embedding_model,
            allow_dangerous_deserialization=True
        )
    else:
        # create new index
        documents = [Document(page_content="Initial knowledge base document")]
        vectorstore = FAISS.from_documents(documents, embedding_model)
        vectorstore.save_local(str(INDEX_PATH))


@tool("rag_tool")
def rag_tool(query: str, k: int = 3) -> list[str]:
    """Perform a Retrieval-Augmented Generation (RAG) query.
    Takes a user query, retrieves relevant documents, and returns their text.
    """
    if not documents or not vectorstore:
        return []
    results = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in results]


# Initialize index on import
load_or_create_index()