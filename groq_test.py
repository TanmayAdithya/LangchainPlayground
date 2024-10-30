from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    streaming=True
)

messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", "Write a poem"),
]
ai_msg = llm.invoke(messages)
ai_msg
print(ai_msg.content)