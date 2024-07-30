# Use an official Python image from the Docker Hub with build tools
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for building NumPy and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
