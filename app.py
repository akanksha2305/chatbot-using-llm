import streamlit as st
from task2.src.chatbot.lLM_chatbot import get_chatbot_response, get_sales_agent_response

def main():
    st.title("LLM Chatbot")
    user_query = st.text_input("Enter your question:")
    if st.button("Get Response"):
        response = get_chatbot_response(user_query)
        st.write(response)

    st.title("Sales Agent Chatbot")
    user_query = st.text_input("Enter your sales-related question:")
    if st.button("Get Sales Response"):
        response = get_sales_agent_response(user_query)
        st.write(response)

if __name__ == "__main__":
    main()
