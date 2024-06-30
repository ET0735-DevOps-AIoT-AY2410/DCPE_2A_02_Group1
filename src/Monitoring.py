import time

from threading import Thread
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_adc as adc
from hal import hal_ir_sensor as ir_sensor
from hal import hal_dc_motor as dc_motor
from hal import hal_servo as servo
from hal import hal_led as led


def adjust_temp(temperature):
    if  temperature > 35:
        dc_motor.set_motor_speed(70)
        print("fan on!")
        print(temperature)
        time.sleep(10)
    else:
        dc_motor.set_motor_speed(0)
        print("fan off!")
        print(temperature)

def adjust_ec(ec_level):
    print(ec_level)
    if ec_level >= 500:
        servo.set_servo_position(180)
        time.sleep(0.5)
        servo.set_servo_position(0)

def adjust_light(light_level):
    print(f"light level = {light_level}")
    if light_level <= 500:
        led.set_output(1,1)
    else:
        led.set_output(1,0)

def adjustment():
    while 1:
        adjust_temp(temp_humid_sensor.read_temp_humidity()[0])
        adjust_ec(adc.get_adc_value(1))
        adjust_light(adc.get_adc_value(0))
        time.sleep(0.5)


def main():
    temp_humid_sensor.init()
    dc_motor.init()
    adc.init()
    servo.init()
    led.init()
    adjustment_thread = Thread(target=adjustment)
    adjustment_thread.start()
        



if __name__ == '__main__':
    main()