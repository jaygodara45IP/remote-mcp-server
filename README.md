### 🚀 FastAPI MCP Server  

A simple guide to set up and run the FastAPI server locally and using Docker.  

## 🔧 Setup (Without Docker)  
```sh
# Clone the repository
git clone <repo_url>

# Move into the project directory
cd <repo_name>

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Copy environment variables
cp .env.local .env

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
```

## 🐳 Setup (Using Docker)  
```sh
# Clone the repository
git clone <repo_url>

# Move into the project directory
cd <repo_name>

# Copy environment variables
cp .env.local .env

# Build the Docker image
docker build -t fastapi-mcp-server .

# Run the container
docker run --env-file .env -p 8000:8000 fastapi-mcp-server
```

Now your FastAPI server is up and running! 🚀