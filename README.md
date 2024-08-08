# DCPE/FT/2A/02 GROUP 1 ET0735 DevOps For AIoT Mini-Project

## Project Overview

This project focuses on developing a DevOps solution for AIoT systems. It includes functionalities for login authentication and monitoring various environmental parameters such as temperature, electrical conductivity (EC), light, pH, and humidity.

## Main Functions

### Login

When the program starts, the LCD screen will prompt for a login method.
- Press 1 to login by password.
- Press 2 to login by RFID card.

#### Password Login

- Enter the password using the keypad.
- Authentication is successful when the screen shows "Access Granted".
- Authentication fails when the screen shows "Access Denied".

#### RFID Login

- When prompted, bring the RFID card to the RFID tag reader.
- Authentication is successful when the screen displays "Login Successful".

### Monitoring

Monitors the levels of temperature, EC, light, pH, and humidity.

#### Temperature Monitoring

- Uses a DHT sensor to monitor temperature readings.
- If the temperature is over 27 degrees, the DC motor spins to simulate a fan spinning to lower the temperature.

#### EC Monitoring

- Uses a potentiometer to simulate the monitoring of electrical conductivity.
- If the electrical conductivity is too low (<=500), the servo motor rotates and dispenses a solution.

#### Light Level Monitoring

- Uses an LDR to monitor light levels.
- If the light level is too low (<=600), the LED turns on.

#### pH Monitoring

- Uses an IR sensor to simulate the monitoring of pH levels.

#### Humidity Monitoring

- Uses a DHT sensor to monitor humidity levels.

### App

- Logs monitored data into a CSV file.
- Data is continuously updated and shown as a graph on an online dashboard.

## Setup Instructions

### Pulling the Docker Image

To pull the Docker image for this project, run the following command:
```bash
docker pull dennistgb/garden:latest
```

### Running the Docker Container

To run the Docker container, use the following command:
```bash
docker run --privileged -d --name garden_monitor -p 5000:5000 dennistgb/garden:latest
```

This will start the container and map port 5000 of the host to port 5000 of the container.

### Stopping the Docker Container

To stop the running container, use the following command:
```bash
docker stop garden_monitor
```

### Removing the Docker Container

To remove the container, use the following command:
```bash
docker rm garden_monitor
```

## Contributors

- Dennis
- Reynard
- Heng Jeang
- Yan Tiong
