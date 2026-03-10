from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
    ) 

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.content)