from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=""
)

model = ChatHuggingFace(llm=llm)


st.header('Research Tool')

user_query = st.text_input('Enter your query')

if st.button('Summarize'):
    result = model.invoke(user_query)
    st.write(result.content)