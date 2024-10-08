import time
from threading import Thread, Event
from src.hal import hal_temp_humidity_sensor as temp_humid_sensor
from src.hal import hal_adc as adc
from src.hal import hal_ir_sensor as ir_sensor
from src.hal import hal_dc_motor as dc_motor
from src.hal import hal_servo as servo
from src.hal import hal_led as led
import database as db
from threading import Thread
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_adc as adc
from hal import hal_ir_sensor as ir_sensor
from hal import hal_dc_motor as dc_motor
from hal import hal_servo as servo
from hal import hal_led as led
from hal import hal_buzzer as buzzer


values = []

def adjust_temp(temperature):
    if  temperature > 23:
        dc_motor.set_motor_speed(70)
        print("fan on!")
        print(temperature)
    elif temperature == -100:
        dc_motor.set_motor_speed(70)
    elif temperature <= 27:
        dc_motor.set_motor_speed(0)
        print("fan off!")
        print(temperature)

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

def pH_warn (pH_level):
    if pH_level == False:
        buzzer.beep (0.5,0.25,4)

def adjustment():
    while not stop_event.is_set():
        try:
            global values 
            values = [temp_humid_sensor.read_temp_humidity()[0],adc.get_adc_value(1),adc.get_adc_value(0),ir_sensor.get_ir_sensor_state(),temp_humid_sensor.read_temp_humidity()[1]]
            adjust_temp(values[0])
            adjust_ec(values[1])
            adjust_light(values[2])
            time.sleep(2)
        except:
            pass



def main():
    temp_humid_sensor.init()
    ir_sensor.init()
    dc_motor.init()
    adc.init()
    servo.init()
    led.init()
    adjustment_thread = Thread(target=adjustment)
    adjustment_thread.start()
