# Write your code here :-)
import board
import pulseio
import time
led = pulseio.PWMOut(board.D4)
i = 0
j = 10
print("Make it red!")

while True:
    led.duty_cycle = i
    time.sleep(0.0000001)
    print (i)
    i = i + j
    if (i == 65530 or i == 0):
        j = -j








