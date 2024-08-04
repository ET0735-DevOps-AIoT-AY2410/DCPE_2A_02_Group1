# Use an official Python image from the Docker Hub with build tools
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install --no-cache-dir rpi.gpio smbus 
# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
