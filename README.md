<<<<<<< HEAD
<<<<<<< HEAD
# DCPE/FT/2A/02 GROUP 1 ET0735 DevOps For AIoT Mini-Project

## Project overview

This project focuses on developing a DevOps solution for AIoT systems. It includes functionalities for login authentication and monitoring various environmental parameters such as temperature, electrical conductivity (EC), light, pH, and humidity
## Main functions

### Login

When program starts, LCD screen will prompt for login method.<br />
Press 1 to login by password or 2 to login by RFID card.

#### Password login

Enter password by using the keypad<br />
Authentication is successful when screen shows "Access Granted"<br />
 Authentication fails when screen shows "Access Denied"

#### RFID login

When prompted, bring RFID card to RFID tag reader. <br />
Authentication is successful when screen displays "Login Successful"

### Monitoring

Monitors the levels of temperature, EC , Light , pH and humidity

#### Temperature monitoring

Uses DHT to monitor temperature readings <br />
If temperature is over 30 degrees, causes DC Motor to spin to simulate a fan spinning to lower temperature.

#### EC Monitoring

Uses potentiometer to simulate the monitoring of electrical conductivity <br />
If electrical conductivity is too high, servo motor rotates

#### Light level monitoring

Uses LDR to monitor light level<br />
If light level is too low, LED turns on.

#### pH monitoring

Uses IR sensor to simulate monitoring of pH

#### Humidity monitoring

Uses DHT to monitor Humidity level

### App 

Logs monitored data into a csv file<br />
Data is continuously updated and shown as a graph on an online dashboard

## Setup Instructions

### Pulling Docker Image 
Pull Docker image of this project by using the following command:<br />
bash<br />
docker pull<br />
dennistgb/garden:latest<br />

### Running Docker Container
Run Docker Container by using the following command:<br />
bash<br />
docker run -privileged -d --name<br />
garden_monitor -p 5000:5000<br />
dennistgb/garden:latest<br />

This will start the container and map port 5000 of the host to port 5000 of the container

### Stopping the Docker Container
Stop docker container by using the following command:<br />
bash<br />
docker rm garden_monitor

## Contributors
 Dennis<br />
 Reynard<br />
 Heng Jeang<br />
 Yan Tiong


=======
# DCPE/FT/2A/02 GROUP 1 ET0735 DevOps For AIoT Mini-Project

## Project overview

This project focuses on developing a DevOps solution for AIoT systems. It includes functionalities for login authentication and monitoring various environmental parameters such as temperature, electrical conductivity (EC), light, pH, and humidity
## Main functions

### Login

When program starts, LCD screen will prompt for login method.<br />
Press 1 to login by password or 2 to login by RFID card.

#### Password login

Enter password by using the keypad<br />
Authentication is successful when screen shows "Access Granted"<br />
 Authentication fails when screen shows "Access Denied"

#### RFID login

When prompted, bring RFID card to RFID tag reader. <br />
Authentication is successful when screen displays "Login Successful"

### Monitoring

Monitors the levels of temperature, EC , Light , pH and humidity

#### Temperature monitoring

Uses DHT to monitor temperature readings <br />
If temperature is over 30 degrees, causes DC Motor to spin to simulate a fan spinning to lower temperature.

#### EC Monitoring

Uses potentiometer to simulate the monitoring of electrical conductivity <br />
If electrical conductivity is too high, servo motor rotates

#### Light level monitoring

Uses LDR to monitor light level<br />
If light level is too low, LED turns on.

#### pH monitoring

Uses IR sensor to simulate monitoring of pH

#### Humidity monitoring

Uses DHT to monitor Humidity level

### App 

Logs monitored data into a csv file<br />
Data is continuously updated and shown as a graph on an online dashboard

## Setup Instructions

### Pulling Docker Image 
Pull Docker image of this project by using the following command:<br />
bash<br />
docker pull<br />
dennistgb/garden:latest<br />

### Running Docker Container
Run Docker Container by using the following command:<br />
bash<br />
docker run -privileged -d --name<br />
garden_monitor -p 5000:5000<br />
dennistgb/garden:latest<br />

This will start the container and map port 5000 of the host to port 5000 of the container

### Stopping the Docker Container
Stop docker container by using the following command:<br />
bash<br />
docker rm garden_monitor

## Contributors
 Dennis<br />
 Reynard<br />
 Heng Jeang<br />
 Yan Tiong


>>>>>>> 1296ac9ee0ca9756b6bd09fa95f5b0ef4a591581
=======
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

- Dennis -> Backend: Monitoring.py, Displaying Graphs, Login.py and Unit Test Cases
- Reynard -> Frontend: index.html, about.html, dashboard.html, styles.css, graph_styles.css and Unit Test Cases
- Heng Jeang -> Hardware test cases
- Yan Tiong -> database.py for analysis (tentative)
>>>>>>> 662af007178cc9c2a1353b60191fddf232732b96
