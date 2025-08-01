

from fastapi import FastAPI
from pydantic import BaseModel
import re

from fastapi.middleware.cors import CORSMiddleware
# ✅ Import qa_chain and chat_history from chat_chain.py
from chat_chain import qa_chain, chat_history
# The vector store is loaded within chat_chain.py, so it's not needed directly here.
# from vector_store import load_vector_store

app = FastAPI()

# ✅ Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Safe import for OpenAI RateLimitError
# This handles potential differences in OpenAI library versions
try:
    from openai import RateLimitError
except ImportError:
    # Fallback for older OpenAI library versions if needed
    from openai.error import RateLimitError


class QueryRequest(BaseModel):
    message: str


@app.post("/predict")
def predict(req: QueryRequest):
    query = req.message
    response = qa_chain.invoke({"question": query, "chat_history": chat_history})
    llm_answer = response["answer"]
    source_documents = response["source_documents"]

    # ✅ Extract titles from LLM answer (bullet points or numbered list)
    titles = re.findall(r'\d+\.\s*(.*?)\s*\(\d{4}\)', llm_answer)
    print("Extracted titles:", titles)

    # Build dictionary from vector store results
    movie_map = {}
    for doc in source_documents:
        meta = doc.metadata
        title = meta.get("Series_Title", "Unknown")
        movie_map[title.lower()] = {
            "title": title,
            "year": str(meta.get("Released_Year", "N/A")),
            "poster": meta.get("Poster_Link", ""),
            "summary": meta.get("Overview", ""),
            "genre": meta.get("Genre", "").split(","),
            "actors": [meta.get("Star1", ""), meta.get("Star2", "")]
        }

    # ✅ Merge vector store + fallback placeholders
    movies = []
    for t in titles:
        data = movie_map.get(t.lower())
        if data:
            movies.append(data)
        else:
            # Fallback if not found
            movies.append({
                "title": t,
                "year": "N/A",
                "poster": "",
                "summary": "No details found in database. (From LLM)",
                "genre": ["Romance"],
                "actors": []
            })

    return {
        "movies": movies,
        "answer": llm_answer,
        "chat_history": chat_history
    }