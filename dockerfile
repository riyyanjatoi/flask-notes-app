
# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Prevent Python from generating bytecode
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output appears immediately in Docker logs
ENV PYTHONUNBUFFERED=1

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Document the application port
EXPOSE 8000

# Start Flask application
CMD ["python", "app.py"]
