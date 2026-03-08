import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

model = SentenceTransformer("all-MiniLM-L6-v2")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

index = faiss.read_index("quran_index.faiss")

with open("verse_data.pkl", "rb") as f:
    df = pickle.load(f)


def search_quran(query):

    query_embedding = model.encode([query])

    D, I = index.search(query_embedding, k=5)

    results = df.iloc[I[0]]

    context = " ".join(results["translation"].tolist())

    prompt = f"""
Answer the question using Quran verses.

Context:
{context}

Question:
{query}

Answer:
"""

    response = generator(prompt, max_length=200)

    return response[0]["generated_text"], results


if __name__ == "__main__":

    question = input("Ask a question: ")

    answer, verses = search_quran(question)

    print(answer)
    print("\nRelevant Verses:\n")
    print(verses)