from digitalio import DigitalInOut, Direction  #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
# the "#pylint: disable-msg=import-error" message is necessary on all CircuitPython specific modules, like digitalio and board
import time 
import random
# import the random module
a = 0
b = 0
c = 0
s = 0
# each function has been run 0 times
values = [True, False]
# a list of values to be chosen from for the random.choice function
class FancyLED(object):
    def __init__(self, LED1, LED2, LED3):
    # the two sets of LEDs are initalized with the three pins of the individual LEDs 
        self.LED1 = DigitalInOut(LED1)
        self.LED1.direction = Direction.OUTPUT
        self.LED2 = DigitalInOut(LED2)
        self.LED2.direction = Direction.OUTPUT
        self.LED3 = DigitalInOut(LED3)
        self.LED3.direction = Direction.OUTPUT

    def alternate(self):
        for a in range (0, 5, 1):
            # when the counter is between 0 and 5 (allows you to run loop 5 times before moving on to next function)
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = True
            # turn on just the outside LEDs...
            time.sleep(0.5)
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            #...then just the middle LED
            time.sleep(0.5)
            self.LED2.value = False
            # turn off the middle LED so it doesn't stay on in the next loop
            a = a + 1 
            # the loop has been run 1 more time

    def blink (self):
        for b in range (0, 5, 1):
            self.LED1.value = True
            self.LED2.value = True
            self.LED3.value = True
            # all LEDs are on
            time.sleep (0.5)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = False
            # all LEDs are off
            time.sleep (0.5)
            b = b + 1 

    def chase (self):
        for c in range (0, 5, 1):
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = False
            # turn on just the first LED...
            time.sleep (0.2)
            # sleep less to create chasing effect
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            #...then just the second...
            time.sleep (0.2)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = True
            #...then just the third
            time.sleep (0.2)
            c = c + 1 
    
    def sparkle (self):
        for s in range (0, 20, 1):
        # loop runs 20 times instead of 5
            self.LED1.value = random.choice (values)
            self.LED2.value = random.choice (values)
            self.LED3.value = random.choice (values)
            # randomly turn each LED on or off
            time.sleep (0.3)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = False
            # then turn all LEDs off to reset
            s = s + 1
            
