import streamlit as st
import huggingface_hub
from transformers import pipeline

# GUI
st.title("💬 Chatbot Demo")

with st.sidebar:
    st.title("💬 Chatbot Demo")
    st.markdown('''
    Author: Jad Tounsi El Azzoiani
    Date: 21/02/2024

    Built using the following:
        - Streamlit
        - HugChat  
    
    ''')

def load_model():
    model = pipeline("text-generation", model="mistralai/Mixtral-8x7B-Instruct-v0.1")
    st.success("Model loaded")
    return model

# Function Definitions
def get_input():
    input = st.chat_input("What's on your mind")
    return input

def generate_response(prompt):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model(prompt)
    return response

def display_response(response):
    with st.chat_message("assistant"):
       st.write(f"Chatbot: {response}")

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear History', on_click=clear_chat_history)


def main():
    
    load_model()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = get_input()
    with st.spinner("Thinking..."):
        response = generate_response(prompt)
    display_response(response)

        # Add assistant response to chat history
    st.session_state.messages.append({"role": "user", "content": response})



main()
