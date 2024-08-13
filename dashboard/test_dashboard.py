import pytest

mock_data = {
    "time": ["10:00", "10:01", "10:02", "10:03"],
    "ph": [7.5, 7.8, 8.1, 7.9],
    "temperature": [25, 26, 27, 28],
    "humidity": [60, 65, 70, 75],
    "light": [500, 550, 600, 650],
    "ec": [400, 450, 500, 550]
}

thresholds = {
    "ph": 8,
    "temperature": 27,
    "humidity": 80,
    "light": 600,
    "ec": 500
}

def update_value(value, threshold, element_id):
    """ Simulates the updateValue function """
    if element_id == 'current-light' and value < threshold:
        color = 'red'
    elif element_id == 'current-ec' and value <= threshold:
        color = 'red'
    elif element_id != 'current-light' and element_id != 'current-ec' and value > threshold:
        color = 'red'
    else:
        color = 'black'
    return color

# Test pH level (above threshold)
def test_update_ph():
    assert update_value(8.1, thresholds['ph'], 'current-ph') == 'red'

# Test Temperature level (equal to threshold)
def test_update_temperature():
    assert update_value(27, thresholds['temperature'], 'current-temperature') == 'black'

# Test Humidity level (below threshold)
def test_update_humidity():
    assert update_value(75, thresholds['humidity'], 'current-humidity') == 'black'

# Test Light level (below threshold)
def test_update_light():
    assert update_value(500, thresholds['light'], 'current-light') == 'red'

# Test EC level (below threshold)
def test_update_ec():
    assert update_value(450, thresholds['ec'], 'current-ec') == 'red'

def test_update_chart():
    # Simulate adding data points and ensuring only the last 8 are kept
    data = []
    max_points = 8

    for time, value in zip(mock_data['time'], mock_data['ph']):
        data.append((time, value))
        if len(data) > max_points:
            data.pop(0)
    
    assert len(data) <= max_points  # Ensure data doesn't exceed max_points
    assert data[-1] == ('10:03', 7.9)  # Ensure the last value is correct

