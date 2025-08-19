from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(..., description="User's question or request")
    context: str | None = Field(None, description="Optional context to guide the answer")
    email: str | None = Field(None, description="Optional email to send results")


class DocumentInput(BaseModel):
    text: str

class QueryInput(BaseModel):
    question: str
    k: int = 3