import pytest
from hal import hal_lcd as LCD
from hal import hal_keypad as keypad
from hal import hal_rfid_reader as rfid_reader
import main

# Mock password for testing
TEST_PASSWORD = "1234"
# Mock RFID ID for testing
TEST_RFID_ID = "356639569392"

@pytest.fixture(autouse=True)
def setup_hardware():
    # Initialize the hardware components
    keypad.init(main.key_pressed)
    main.shared_keypad_queue.queue.clear()
    lcd = LCD.lcd()
    lcd.lcd_clear()
    rfid_reader.init()
    
    yield

    # Cleanup if necessary
    lcd.lcd_clear()

def test_pass_login_correct_password(setup_hardware):
    # Prompt to enter the correct password
    input(f"Please enter the correct password '{TEST_PASSWORD}#' on the keypad and press Enter to continue...")
    assert main.pass_login() is True

def test_pass_login_wrong_password(setup_hardware):
    # Prompt to enter an incorrect password
    input("Please enter the wrong password '5678#' on the keypad and press Enter to continue...")
    assert main.pass_login() is False

def test_rfid_login_success(setup_hardware):
    # Prompt to present the correct RFID card
    input(f"Please place the correct RFID card with ID '{TEST_RFID_ID}' near the reader and press Enter to continue...")
    assert main.rfid_login() is True

def test_main_password_login(setup_hardware):
    # Prompt to select password login and enter the correct password
    input(f"Please select '1' for password login, then enter '{TEST_PASSWORD}#' on the keypad and press Enter to continue...")
    assert main.main() is True

def test_main_rfid_login(setup_hardware):
    # Prompt to select RFID login and present the correct RFID card
    input(f"Please select '2' for RFID login and present the correct RFID card with ID '{TEST_RFID_ID}', then press Enter to continue...")
    assert main.main() is True
