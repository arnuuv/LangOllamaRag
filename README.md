# Restaurant Review Q&A System

A conversational AI system that answers questions about a restaurant based on customer reviews using LangChain, Ollama, and ChromaDB.

## Prerequisites

- Python 3.8+
- Ollama installed and running
- Required Python packages (install via pip):
  ```bash
  pip install langchain-ollama langchain-core chromadb pandas
  ```

## Setup

1. Make sure you have Ollama installed and the following models:

   - llama2 (or another compatible model)
   - mxbai-embed-large (for embeddings)

2. Place your restaurant reviews in `realistic_restaurant_reviews.csv` with the following columns:

   - Title
   - Review
   - Rating
   - Date

3. Run the system:
   ```bash
   python main.py
   ```

## Usage

- The system will prompt you to ask questions about the restaurant
- Type your question and press Enter
- Type 'q' to quit the program

## How it Works

1. Restaurant reviews are stored in a ChromaDB vector database
2. When you ask a question, the system finds the most relevant reviews
3. An LLM (using Ollama) provides a natural, conversational response based on those reviews

## Files

- `main.py`: The main application with the Q&A loop
- `vector.py`: Handles the vector database setup and retrieval
- `realistic_restaurant_reviews.csv`: Contains the restaurant reviews data
