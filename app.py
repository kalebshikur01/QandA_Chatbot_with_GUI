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