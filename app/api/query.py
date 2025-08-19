#app/api/query
from fastapi import APIRouter, HTTPException
from app.models.query import QueryRequest
from app.models.response import QueryResponse
from app.core.config import Health
from app.services.mcp.mcp_service import mcp_tool

router = APIRouter(
    prefix="/api",
    tags=["Query"]
)

@router.get("/health", response_model=Health)
async def health():
    return Health()

@router.post("/query", response_model=QueryResponse)
async def process_query(payload: QueryRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    resp = await mcp_tool.ainvoke({"question": payload.question,"email": payload.email})

    return resp
