import streamlit as st
from ollama import chat

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

def process_input():
    if prompt := st.chat_input(placeholder="Enter your query here..."):

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            response = chat(model='llama3.2:1b', messages=[{"role": "user", "content": prompt}])
            ai_response = response['message']['content']
        except Exception as e:
            ai_response = f"Error: {str(e)}"

        st.session_state.messages.append({"role": "ai", "content": ai_response})
        with st.chat_message("ai"):
            st.markdown(ai_response)

def main():
    st.title("CHATBOT")
    initialize_session_state()
    display_messages()
    process_input()


if __name__ == "__main__":  
    main()
