import time
from threading import Thread
import queue
from src.hal import hal_lcd as LCD
from src.hal import hal_keypad as keypad

# Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()

# Predefined password for login
PASSWORD = "1234"

# Callback function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)

def login():
    lcd = LCD.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string("Enter Password:", 1)
    print("againnnnn")
    input_password = ""
    while True:
        key = shared_keypad_queue.get()
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

def main():
    # Initialization of HAL modules
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    access_granted = login()
    if access_granted:
        lcd = LCD.lcd()
        lcd.lcd_clear()
        lcd.lcd_display_string("Garden", 1)
        lcd.lcd_display_string("Running...", 2)
        print("logined")
        return True

if __name__ == '__main__':
    main()
