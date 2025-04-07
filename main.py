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

def calculate_average_rating(reviews):
    """Calculate the average rating from retrieved reviews."""
    total = 0
    count = 0
    for review in reviews:
        if 'rating' in review.metadata:
            total += review.metadata['rating']
            count += 1
    return round(total / count, 1) if count > 0 else "No ratings found"

while True:
    print("\n\n---------------------------------")
    question = input("Ask your question (q to quit): ")
    
    print("\n\n---------------------------------") 
    
    if question == "q":
        break
    reviews = retriever.invoke(question)
    
    # Calculate and display average rating
    avg_rating = calculate_average_rating(reviews)
    print(f"Average rating from relevant reviews: {avg_rating}/5")
    
    result = chain.invoke({
        "reviews": reviews,
        "question": question
    })
    print(result)  