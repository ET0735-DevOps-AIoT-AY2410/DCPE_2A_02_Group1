import pytest
from hal import hal_lcd as LCD
from hal import hal_keypad as keypad
from hal import hal_rfid_reader as rfid_reader
import queue
import main  

PASSWORD == 1234

@pytest.fixture(autouse=True)
def setup_hardware():
    keypad.init(main.key_pressed)
    main.shared_keypad_queue.queue.clear()
    lcd = LCD.lcd()
    lcd.lcd_clear()
    rfid_reader.init()

def test_pass_login_correct_password(setup_hardware):
    input("Please enter the correct password '1234#' on the keypad and press Enter to continue...")
    assert main.pass_login() is True

def test_pass_login_wrong_password(setup_hardware):
    input("Please enter the wrong password '5678#' on the keypad and press Enter to continue...")
    assert main.pass_login() is False

def test_rfid_login_success(setup_hardware):
    input("Please place the correct RFID card near the reader and press Enter to continue...")
    assert main.rfid_login() is True

def test_main_password_login(setup_hardware):
    input("Please select '1' for password login, then enter '1234#' on the keypad and press Enter to continue...")
    assert main.main() is True

def test_main_rfid_login(setup_hardware):
    input("Please select '2' for RFID login and present the correct RFID card, then press Enter to continue...")
    assert main.main() is True
