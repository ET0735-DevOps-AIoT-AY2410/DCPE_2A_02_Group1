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
    print(f"Key pressed: {key}")  # Debug print

def login():
    lcd = LCD.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string("Enter Password:", 1)
    print("Starting login loop")  # Debug print
    input_password = ""
    while True:
        key = shared_keypad_queue.get()
        print(f"Key retrieved from queue: {key}")  # Debug print
        if key == "#":
            if input_password == PASSWORD:
                lcd.lcd_clear()
                lcd.lcd_display_string("Access Granted", 1)
                print("Access Granted")  # Debug print
                time.sleep(2)
                return True
            else:
                lcd.lcd_clear()
                lcd.lcd_display_string("Access Denied", 1)
                print("Access Denied")  # Debug print
                time.sleep(2)
                input_password = ""
                lcd.lcd_clear()
                lcd.lcd_display_string("Enter Password:", 1)
                print("Ready for another attempt")  # Debug print
        elif key == "*":
            input_password = ""
            lcd.lcd_clear()
            lcd.lcd_display_string("Enter Password:", 1)
            print("Password reset")  # Debug print
        else:
            input_password += str(key)
            lcd.lcd_display_string("*" * len(input_password), 2)
            print(f"Current password input: {input_password}")  # Debug print

def main():
    # Initialization of HAL modules
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    access_granted = login()
    if access_granted == True:
        lcd = LCD.lcd()
        lcd.lcd_clear()
        lcd.lcd_display_string("Garden", 1)
        lcd.lcd_display_string("Running...", 2)
        print("Logged in successfully")  # Debug print
        return True
    return False

if __name__ == '__main__':
    main()
