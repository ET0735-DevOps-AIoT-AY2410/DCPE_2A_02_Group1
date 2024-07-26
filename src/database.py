import pandas as pd
import random
import os
import numpy as np
from scipy import stats
import time
from datetime import datetime


# File path for the CSV file
csv_file = 'database.csv'
csv_file2 = 'analysis.csv'
# Function to log data into the CSV file
def log_data(temp, ecval, light, phval, humidity):
    # Get the current timestamp
    timestamp = datetime.now().strftime('%H:%M:%S')
    if temp == -100:
        temp = 25.0
    # Create a dictionary for the new entry
    data = {
        'timestamp': [timestamp],
        'Temperature': [temp],
        'EC Level': [ecval],
        'Light Level': [light],
        'pH Level': [phval],
        'Humidity': [humidity]        

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

def analyze_data(df):
    analysis = {}
    columns = ['EC Level', 'Temperature', 'Humidity', 'pH Level', 'Light Level']
    
    for col in columns:
        data = df[col].values
        if (col=='pH Level'):
            analysis[col] = {
                'mode':stats.mode(data)
            }
        else:
            analysis[col] = {
                'mean': np.mean(data),
                'median': np.median(data),
                'std_dev': np.std(data)
            }
    
    # Create a DataFrame from the dictionary
    df2 = pd.DataFrame(analysis)
    
    # Check if the CSV file exists and is not empty
    if os.path.exists(csv_file2) and os.path.getsize(csv_file2) > 0:
        # Append the DataFrame to the CSV file
        df2.to_csv(csv_file2, mode='a', index=False, header=False)
    else:
        # Create the CSV file with the header
        df2.to_csv(csv_file2, mode='w', index=False, header=True)
    return analysis

    