# main.py

from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.api.query import router as query_router

app = FastAPI(
    title="ClariBase - Enterprise Knowledge Agent",
    description="LLM + RAG powered assistant with Model Context Protocol and Email",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router)

@app.get("/")
async def root():
    return {"message": "Welcome to ClariBase 👋"}



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


# python - m venv venv
# source venv/bin/activate
# uvicorn app.main:app --reload


# Example Question

# "How many annual leave days do I get?"
# "Can unused leave be carried over to next year?"
# "How long is maternity leave?"
# "Do I need a medical certificate for sick leave?"
# "How many days of paternity leave are allowed?"