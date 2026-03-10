from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620")

response = model.invoke("What is the capital of India?")

print(response.content)
