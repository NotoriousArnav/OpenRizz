from langchain_groq import ChatGroq

groq = ChatGroq(
    model_name="gemma-7b-it",
    streaming = True
)

llm = groq
