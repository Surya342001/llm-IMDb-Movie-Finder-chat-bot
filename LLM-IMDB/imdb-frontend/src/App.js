
import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [chatMessages, setChatMessages] = useState([]);
  const [movieResults, setMovieResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [chatOpen, setChatOpen] = useState(true);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  const handleSendMessage = async () => {
    if (!query.trim()) return;

    const userText = query;
    setChatMessages(prev => [...prev, { type: "user", text: userText }]);
    setQuery("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      const data = await res.json();

      console.log(data,"teh data")
      setMovieResults(data.movies || []);

      if (data.answer) {
        setChatMessages(prev => [...prev, { type: "bot", text: data.answer }]);
      }
    } catch (err) {
      setChatMessages(prev => [...prev, { type: "bot", text: "⚠️ Error: Could not fetch results" }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !loading) handleSendMessage();
  };

  return (
    <div className="app">
    {/* Main content area */}
    <div className="main-content">
      <h1 className="title">Movies</h1>
      <div className="search-bar">
        <input
          type="text"
          placeholder="Hosít your a recommendation movies "
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={handleSendMessage}>🔍</button>
      </div>
  
      <h2 style={{ marginBottom: "20px", fontSize: "20px", color: "#9ca3af" }}>Movies Results</h2>
  
      {movieResults.length > 0 ? (
        <div className="movies-grid">
          {movieResults.map((movie, idx) => (
            <div key={idx} className="movie-card">
              <img src={movie.poster} alt={movie.title} />
              <h2>{movie.title}</h2>
              <p style={{ fontSize: "14px", color: "#9ca3af" }}>{movie.year}</p>
              <p style={{ fontSize: "12px", color: "#d1d5db" }}>{movie.summary}</p>
              <p><strong>Genre:</strong> {movie.genre.join(", ")}</p>
              <p><strong>Actors:</strong> {movie.actors.join(", ")}</p>
            </div>
          ))}
        </div>
      ) : (
        <div className="no-movies">
          <p>👋 Ask me about movies to see recommendations!</p>
        </div>
      )}
    </div>
  
    {/* Static right-side chat */}
    <div className="chat-widget">
      <div className="chat-header">🤖 Ask about movies</div>
      <div className="messages-display">
        {chatMessages.map((msg, i) => (
          <div key={i} className={`chat-message ${msg.type}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="chat-message bot">Typing...</div>}
        <div ref={messagesEndRef}></div>
      </div>
      <div className="input-area">
        <input
          type="text"
          placeholder="Type your question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
          className="chat-input"
        />
        <button onClick={handleSendMessage} className="send-btn">Send</button>
      </div>
    </div>
  </div>
  
  );
}

export default App;
