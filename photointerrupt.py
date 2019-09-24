import time
import board
from digitalio import DigitalInOut, Direction, Pull

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
PI = DigitalInOut(board.D8)
PI.direction = Direction.INPUT
PI.pull = Pull.UP
# the photo interrupter is plugged into digital pin 8
p = 0
# PI has been interrupted 0 times
interrupt = False
while True:
    lcd.backlight = True
    # turn on LCD
    if PI.value:
        if interrupt == False:
            interrupt = True
            # when interrupt equals True the count will not go up
            p = p + 1
            print ("interrupted")
    if not PI.value:
        interrupt = False
        # interrupt must be turned off to begin counting again (button only counts once per interrupt, no matter how long it is interrupted for)
    if time.monotonic () % 4 == 0:
    # every 4 seconds print the interrupt count
        lcd.set_cursor_pos (0,0)
        lcd.print ("Interrupted ")
        lcd.set_cursor_pos (1,0)
        lcd.print(str (p))
        lcd.print (" times")