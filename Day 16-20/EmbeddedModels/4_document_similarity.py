from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = [
       "Sachin Tendulkar is known as the “God of Cricket” in India.",

       "India national cricket team is one of the strongest teams in world cricket.",

       "Virat Kohli is famous for his aggressive batting and leadership.",

       "MS Dhoni led India to victory in the 2011 Cricket World Cup.",

       "Cricket is the most popular sport in India."
]

query = "Tell me about MS DHONI"

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index, score = (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

print(query)
print(document[index])
print("Similarity scroe is:",score)


