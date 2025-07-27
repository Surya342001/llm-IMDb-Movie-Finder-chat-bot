from fastapi import FastAPI
from pydantic import BaseModel
import re

from fastapi.middleware.cors import CORSMiddleware
from vector_store import load_vector_store

app = FastAPI()

# ✅ Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load Chroma vector store once
store = load_vector_store()


class QueryRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(req: QueryRequest):
    query = req.message

    # ✅ Extract 4-digit year from query
    year_match = re.search(r"\b(19\d{2}|20\d{2})\b", query)
    search_year = year_match.group(0) if year_match else None

    results = store.similarity_search(query, k=10)

    seen_titles = set()
    movies = []

    for r in results:
        meta = r.metadata
        title = meta.get("Series_Title", "Unknown")
        year = str(meta.get("Released_Year", "N/A"))

        if search_year and year != search_year:
            continue

        if title in seen_titles:
            continue
        seen_titles.add(title)

        movies.append({
            "title": title,
            "year": year,
            "poster": meta.get("Poster_Link", ""),
            "summary": meta.get("Overview", ""),
            "genre": meta.get("Genre", "").split(",") if meta.get("Genre") else [],
            "actors": [meta.get("Star1", ""), meta.get("Star2", "")]
        })
        
        print("movies ",movies)
        
      

    return {"movies": movies}



