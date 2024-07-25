import faiss
import numpy as np
import os
import pickle
from sentence_transformers import SentenceTransformer

VECTOR_DB_PATH = 'task2/dataknowledge_base/embeddings/faiss_index.index'
DOCUMENTS_PATH = 'task2/data/knowledge_base/documents/documents.pkl'

# Initialize the embedding model
MODEL_NAME = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)

def load_vector_db():
    index = faiss.read_index(VECTOR_DB_PATH)
    return index

def load_documents():
    """Load documents from a pickle file."""
    if not os.path.exists(DOCUMENTS_PATH):
        raise FileNotFoundError(f"Documents file not found at {DOCUMENTS_PATH}")
    with open(DOCUMENTS_PATH, 'rb') as f:
        documents = pickle.load(f)
    return documents

def retrieve_context(query, index):
    """Retrieve relevant context from the FAISS index based on the query."""
    # Convert query to embedding
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=1)
    best_match_idx = indices[0][0]
    
    # Load documents corresponding to the best match index
    documents = load_documents()
    context = documents[best_match_idx]
    
    return context
