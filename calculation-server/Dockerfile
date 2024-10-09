#Author: Sboniso Makhonjwa
#Date : 05/08/2024

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


# Run the FastAPI application
CMD ["uvicorn", "fastapi_server:app", "--host", "0.0.0.0", "--port", "8000"]
