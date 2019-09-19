import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
button = DigitalInOut(board.D4)
button.direction = Direction.INPUT
button.pull = Pull.UP
switch = DigitalInOut(board.D8)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
p = 0
j = 1
press = False
while True:
    lcd.backlight = True
    lcd.set_cursor_pos (0,0)
    if not button.value:
        if press == False:
            press = True
            if switch.value:
                p = p + j
            if not switch.value:
                p = p - j
    if button.value:
        press = False
    lcd.set_cursor_pos (0, 0)
    lcd.print ("Presses = ")
    lcd.print (str(p))
    lcd.print ("    ")
    if switch.value:
        lcd.set_cursor_pos (1,0)
        lcd.print ("Switch St = UP  ")
    if not switch.value:
        lcd.set_cursor_pos (1,0)
        lcd.print ("Switch St = DOWN")