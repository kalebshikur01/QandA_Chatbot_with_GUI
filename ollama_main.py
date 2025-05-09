import streamlit as st
import openai
from langchain_ollama.llms import OllamaLLM
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

os.environ['LANGCHAIN_TRACING_V2']="true"

os.environ['LANGCHAIN_PROJECT'] = "Q&A chatbot project with Ollama"

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistance"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, llm, temprature, max_tokens):
    llm = OllamaLLM(model='llama3.2:1b')
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke(question)

    return answer

st.title("Enhanced Q&A Chatbot With OpenAI")

st.sidebar.title("settings")

# api_key=st.sidebar.text_input("Enter API key", type="password")

engine=st.sidebar.selectbox("Select Ollama model", ['llama3.2:1b'])

temprature=st.sidebar.slider("Temprature", min_value=0.1, max_value=1.0, value=0.1)
max_tokens=st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Ask your question")

user_input=st.text_input("You:")


if user_input:
    response=generate_response(user_input, engine, temprature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


