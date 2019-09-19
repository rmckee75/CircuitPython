import time
import board
import pulseio
import touchio
from adafruit_motor import servo
pwm = pulseio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency = 50)
my_servo = servo.Servo(pwm)
touch1 = touchio.TouchIn(board.A1)
touch4 = touchio.TouchIn(board.A4)
i = 5
j = 5

while True:
    my_servo.angle = i
    if touch1.value and i < 180:
        i = i + j
    if touch4.value and i > 0:
        i = i - j
    print (i)
    time.sleep (0.1)










