import time
import board
import pulseio
import touchio
# imports the capacitive touch function
from adafruit_motor import servo
pwm = pulseio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency = 50)
# servo is plugged into digital pin 3
# sets duty_cycle (percentage of time pulses are high) and frequency (of pulses)
my_servo = servo.Servo(pwm)
touch1 = touchio.TouchIn(board.A1)
touch4 = touchio.TouchIn(board.A4)
# the two capacitive touch wires are
i = 5
j = 5

while True:
    my_servo.angle = i
    if touch1.value and i < 180:
        i = i + j
    if touch4.value and i > 0:
        i = i - j
    # when a wire is touched the servo switches direction
    # servo must remain in range (0 - 180 degrees)
    print (i)
    time.sleep (0.1)









