import time
from threading import Thread, Event
from src.hal import hal_temp_humidity_sensor as temp_humid_sensor
from src.hal import hal_adc as adc
from src.hal import hal_ir_sensor as ir_sensor
from src.hal import hal_dc_motor as dc_motor
from src.hal import hal_servo as servo
from src.hal import hal_led as led


values = []
stop_event = Event()

def adjust_temp(temperature):
    if  temperature > 27:
        dc_motor.set_motor_speed(70)
    if temperature == -100:
        dc_motor.set_motor_speed(70)
    elif temperature <= 27:
        dc_motor.set_motor_speed(0)

def adjust_ec(ec_level):
    if ec_level <= 500:
        servo.set_servo_position(180)
        time.sleep(0.5)
        servo.set_servo_position(0)

def adjust_light(light_level):
    if light_level <= 600:
        led.set_output(1,1)
    else:
        led.set_output(1,0)

def adjustment():
    while not stop_event.is_set():
        try:
            global values 
            values = [temp_humid_sensor.read_temp_humidity()[0],adc.get_adc_value(1),adc.get_adc_value(0),ir_sensor.get_ir_sensor_state(),temp_humid_sensor.read_temp_humidity()[1]]
            print(values)
            adjust_temp(values[0])
            adjust_ec(values[1])
            adjust_light(values[2])
            time.sleep(2)
            print("adjusting")
        except:
            pass

def stopadj():
    stop_event.set()
    print("stopped all")

def main():
    temp_humid_sensor.init()
    ir_sensor.init()
    dc_motor.init()
    adc.init()
    servo.init()
    led.init()
    adjustment_thread = Thread(target=adjustment)
    adjustment_thread.start()
