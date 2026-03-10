from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4",temprature=0)

response = model.invoke("What is the capital of India?")

print(response.content)

