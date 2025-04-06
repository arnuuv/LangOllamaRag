from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model = "llama3.2")
template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

Answer the question based on the reviews provided. If the reviews don't contain relevant information, say so.
"""
 
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
  print("\n\n---------------------------------")
  question = input("Ask your question (q to quit): ")
  
  print("\n\n---------------------------------") 
  
  if question == "q":
    break
  reviews = retriever.invoke(question)
  print("Retrieved reviews:", reviews)  # Debug line to see what's being retrieved
  result = chain.invoke({
    "reviews": reviews,
    "question": question
  })
  print(result)  