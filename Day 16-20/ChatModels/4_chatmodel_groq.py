from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")

response = model.invoke("What is the capital of India?")

print(response.content)