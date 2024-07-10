from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import os
from datetime import datetime
import time
import database as db
import Monitoring as mon
from threading import Thread
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_adc as adc
from hal import hal_ir_sensor as ir_sensor
from hal import hal_dc_motor as dc_motor
from hal import hal_servo as servo
from hal import hal_led as led

csv_file = 'database.csv'


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


datas = {
        #'''"time": [datetime.now().strftime('%H:%M:%S')],
        #"ph": [values[3]],
        #"temperature": [values[0]],
        #"humidity": [values[4]],
        #"light": [values[2]],
        #"ec": [values[1]]'''
        "time": [datetime.now().strftime('%H:%M:%S')],
        "ph": [1],
        "temperature": [1],
        "humidity": [1],
        "light": [1],
        "ec": [1]
    }

def update_data(data_storage):
    values = [temp_humid_sensor.read_temp_humidity()[0],adc.get_adc_value(1),adc.get_adc_value(0),ir_sensor.get_ir_sensor_state(),temp_humid_sensor.read_temp_humidity()[1]]
    
    current_time = datetime.now().strftime('%H:%M:%S')
    data_storage["time"].append(current_time)
    data_storage["time"].pop(0)
    
    data_storage["ph"].append(1)
    data_storage["ph"].pop(0)
    
    data_storage["temperature"].append(values[0])
    data_storage["temperature"].pop(0)
    
    data_storage["humidity"].append(values[4])
    data_storage["humidity"].pop(0)
    
    data_storage["light"].append(values[2])
    data_storage["light"].pop(0)
    
    data_storage["ec"].append(values[1])
    data_storage["ec"].pop(0)
    print(data_storage)

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

app = Flask(__name__, template_folder='../dashboard')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    update_data(datas)
    return jsonify(datas)
            
       
if __name__ == '__main__':
    temp_humid_sensor.init()
    ir_sensor.init()
    dc_motor.init()
    adc.init()
    servo.init()
    led.init()
    '''adjustment_thread = Thread(target=mon.adjustment)
    adjustment_thread.start()'''
    app.run(debug=True)