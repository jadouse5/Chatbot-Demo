import streamlit as st
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

model = load_model()

# Function Definitions
def get_input():
    input = st.chat_input("What's on your mind")
    return input

def generate_response(prompt):
    if prompt:  # Ensure there's a prompt to avoid generating from an empty string
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = model(prompt, max_length=50)[0]['generated_text']
        return response
    return ""

def display_response(response):
    with st.chat_message("assistant"):
       st.write(f"Chatbot: {response}")

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

st.sidebar.button('Clear History', on_click=clear_chat_history)


def main():

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages():
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = get_input()
    
    if prompt:
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            display_response(response)

        # Add assistant response to chat history
    st.session_state.messages.append({"role": "user", "content": response})


if __name__ == "__main__":
    main()
