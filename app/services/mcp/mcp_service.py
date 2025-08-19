# app/services/mcp/mcp_service.py

from typing import List
from app.models.response import SourceDocument, QueryResponse
from app.services.llm.llm_service import llm
from app.services.rag.rag_service import vectorstore
from app.services.email.email_service import send_email_tool
from langchain.chains import RetrievalQA
from langchain.tools import tool

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff"
)

@tool("mcp_tool")
async def mcp_tool(question: str, email: str | None = None, user_id: str | None = None, send_email: bool = True, ) -> QueryResponse:
    """Handle a query via the MCP (Model Context Protocol) service. Returns the processed response based on MCP integration."""
    answer = qa_chain.run(question)
    sources: List[SourceDocument] = []  # Later: attach doc metadata

    if email:
        subject = "ClariBase Answer"
        body = f"Q: {question}\n\nA:\n{answer}"
        await send_email_tool.ainvoke({"to":email, "subject":subject, "body":body})

    return QueryResponse(answer=answer, sources=sources)