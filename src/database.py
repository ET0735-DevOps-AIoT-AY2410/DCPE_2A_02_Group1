import pandas as pd
import random
import os
import numpy as np
import time
from datetime import datetime


# File path for the CSV file
<<<<<<< HEAD
csv_file = 'src/database.csv'
time_file = 'src/timeanalysis.csv'
ec_file = 'src/ecanalysis.csv'
=======
csv_file = 'database.csv'
tempanalysiscsv_file = 'temperature_analysis.csv'
ecanalysiscsv_file= 'ec_analysis.csv'
>>>>>>> 8de241a1c580469bbaa4108d832ea3217fcc987f
# Function to log data into the CSV file
def log_data(data):
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # Check if the CSV file exists and is not empty
    if os.path.exists(time_file) and os.path.getsize(time_file) > 0:
        # Append the DataFrame to the CSV file
        df.to_csv(time_file, mode='a', index=False, header=False)
    else:
        # Create the CSV file with the header
        df.to_csv(time_file, mode='w', index=False, header=True)

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

<<<<<<< HEAD
def historical_data(df):
    time_filter = ['2024-08-04']
    analysis = pd.DataFrame[df['Time'].isin(time_filter)]
    return analysis
    
def main():
    df=read_data()
    analysis=historical_data(df)
    log_data(analysis)




if __name__ == '__main__':
    main()

=======
def analyze_temperature_data(temperature):
    
    analysis = {
        'mean': np.mean(temperature),
        'median': np.median(temperature),
        'std_dev': np.std(temperature)
    }
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(analysis)
    
    # Check if the CSV file exists and is not empty
    if os.path.exists(tempanalysiscsv_file) and os.path.getsize(tempanalysiscsv_file) > 0:
        # Append the DataFrame to the CSV file
        df.to_csv(tempanalysiscsv_file, mode='a', index=False, header=False)
    else:
        # Create the CSV file with the header
        df.to_csv(tempanalysiscsv_file, mode='w', index=False, header=True)
    return analysis

def analyze_ec_data(ecval):
    
    analysis = {
        'mean': np.mean(ecval),
        'median': np.median(ecval),
        'std_dev': np.std(ecval)
    }
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(analysis)
    
    # Check if the CSV file exists and is not empty
    if os.path.exists(ecanalysiscsv_file) and os.path.getsize(ecanalysiscsv_file) > 0:
        # Append the DataFrame to the CSV file
        df.to_csv(ecanalysiscsv_file, mode='a', index=False, header=False)
    else:
        # Create the CSV file with the header
        df.to_csv(ecanalysiscsv_file, mode='w', index=False, header=True)
    return analysis
    
>>>>>>> 8de241a1c580469bbaa4108d832ea3217fcc987f
