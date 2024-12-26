import streamlit as st
from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize Streamlit app
st.title("Basic LangChain Chatbot with Ollama")

# Ollama setup
def get_ollama_model():
    return Ollama(model="llama3.2")  # Specify the version of Llama

# Set up ConversationChain
def initialize_chain():
    llm = get_ollama_model()
    memory = ConversationBufferMemory()  # Memory for conversation history
    return ConversationChain(llm=llm, memory=memory)

# Initialize the chain
if "chain" not in st.session_state:
    st.session_state.chain = initialize_chain()

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

# Chat response
if user_input:
    response = st.session_state.chain.run(user_input)
    st.write("Chatbot:", response)
