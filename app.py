from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import os
from datetime import datetime

csv_file = 'database.csv'

with open(csv_file, mode='r', newline=' ') as file:
    csv_reader =  csv.DictReader(file)
    csv_file = [row for row in csv_reader]

# Function to log data into the CSV file
def log_data(ecval, temp, humidity, phlvl, light):
    timestamp = datetime.now().strftime('%H:%M:%S')
    data = {
        'timestamp': [timestamp],
        'EC Level': [ecval],
        'Temperature': [temp],
        'Humidity': [humidity],
        'pH Level': [phlvl],
        'Light Level': [light],
    }
    
    df = pd.DataFrame(data)
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df.to_csv(csv_file, mode='a', index=False, header=False)
    else:
        df.to_csv(csv_file, mode='w', index=False, header=True)

# Function to read the data from the CSV file into a DataFrame
def read_data():
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df = pd.read_csv(csv_file)
        return df
    else:
        return pd.DataFrame(columns=['timestamp', 'EC Level', 'Temperature', 'Humidity', 'pH Level', 'Light Level'])

# Function to analyze data using NumPy
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

app = Flask(__name__, template_folder='dashboard')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # Get data from the request
        data = request.json
        log_data(data['ec'], data['temperature'], data['humidity'], data['ph'], data['light'])
        return jsonify(success=True)
    else:
        df = read_data()
        data_storage = {
            "time": df['timestamp'].tolist(),
            "ph": df['pH Level'].tolist(),
            "temperature": df['Temperature'].tolist(),
            "humidity": df['Humidity'].tolist(),
            "light": df['Light Level'].tolist(),
            "ec": df['EC Level'].tolist()
        }
        return jsonify(data_storage)

if __name__ == '__main__':
    app.run(debug=True)