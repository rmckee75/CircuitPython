import board
# imports breadboard
import pulseio
# imports PWM
import time
# most functions must be imported from modules before they can be used (even breadboard and time)
led = pulseio.PWMOut(board.D4)
# the LED is attached to digital pin 4 (a PWM pin)
i = 0
# duty_cycle starts at 0...
j = 10
# ...and goes up by 10
print("Make it red!")

while True:
# equivalent of void loop ()
    led.duty_cycle = i
    # the duty_cycle is the brightness
    time.sleep(0.0000001)
    # wait a very small amount of time
    print (i)
    i = i + j
    # brightness (duty_cycle) changes by 10 each time
    if (i == 65530 or i == 0):
        j = -j
        # when brightness reaches 0 or 65530 (max value), switch directions







