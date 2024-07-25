from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

def load_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def generate_embeddings(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    return embeddings

def save_faiss_index(embeddings, index_path):
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings))
    faiss.write_index(index, index_path)

if __name__ == "__main__":
    pdf_text = load_text("task1/data/pdfs/extracted_text.txt")
    website_text = load_text("task1/data/websites/website_text.txt")
    youtube_transcript = load_text("task1/data/transcripts/video_transcript.txt")

    texts = [pdf_text, website_text, youtube_transcript]
    embeddings = generate_embeddings(texts)

    save_faiss_index(embeddings, "task1\\data\\embeddings\\faiss_index.index")
