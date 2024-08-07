import pandas as pd
import random
import os
import numpy as np
import time
from datetime import datetime


# File path for the CSV file
csv_file = 'src/database.csv'
temp_file = 'src/tempanalysis.csv'
ec_file = 'src/ecanalysis.csv'
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

# Function to read the data from the CSV file into a DataFramew
def analyze_data(df):
    analysis = {}
    columns = ['EC Level', 'Temperature', 'Humidity', 'pH Level', 'Light Level']
    
    for col in columns:
        data = df[col].values
        analysis[col] = {
            'mean': np.mean(data),
            'median': np.median(data),
            'std_dev': np.std(data)
        }
    
    return analysis



# Function to read the data from the CSV file into a DataFrame
def read_data():
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df = pd.read_csv(csv_file)
        return df
    else:
        return pd.DataFrame(columns=['timestamp', 'EC Level', 'Temperature', 'Humidity', 'pH Level', 'Light Level'])

def historical_data(df):
    
    
def main():
    df=read_data()



if __name__ == '__main__':
    main()

