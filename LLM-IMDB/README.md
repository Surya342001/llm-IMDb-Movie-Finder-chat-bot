📌 🎥 IMDb Movie Finder (LLM + LangChain + FastAPI)

🚀 Features:
✅ Query movies using natural language
✅ Supports year, genre, and actor filters
✅ Uses LangChain + ChromaDB for semantic search
✅ Conversational memory for follow-up questions

🛠️ Setup Instructions

1️⃣ Activate Conda Environment
👉 You need the correct Python environment to run the backend.

🔹 Run this in your terminal (anywhere):

python -m venv venv
source venv/bin/activate 



conda activate llm-imdb-py311

✅ Why: This ensures you're using Python 3.11 with all required packages for the backend.

🔹 Verify Python version:

python --version

✅ Expected: Python 3.11.x

2️⃣ Setup Backend (FastAPI)
📂 Navigate to backend folder:

cd /Users/surya.prakash1/Downloads/testing 2/LLM-IMDB/backend
🔹 Install Python dependencies:

pip install -r requirements.txt

✅ Why: Installs FastAPI, LangChain, OpenAI SDK, ChromaDB, etc.


🔹 Build the Vector Store (important step):

python vector_store.py

⚠️ If PyTorch gives an error:

pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu
🔹 Start the backend server:

uvicorn main:app --reload --port 8000
✅ Why: Runs the FastAPI backend that processes movie queries.

📌 Keep this terminal window open.

3️⃣ Setup Frontend (React)
📂 Open a new terminal tab/window and navigate to frontend:

cd /Users/surya.prakash1/Downloads/testing 2/LLM-IMDB/imdb-frontend
🔹 Install Node.js dependencies:

npm install
✅ Why: Installs React, Axios, and other frontend libraries.

🔹 Start the React app:

npm start
✅ Why: Runs the web interface to interact with the backend.

4️⃣ Test the App
Open: http://localhost:3000 in your browser
Try example queries:
Show me some comedy movies
Movies with Leonardo DiCaprio
Best action thrillers with Keanu Reeves
📌 Folder & Command Summary

Activate Environment: (Anywhere)
conda activate llm-imdb-py311
Backend: (LLM-IMDB/backend)
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
Frontend: (LLM-IMDB/imdb-frontend)
npm install
npm start
🔍 Why install these?

FastAPI → Backend server for API requests.
LangChain → LLM orchestration for movie queries.
OpenAI → Uses GPT model to understand questions.
ChromaDB → Stores and retrieves movie embeddings.
React → Frontend UI for user interaction.






# ✅ Example Queries You Can Type
# These work without any code changes, assuming you're using basic similarity_search():

# 🎭 By Genre
# "Show me some comedy movies"

# "Find thriller films"

# "List top romantic movies"

# 👤 By Actor / Star
# "Movies with Leonardo DiCaprio"

# "Show films starring Natalie Portman"

# 🎬 By Director (if available in metadata — check your dataset)
# "Movies directed by Christopher Nolan" (Only if director info is part of the text)

# 🧠 By Plot/Theme
# "Time travel science fiction movies"

# "Movies about survival in space"

# "Psychological thrillers with a twist ending"

# 🗓️ By Time/Year
# "Movies released after 2015" (Only works well if year info is embedded in text — you can add it if not)

# 🔁 Combination Filters
# "Romantic dramas with Tom Hanks"

# "Best action thrillers with Keanu Reeves"

# "Underrated war movies"

