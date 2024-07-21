# Use the official image as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source code
COPY src /app/src
COPY models_pickle /app/models_pickle
COPY processors_pickle /app/processors_pickle

# Set environment variable for the port
ENV PORT 8080

# Run the application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
