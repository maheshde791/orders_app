# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Set the entrypoint for the task service
CMD ["python", "main.py"]