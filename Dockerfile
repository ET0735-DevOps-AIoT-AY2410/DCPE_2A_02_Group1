# Use an official Python image from the Docker Hub with build tools
FROM arm32v7/python:3

ENV SPI_PATH /app/SPI-Py

ENV TZ=Asia/Singapore
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhost.org -r requirements.txt 

RUN pip3 install --no-cache-dir rpi.gpio\
 smbus

RUN apt-get update
# Copy the rest of the application code into the container
COPY . .

WORKDIR $SPI_PATH

RUN python3 setup.py install

RUN pip3 install spidev

WORKDIR /app

RUN apt install nano -y
# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "-u", "app.py"]
