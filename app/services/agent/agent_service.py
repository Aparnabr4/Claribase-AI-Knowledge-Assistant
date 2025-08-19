# app/services/agent_service.py
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from app.services.llm.llm_service import answer_tool
from app.services.email.email_service import send_email_tool  # assume wrapped as Tool
from app.services.mcp.mcp_service import mcp_tool             # optional if you expose MCP
from app.services.rag.rag_service import rag_tool             # assume wrapped as Tool

load_dotenv()

# LangChain LLM
llm = ChatOpenAI(
    model="llama3-8b-8192",
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1",
    temperature=0.2
)

# Register tools
tools = [
    answer_tool,     # knowledge base Q&A
    rag_tool,        # retrieval
    send_email_tool, # email sending
    mcp_tool         # (optional) MCP
]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(query: str) -> str:
    """
    Run the LangChain agent with all registered tools.
    """
    return agent.run(query)
