# Quran AI Assistant

An AI-powered question answering system that retrieves Quran verses using semantic search and Retrieval-Augmented Generation (RAG).

## Features

• Semantic search across Quran verses  
• AI generated answers  
• Arabic + English verse display  
• FAISS vector database  
• Streamlit dashboard

## Technologies

Python  
FAISS  
Sentence Transformers  
HuggingFace Transformers  
Streamlit  

## Dataset

Quran dataset containing:

- Surah number
- Ayah number
- English translation
- Arabic text

## Installation

pip install -r requirements.txt

## Create embeddings

python src/create_embeddings.py

## Run application

streamlit run dashboard/streamlit_app.py

## Example Question

What does Quran say about patience?

## Project Structure

src/ → AI pipeline  
data/ → dataset  
dashboard/ → UI  

## Author

Zohib Khan# Quran-AI-Assistant
