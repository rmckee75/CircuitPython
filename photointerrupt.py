import time
import board
from digitalio import DigitalInOut, Direction, Pull

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
PI = DigitalInOut(board.D8)
PI.direction = Direction.INPUT
PI.pull = Pull.UP
p = 0
interrupt = False
while True:
    lcd.backlight = True
    if PI.value:
        if interrupt == False:
            interrupt = True
            p = p + 1
            print ("interrupted")
    if not PI.value:
        interrupt = False
    if time.monotonic () % 4 == 0:
        lcd.set_cursor_pos (0,0)
        lcd.print ("Interrupted ")
        lcd.set_cursor_pos (1,0)
        lcd.print(str (p))
        lcd.print (" times")