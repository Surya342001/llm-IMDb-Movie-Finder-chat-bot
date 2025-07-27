from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from imdb_loader import load_imdb_data
import os

PERSIST_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")

def create_vector_store():
    df = load_imdb_data()
    texts = df["text"].tolist()
    metadatas = df.to_dict(orient="records")

    # ✅ Use local HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    store = Chroma.from_texts(
        texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory=PERSIST_DIR
    )
    store.persist()
    print("✅ Chroma vector store created and saved!")

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)


# ✅ Run this file directly
if __name__ == "__main__":
    create_vector_store()

    # Test loading
    store = load_vector_store()
    print("📦 Total documents in store:", store._collection.count())

    results = store.similarity_search("romantic drama", k=3)
    print("🔍 Sample results:")
    for r in results:
        print("-", r.metadata.get("title", "No title"))
