# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Environment variables for default configuration
ENV API_BASE_URL=https://router.huggingface.co/v1
ENV MODEL_NAME=meta-llama/Meta-Llama-3-8B-Instruct
ENV HF_TOKEN=""

# Run the environment check as default command
CMD ["python", "main.py"]
