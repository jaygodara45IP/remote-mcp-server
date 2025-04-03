# Basic MCP Server

## Installation Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/jaygodara45IP/remote-mcp-server
   cd remote-mcp-server
   ```

2. **Ensure you have `uv` installed:**
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies:**
   ```sh
   uv pip install
   ```

4. **Add required environment variables in the `.env` file. **  
    .env.copy contains the required information

5. **Run the server:**
   ```sh
   uvicorn app.main:app --reload
   ```

