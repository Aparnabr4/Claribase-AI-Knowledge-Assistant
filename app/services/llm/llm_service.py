import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool

load_dotenv()

LLM_MODEL = "llama3-8b-8192"

# LangChain Groq LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=LLM_MODEL,
    temperature=0.2
)

@tool("answer_tool")
def answer_tool(question: str, context_docs: list[str]) -> str:
    """Answer a user question using the LLM. The tool takes a `question` and an optional `context` string, then generates an accurate answer using the LLM."""
    context = "\n".join(context_docs)
    template = """You are ClariBase, an enterprise knowledge assistant. Use ONLY the provided context to answer the question.If the answer is not in the context, say "I don't know."
    Context: {context}
    Question: {question}"""

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    response = chain.invoke({"context": context, "question": question})
    return response.content.strip()
