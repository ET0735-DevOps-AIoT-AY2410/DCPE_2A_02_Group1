# DCPE/FT/2A/02 GROUP 1 ET0735 DevOps For AIoT Mini-Project
Done by Dennis, Reynard, Heng Jeang and Yan Tiong 
## Main functions
### Login
When program starts, LCD screen will prompt for login method.
Press 1 to login by password or 2 to login by RFID card.
#### Password login
Enter password by pressing the keys corresponding to the password on keypad, authentication is successful when screen shows "Access Granted". Authentication fails when screen shows "Access Denied"
#### RFID login
When prompted, bring RFID card to RFID tag reader. Authentication is successful when screen displays "Login Successful"
### Monitoring
Monitors the levels of temperature, EC , Light , pH and humidity
#### Temperature monitoring
Uses DHT to monitor temperature readings 
If temperature is over 30 degrees, causes DC Motor to spin to simulate a fan spinning to lower temperature.
#### EC Monitoring
Uses potentiometer to simulate the monitoring of electrical conductivity
If electrical conductivity is too high, servo motor rotates
#### Light level monitoring
Uses LDR to monitor light level
If light level is too low, LED turns on.
#### pH monitoring
Uses ir sensor to simulate monitoring of pH
#### Humidity monitoring
Uses DHT to monitor Humidity level
### App 
Logs monitored data into a csv file
Data is continuously updated and shown as a graph on an online dashboard



