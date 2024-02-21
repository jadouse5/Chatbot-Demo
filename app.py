import streamlit as st

st.title("Chatbot Demo")

with st.sidebar:
    st.title("Chatbot Demo")
    st.markdown('''
    Author: Jad Tounsi El Azzoiani
    Date: 21/02/2024

    Built using the following:
        - Streamlit
        - HugChat  
    
    ''')


# Function Definitions

'''def generate_response(prompt):
    bot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response'''



# Setting up chat UI
with st.chat_message("user"):
    st.write("Hello human👋") 
    st.write("What can I do for you today?")

prompt = st.chat_input("Say something")

if prompt:
    st.write(f"User: {prompt}")

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input

if prompt := st.chat_input("Message chatbot"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Chatbot: {prompt}"

with st.chat_messages("assistant"):
    st.markdown(response)

st.session_state.messages.append({"role": "user", "content": response})