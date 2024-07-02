import pandas as pd
import random
import os
from datetime import datetime


# File path for the CSV file
csv_file = 'database.csv'

# Function to log data into the CSV file
def log_data(ecval, temp, humidity, phval, light):
    # Get the current timestamp
    timestamp = datetime.now().strftime('%H:%M:%S')
    
    # Create a dictionary for the new entry
    data = {
        'timestamp': [timestamp],
        'EC Level': [ecval],
        'Temperature': [temp],
        'Humidity': [humidity],
        'pH Level': [phval],
        'Light Level': [light]
    }
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # Check if the CSV file exists and is not empty
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        # Append the DataFrame to the CSV file
        df.to_csv(csv_file, mode='a', index=False, header=False)
    else:
        # Create the CSV file with the header
        df.to_csv(csv_file, mode='w', index=False, header=True)

# Function to read the data from the CSV file into a DataFrame
def read_data():
    # Check if the CSV file exists and is not empty
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        return df
    else:
        # Return an empty DataFrame if the file does not exist or is empty
        return pd.DataFrame(columns=['timestamp', 'EC Level', 'Temperature', 'Humidity', 'pH Level', 'Light Level'])


