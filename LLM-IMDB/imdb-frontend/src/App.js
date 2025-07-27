import React, { useState } from "react";
import "./App.css"; // ✅ custom CSS


function App() {
  const [query, setQuery] = useState("");
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: query }),
      });
      

      const data = await res.json();
      setMovies(data.movies || []);
    } catch (err) {
      console.error("Error fetching movies", err);
    }

    setLoading(false);
  };
  const uniqueMovies = movies.filter(
    (movie, index, self) =>
      index === self.findIndex((m) => m.title === movie.title)
  );
  
  return (
    <div className="app">
      <h1 className="title">🎥 IMDb Movie Finder</h1>

      <div className="search-container">
        <input
          type="text"
          placeholder="Describe a movie (e.g. sci-fi with robots)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-box"
        />
        <button onClick={handleSearch} className="search-btn">Search</button>
      </div>

      {loading && <p className="loading">🔍 Searching movies...</p>}
     

      <div className="movies-grid">
  {uniqueMovies.map((movie, idx) => (
    <div key={idx} className="movie-card">
      <h2>{movie.title}</h2>
      <p className="year">{movie.year}</p>
      {movie.poster && <img src={movie.poster} alt={movie.title} />}
      <p className="summary">{movie.summary}</p>
      <p><strong>Genre:</strong> {movie.genre.join(", ")}</p>
      <p><strong>Actors:</strong> {movie.actors.join(", ")}</p>
    </div>
  ))}
</div>
{/* <div className="movies-grid">
  {uniqueMovies.map((movie, idx) => (
    <MovieCard key={idx} movie={movie} />
  ))}
</div> */}
    </div>
  );
}

export default App;

