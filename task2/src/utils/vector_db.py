import os
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

VECTOR_DB_PATH = 'task2/data/knowledge_base/embeddings/embeddings.pkl'

def load_vector_db():
    if not os.path.exists(VECTOR_DB_PATH):
        raise FileNotFoundError(f"Vector database not found at {VECTOR_DB_PATH}")
    with open(VECTOR_DB_PATH, 'rb') as f:
        vector_db = pickle.load(f)
    return vector_db

def retrieve_context(query, vector_db):
    vectorizer = vector_db['vectorizer']
    embeddings = vector_db['embeddings']
    texts = vector_db['texts']

    query_embedding = vectorizer.transform([query]).toarray()
    similarities = cosine_similarity(query_embedding, embeddings)
    best_match_idx = np.argmax(similarities)
    context = texts[best_match_idx]
    
    return context
