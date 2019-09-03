import time
import board
import digitalio

button_a = digitalio.DigitalInOut(board.D2)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

lcd.clear()

while True:
    if button_a.value:
        lcd.set_cursor_pos(1, 4)
        lcd.print("     ")
    else:
        lcd.set_cursor_pos(1, 4)
        lcd.print("hello")


# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)
