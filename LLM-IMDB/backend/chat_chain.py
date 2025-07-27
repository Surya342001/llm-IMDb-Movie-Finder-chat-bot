from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from vector_store import load_vector_store
from openai.error import RateLimitError

vectorstore = load_vector_store()
chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

qa_chain = ConversationalRetrievalChain.from_llm(
    chat_model,
    vectorstore.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True
)

chat_history = []

def safe_qa(query):
    global chat_history
    try:
        response = qa_chain({"question": query, "chat_history": chat_history})
        chat_history.append((query, response["answer"]))
        return response["answer"]
    except RateLimitError:
        return "⚠️ OpenAI API quota exceeded. Please check your API key or try again later."
