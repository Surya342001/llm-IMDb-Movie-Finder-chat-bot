📌 🎥 IMDb Movie Finder
A natural language chatbot for querying movies using LangChain, vector search, and a local LLM (Gemma, LLaMA2) served via Ollama.

This project provides a fully local solution for interacting with a movie database using natural language queries, leveraging the power of large language models and vector search for semantic retrieval.

🚀 Features
✅ Query movies using natural language: Ask questions about movies in a conversational style.

✅ Filters by genre, year, actor, etc.: Refine your searches with specific criteria.

✅ LangChain + ChromaDB for semantic retrieval: Intelligent search capabilities based on meaning, not just keywords.

✅ Supports conversational history: The chatbot remembers previous interactions for a more fluid conversation.

✅ Runs fully local: Utilizes Ollama with Gemma or LLaMA2, ensuring your data stays on your machine.

🛠️ Setup Instructions
Follow these steps to get the IMDb Movie Finder up and running on your local machine.

1️⃣ Activate Environment
It's recommended to use a virtual environment to manage dependencies.

Using venv:

<------- Activate venv environment ----->

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Or if using Conda:

<------- Create and activate Conda environment ----->

conda create -n llm-imdb-py311 python=3.11 -y
conda activate llm-imdb-py311

✅ This ensures you're using Python 3.11+ with correct dependencies.

2️⃣ Install Python Dependencies (Backend)
Navigate into the backend directory and install the required libraries.

<------- Change directory to backend and install requirements ----->

cd LLM-IMDB/backend
pip install -r requirements.txt

If you need a CPU-only PyTorch installation (e.g., if you don't have a compatible GPU):

<------- Install PyTorch CPU-only ----->

pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

3️⃣ Setup Vector Store (Run Once)
This step builds and saves the vector database from the movies.csv file. This process converts movie data into embeddings for efficient semantic search.

<------- Run IMDb data loader ----->

python imdb_loader.py

✅ This step converts movie data into embeddings using sentence-transformers.

4️⃣ Set Up Ollama (Local LLM Server)
Ollama is used to run the large language model locally.

Install Ollama:

macOS:

<------- Install Ollama on macOS ----->

brew install ollama

Ubuntu:

<------- Install Ollama on Ubuntu ----->

curl -fsSL https://ollama.com/install.sh | sh

Start the Ollama server (in a separate terminal and keep it running):

<------- Start Ollama server ----->

ollama serve

If port 11434 is already in use, Ollama is likely already running.

Pull a supported model (e.g., Gemma or LLaMA2). This will download the model to your machine:

<------- Pull Gemma 2b model ----->

ollama run gemma:2b

or

<------- Pull LLaMA2 model ----->

ollama run llama2

✅ This step downloads the local LLM that will be used for generating answers.

5️⃣ Run the Backend (FastAPI + LangChain + Ollama)
Start the FastAPI backend server. This will expose the chatbot via REST APIs.

<------- Start backend server ----->

uvicorn main:app --reload --port 8000

By default, your backend will be running at: http://127.0.0.1:8000

✅ This serves the movie chatbot via REST APIs using a LangChain ConversationalRetrievalChain.

6️⃣ Start Frontend (React)
In a new terminal, navigate to the frontend directory and start the React development server.

<------- Change directory to frontend and install npm packages ----->

cd LLM-IMDB/imdb-frontend
npm install

<------- Start React frontend development server ----->

npm start

Visit: http://localhost:3000

✅ Example Queries
Here are some example queries you can try with the chatbot:

"Show me some comedy movies"

"Movies with Leonardo DiCaprio"

"Psychological thrillers with a twist ending"

"Best action thrillers with Keanu Reeves"

"Romantic dramas with Tom Hanks"

"Movies released after 2015"

✅ These queries are semantically matched using LangChain + ChromaDB.

🧠 How to Switch LLM Models (Ollama)
You can easily switch the Large Language Model used by the backend.

In query_processor.py, locate the following line:

<------- ChatOllama model configuration ----->

chat_model = ChatOllama(model="gemma:2b", temperature=0)

You can change "gemma:2b" to any other supported Ollama model. Some popular options include:

"llama2"

"gemma:2b-it"![Uploading recommendation.mp4 (online-video-cutter.com).gif…]()


Or explore more models from the Ollama Librar
![recommendation mp4 (online-video-cutter com)](https://github.com/user-attachments/assets/3404eaf2-6d7f-48cc-b723-a2ca615348f1)
