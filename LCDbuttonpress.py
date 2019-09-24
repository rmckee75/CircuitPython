import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
# if 0x3F adress doesn't work try 0x27
button = DigitalInOut(board.D4)
button.direction = Direction.INPUT
button.pull = Pull.UP
# button starts pulled up (pressing will pull it down)
switch = DigitalInOut(board.D8)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
p = 0
# the button has been pressed 0 times
j = 1
# the button press count will increase by 1
press = False
while True:
    lcd.backlight = True
    # turn on LCD
    lcd.set_cursor_pos (0,0)
    # start typing in top left corner
    if not button.value:
    # when the button is pressed
        if press == False:
            press = True
            # when press equals True the press count will not go up
            if switch.value:
                p = p + j
            if not switch.value:
                p = p - j
            # switch value determines direction
    if button.value:
        press = False
        # press must be turned off to begin counting again (button only counts once per press, no matter how long it is pressed down)
    lcd.set_cursor_pos (0, 0)
    lcd.print ("Presses = ")
    lcd.print (str(p))
    # print the press value (string data)
    lcd.print ("    ")
    # print empty space to clear any previous numbers
    if switch.value:
        lcd.set_cursor_pos (1,0)
        lcd.print ("Switch St = UP  ")
    if not switch.value:
        lcd.set_cursor_pos (1,0)
        lcd.print ("Switch St = DOWN")