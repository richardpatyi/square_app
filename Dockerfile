# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# Cloud Run uses PORT=8080
ENV PORT=8080

# Run the app
CMD ["python", "square.py"]