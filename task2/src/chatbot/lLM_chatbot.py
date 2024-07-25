import openai
from task2.src.utils.vector_db import load_vector_db, retrieve_context

# Load OpenAI API key from environment variable
import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

def get_chatbot_response(user_query):
    """Generate a response using OpenAI GPT-3.5 and the context retrieved from FAISS."""
    index = load_vector_db()
    context = retrieve_context(user_query, index)
    
    # Generate a response using the GPT-3.5 model
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:",
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

def get_sales_agent_response(user_query):
    """Generate a sales-oriented response using OpenAI GPT-3.5 and the context retrieved from FAISS."""
    index = load_vector_db()
    context = retrieve_context(user_query, index)
    
    # Generate a response with a sales focus
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Context: {context}\n\nUser Query: {user_query}\n\nAs a sales agent, respond to the query:",
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
