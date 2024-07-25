import streamlit as st
from task2.src.chatbot.lLM_chatbot import get_chatbot_response, get_sales_agent_response


def main():
    st.title("Apple Vision Pro Chatbot")

    user_query = st.text_input("Enter your query:")
    
    if st.button("Get Response"):
        if user_query:
            # Call the chatbot response function
            response = get_chatbot_response(user_query)
            st.write("Response:")
            st.write(response)

    if st.button("Get Sales Response"):
        if user_query:
            # Call the sales agent response function
            response = get_sales_agent_response(user_query)
            st.write("Sales Response:")
            st.write(response)

if __name__ == "__main__":
    main()
