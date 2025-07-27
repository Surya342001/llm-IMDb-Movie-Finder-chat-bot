from langchain.chains import ConversationalRetrievalChain
# ✅ Changed: Import ChatOllama for local LLMs via Ollama
from langchain_community.chat_models import ChatOllama
from vector_store import load_vector_store

# Removed: from openai import RateLimitError, as we are no longer using OpenAI directly
# Error handling will be more general for local models

vectorstore = load_vector_store()

# ✅ Changed: Use ChatOllama with a local model (e.g., "llama2" or "gemma:2b")
# Make sure you have Ollama installed and the chosen model pulled.
# For example, to use Llama 2: model="llama2"
# For a smaller Gemma model: model="gemma:2b"
# You can find available models on ollama.com/library
chat_model = ChatOllama(model="llama2", temperature=0) # You can change "llama2" to "gemma:2b" or another model

qa_chain = ConversationalRetrievalChain.from_llm(
    chat_model,
    vectorstore.as_retriever(search_kwargs={"k": 5}),  # 🔥 fetch more docs
    return_source_documents=True
)


chat_history = []

def safe_qa(query):
    global chat_history
    try:
        response = qa_chain.invoke({"question": query, "chat_history": chat_history})
        chat_history.append((query, response["answer"]))
        return response["answer"]
    except Exception as e: # Catch a general exception for local LLM issues
        # Provide a user-friendly message for local LLM errors
        return f"⚠️ Error with local LLM: {str(e)}. Please ensure Ollama is running and the '{chat_model.model}' model is pulled."

