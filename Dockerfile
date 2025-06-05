# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables (optional if you use `aws configure`)
ENV AWS_DEFAULT_REGION=ap-south-1

# Run the pipeline
CMD ["python", "run_pipeline.py"]
