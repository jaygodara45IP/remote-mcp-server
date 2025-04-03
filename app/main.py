import json, os, requests
from fastapi import FastAPI
from app.sse import create_sse_server
from mcp.server.fastmcp import FastMCP

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")


app = FastAPI()
mcp = FastMCP("demo-server")

@app.get("/")
def read_root():
    return {"message": "Server running good..."}

# Mount the Starlette SSE server onto the FastAPI app
app.mount("/", create_sse_server(mcp))



@mcp.tool()
def google_search(query: str):
    """Performs google search on the provided query.
    Args:
    query: the query to perform google search on (eg. what is the today's date?)
    
    Returns:
    Text from the google search as string"""
    url = "https://google.serper.dev/search"

    payload = json.dumps({
    "q": query,
    "num": 3
    })
    headers = {
    'X-API-KEY': SERPER_API_KEY,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    text = ""
    for current_response in response["organic"]:
        text += current_response["snippet"]
        text += "\n"

    return text

@mcp.tool()
def internal_knowledge_base():
    """Return internal information about Infinite possibilties."""
    return """Number of employees in Infinite possibilties are 21. We have frontend, backend and AI teams.
    Main tech stack is fastapi, sql, major llm providers, azure."""