import os
import openai
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

def create_embeddings(texts):
    vectorizer = TfidfVectorizer()
    embeddings = vectorizer.fit_transform(texts).toarray()
    return vectorizer, embeddings

def save_embeddings(texts, vectorizer, embeddings, output_path):
    with open(output_path, 'wb') as f:
        pickle.dump({'texts': texts, 'vectorizer': vectorizer, 'embeddings': embeddings}, f)

if __name__ == "__main__":
    openai.api_key ='sk-proj-1irQpfPKBkkb9pyQRkAgT3BlbkFJ6UQ4pz7xPxDmshwpindO'  # Ensure the API key is set in the environment variables

    # Load data from text files
    pdf_text_path = "task1/data/pdfs/extracted_text.txt"
    website_text_path = "task1/data/websites/website_text.txt"
    youtube_transcript_path = "task1/data/transcripts/video_transcript.txt"

    with open(pdf_text_path, 'r') as file:
        pdf_text = file.read()

    with open(website_text_path, 'r', encoding="utf-8") as file:
        website_text = file.read()

    with open(youtube_transcript_path, 'r', encoding="utf-8") as file:
        youtube_text = file.read()

    texts = [pdf_text, website_text, youtube_text]

    # Create and save embeddings
    vectorizer, embeddings = create_embeddings(texts)
    save_embeddings(texts, vectorizer, embeddings, "task2/data/knowledge_base/embeddings/embeddings.pkl")
