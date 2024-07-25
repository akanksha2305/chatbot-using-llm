from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle
import os

# Define paths
PDF_TEXT = "task1\data\pdfs\extracted_text.txt"
WEBSITE_TEXT = "task1\data\websites\website_text.txt"
YOUTUBE_TEXT = "task1\data\transcripts\video_transcript.txt"

DOCUMENTS = [PDF_TEXT, WEBSITE_TEXT, YOUTUBE_TEXT]
VECTOR_DB_PATH = 'data/knowledge_base/embeddings/faiss_index.index'
DOCUMENTS_PATH = 'data/knowledge_base/documents/documents.pkl'

# Initialize the embedding model
MODEL_NAME = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)

# Generate embeddings
embeddings = model.encode(DOCUMENTS)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # Using L2 distance
index.add(embeddings)  # Add embeddings to the index

# Save the FAISS index
os.makedirs(os.path.dirname(VECTOR_DB_PATH), exist_ok=True)
faiss.write_index(index, VECTOR_DB_PATH)

# Save the documents
os.makedirs(os.path.dirname(DOCUMENTS_PATH), exist_ok=True)
with open(DOCUMENTS_PATH, 'wb') as f:
    pickle.dump(DOCUMENTS, f)

print("FAISS index and documents saved successfully.")
