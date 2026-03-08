import faiss
import pickle
from sentence_transformers import SentenceTransformer
from src.data_loader import load_quran_data

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings():

    df = load_quran_data()

    texts = df["translation"].tolist()

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, "quran_index.faiss")

    with open("verse_data.pkl", "wb") as f:
        pickle.dump(df, f)

    print("Embeddings created successfully")


if __name__ == "__main__":

    create_embeddings()