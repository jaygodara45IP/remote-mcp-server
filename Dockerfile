# Use official Python image as base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first (to leverage caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the application port (default for FastAPI)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]