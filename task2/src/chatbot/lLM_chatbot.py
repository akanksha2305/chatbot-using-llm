import openai
from task2.src.utils.vector_db import load_vector_db, retrieve_context

openai.api_key = 'sk-proj-1irQpfPKBkkb9pyQRkAgT3BlbkFJ6UQ4pz7xPxDmshwpindO'  # Ensure the API key is set in the environment variables

def get_chatbot_response(query):
    vector_db = load_vector_db()
    context = retrieve_context(query, vector_db)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Switch to a lower-cost model
            prompt=f"Context: {context}\n\nQ: {query}\nA:",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        return f"Rate limit exceeded: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_sales_agent_response(query):
    vector_db = load_vector_db()
    context = retrieve_context(query, vector_db)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Switch to a lower-cost model
            prompt=f"You are a sales agent. Context: {context}\n\nQ: {query}\nA:",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        return f"Rate limit exceeded: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"