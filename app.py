import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

os.environ['LANGCHAIN_TRACING_V2']="true"

os.environ['LANGCHAIN_PROJECT'] = "Q&A chatbot project 1"

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistance"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, api_key, llm, temprature, max_tokens):
    openai.api_key=api_key
    llm = ChatOpenAI(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke(question)

    return answer

st.title("Enhanced Q&A Chatbot With OpenAI")

st.sidebar.title("settings")

api_key=st.sidebar.text_input("Enter API key", type="password")

engine=st.sidebar.selectbox("Select OpenAI model", ["gpt-4o", "gpt-4-turbo","gpt-4"])

temprature=st.sidebar.slider("Temprature", min_value=0.1, max_value=1, value=0.1)
max_tokens=st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Ask your question")

user_input=st.text_input("You:")


if user_input and api_key:
    response=generate_response(user_input, api_key, engine, temprature, max_tokens)
    st.write(response)

elif user_input:
    st.write("Please provide the appropriate API key")

else:
    st.write("Please provide the user input")


    