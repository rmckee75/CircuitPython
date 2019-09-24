import board
import time
import neopixel
# neopixel is built-in metro RGB LED
from adafruit_hcsr04 import HCSR04
# import the HCSR04 ultrasonic sensor
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
trig = board.D10
echo = board.D7
# ultrasonic sensor plugged into pins D10 and D7
sonar = HCSR04 (trig, echo)
# sonar will judge distance by bouncing wave off object
while True:
    try:
    # try to find distance value
        n = sonar.distance
        # find the distance of the object
        if (n < 15):
        # red will have a value when distance is less than 15
            R = abs(5 - n)
            redfloat = (255 - R*25.5)
            # distance away from 5 (peak red value) is subtracted from 255 (max color value)
            red = int(round(redfloat))
            # RGB only accepts integers
        elif (n > 15):
            red = 0
        if (n > 10):
            if (n < 30):
            # blue will have a value when distance is between 10 and 30
                B = abs(20 - n)
                bluefloat =(255 - B*25.5)
                # distance away from 20 (peak blue value) is subtracted from 255 (max color value)
                blue = int(round(bluefloat))
            elif (n > 30):
                blue = 0
        elif (n < 10):
            blue = 0
        if (n > 25):
        # green will have a value when distance is greater than 25
            G = abs (35 - n)
            greenfloat = (255 - G*25.5)
            # distance away from 35 (peak blue value) is subtracted from 255 (max color value)
            green = int(round(greenfloat))
        elif (n < 25):
            green = 0
        print (sonar.distance)
        print (red, green, blue)
        color = (red, green, blue)
        # color is mixture of red, green, and blue values
        dot.fill (color)
        # color the neopixel
    except:
        # when distance can't be found, say nothing, and try again (don't give error)
        print ("")
    time.sleep (0.01)