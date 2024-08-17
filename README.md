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
### Pytest

-"update_value" function behaves as expected across different scenarios  
-"test_update_chart" ensures that the simulated chart data retains only the most recent data points

## Contributors

- Dennis -> Backend: Monitoring.py, Displaying Graphs, dashboard.html, Login.py and Unit Test Cases
- Reynard -> Frontend: index.html, about.html, dashboard.html, styles.css, graph_styles.css and Unit Test Cases
- Heng Jeang -> Hardware test cases, Backend: dashboard.html
- Yan Tiong -> database.py for analysis (tentative)
=======
# DCPE/FT/2A/02 GROUP 1 ET0735 DevOps For AIoT Mini-Project

## Disclaimer 
This README is updated as of 16th August 2024.
Newly added feature of database analysis is NOT Dockerized.
Last dockerized version is the base version found @https://hub.docker.com/repository/docker/dennistgb/garden/general

## Project Overview

This project focuses on developing a DevOps solution for AIoT systems. It includes functionalities for login authentication and monitoring various environmental parameters such as temperature, electrical conductivity (EC), light, pH, and humidity.

## Main Functions

### Login [Additional Function]

When the program starts, the LCD screen will prompt for a login method.
- Press 1 to login by password.
- Press 2 to login by RFID card.

#### Password Login [Additional Function]

- Enter the password using the keypad.
- Authentication is successful when the screen shows "Access Granted".
- Authentication fails when the screen shows "Access Denied".

#### RFID Login [Additional Function]

- When prompted, bring the RFID card to the RFID tag reader.
- Authentication is successful when the screen displays "Login Successful".

### Data Analysis [Additional Function - Undockerized] 
- Takes data from database.csv.
- Finds Mean, Median, and Standard Deviation of Data.
- Updates when new data is added.

### Monitoring [Base Function]

Monitors the levels of temperature, EC, light, pH, and humidity.

#### Temperature Monitoring [Base Function]

- Uses a DHT sensor to monitor temperature readings.
- If the temperature is over 27 degrees, the DC motor spins to simulate a fan spinning to lower the temperature.

#### EC Monitoring [Base Function]

- Uses a potentiometer to simulate the monitoring of electrical conductivity.
- If the electrical conductivity is too low (<=500), the servo motor rotates and dispenses a solution.

#### Light Level Monitoring [Base Function]

- Uses an LDR to monitor light levels.
- If the light level is too low (<=600), the LED turns on.

#### pH Monitoring [Base Function]

- Uses an IR sensor to simulate the monitoring of pH levels.

#### Humidity Monitoring [Base Function]

- Uses a DHT sensor to monitor humidity levels.

### App [Base Function]

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

- Dennis -> Backend: Monitoring.py, Login.py, Graphs: dashboard.html, Unit Test Cases 
- Reynard -> Frontend: index.html, about.html, dashboard.html, styles.css, graph_styles.css and Unit Test Cases
- Heng Jeang -> Hardware + Software test cases
- Yan Tiong -> database.py for analysis 
>>>>>>> 4fb5c159550499ff9d3224910b43dfbcdd99f0db
