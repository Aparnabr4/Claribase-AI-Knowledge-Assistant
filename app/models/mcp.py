from pydantic import BaseModel
from typing import Any, Dict, Optional


class MCPMessage(BaseModel):
    """Represents a single MCP message."""
    type: str
    data: Dict[str, Any]


class MCPEnvelope(BaseModel):
    """Represents the envelope structure for sending/receiving MCP messages."""
    id: str
    timestamp: str
    source: str
    destination: str
    message: MCPMessage
    metadata: Optional[Dict[str, Any]] = None
