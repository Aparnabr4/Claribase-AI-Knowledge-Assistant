from pydantic import BaseModel, Field
from typing import Optional, List

class SourceDocument(BaseModel):
    title: str
    url: Optional[str]
    snippet: Optional[str]

class QueryResponse(BaseModel):
    answer: str = Field(..., description="Final answer from LLM+RAG")
    sources: Optional[List[SourceDocument]] = Field(None, description="List of documents used")
