# CircuitPython

My CircuitPython assignments

## Hello CircuitPython (and Metro and Mu)
### Objective
Use the CircuitPython coding language and Metro M0 Express to code a LED to fade in and out
### Wiring
![alt text](ledfadewiring.PNG)
### Lessons Learned
In this assignment, I learned that the easiest way to code an LED is with a PWM (pulse width moderator) pin.  PWM pins change the percentage of time that the LED is on (duty cycle), which makes it appear as if the brightness is fading in and out.  I also learned the basics of CircuitPython coding language, such as the fact that you have to import modules for most functions, and that while True takes the place of void loop ().

## CircuitPython Servo
### Objective
Using capacitive touch, the 180 micro servo should rotate in one direction when touching one wire, and in the other direction when touching the other### Wiring
![alt text](servowiring.PNG)
### Lessons Learned
In this assignment, I learned that PWM and duty cycles can also be used for servos, and that using the touchio module, your metro can tell when you are touching a wire.

## CircuitPython LCD
### Objective
The LCD screen should count the number of times a button has been pressed, and the direction of counting should be determined by a switch
### Wiring
![alt text](lcdwiring.PNG)
### Lessons Learned
In this assignment, I learned that Metro reads buttons and switches by reading the voltage, so you need to start with them "pulled up" and the Metro will detect when they have been pressed/switched because the voltage will change.  Additionally, I used boolean values (True and False) to prevent the count from going up while the button was pressed down.  If you turn the boolean to True when the button is pressed, and ensure that the count only goes up when the boolean is False, the boolean will have to be unpressed and pressed again for the count to go up.
