from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model = "llama3.2")
template = """
You are a friendly restaurant critic helping customers understand the restaurant based on real customer reviews.

Reviews to consider:
{reviews}

Customer question: {question}

Provide a conversational response based on these reviews. Be specific about what customers liked or disliked, but write naturally as if you're having a conversation. Avoid mentioning that these are reviews or documents - just share the information as if you're knowledgeable about the restaurant.
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
    result = chain.invoke({
        "reviews": reviews,
        "question": question
    })
    print(result)  