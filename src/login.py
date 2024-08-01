import time
from threading import Thread
import queue
from src.hal import hal_lcd as LCD
from src.hal import hal_keypad as keypad
from src.hal import hal_rfid_reader as rfid_reader

# Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()

# Predefined password for login
PASSWORD = "1234"

# Callback function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)

def pass_login():
    lcd = LCD.lcd()
    input_password = ""
    while True:
        key = shared_keypad_queue.get()
        lcd.lcd_clear()
        lcd.lcd_display_string("Input Password:", 1)
        if key == "#":
            if input_password == PASSWORD:
                lcd.lcd_clear()
                lcd.lcd_display_string("Access Granted", 1)
                time.sleep(2)
                return True
            else:
                lcd.lcd_clear()
                lcd.lcd_display_string("Access Denied", 1)
                time.sleep(2)
                input_password = ""
                lcd.lcd_clear()
                lcd.lcd_display_string("Enter Password:", 1)
        elif key == "*":
            input_password = ""
            lcd.lcd_clear()
            lcd.lcd_display_string("Enter Password:", 1)
        else:
            input_password += str(key)
            lcd.lcd_display_string("*" * len(input_password), 2)
            

def rfid_login():
    lcd = LCD.lcd()
    reader = rfid_reader.init()
    lcd.lcd_clear()
    lcd.lcd_display_string("Bring Card", 1)
    while 1:
        print("im here")
        id = reader.read_id_no_block()
        id = str(id)
        if id == '356639569392':
            print("RFID card ID = " + id)
            lcd.lcd_clear()
            time.sleep(0.5)
            lcd.lcd_display_string("Login Success", 1)
            lcd.lcd_clear()
            lcd.lcd_display_string(id, 2)
            return True


def main():
    # Initialization of HAL modules
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    lcd = LCD.lcd()
    lcd.lcd_display_string("Select Login", 1)
    lcd.lcd_display_string("Method:", 2)
    time.sleep(2)
    lcd.lcd_clear()
    lcd.lcd_display_string("1: Password", 1)
    lcd.lcd_display_string("2: Rfid", 2)
    time.sleep(2)
    key = shared_keypad_queue.get()
    if key == 1:
        accessed = pass_login()
    elif key == 2:
        accessed = rfid_login()
    if accessed == True:
        lcd.lcd_clear()
        lcd.lcd_display_string("Garden", 1)
        lcd.lcd_display_string("Running...", 2)
        print("logined")
        return True
    return False
    


if __name__ == '__main__':
    main()
