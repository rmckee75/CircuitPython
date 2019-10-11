from pulseio import PWMOut #pylint: disable-msg=import-error
# import the PWMOut class from the pulseio module
class RGB(object):
    def __init__ (self, Rpin, Gpin, Bpin):
    # the object (RGB LED) is initialized with a a red, green, and blue pins
        self.Rpin = PWMOut (Rpin, duty_cycle = 65535, frequency = 500)
        self.Gpin = PWMOut (Gpin, duty_cycle = 65535, frequency = 500)
        self.Bpin = PWMOut (Bpin, duty_cycle = 65535, frequency = 500)
        # each pin is a PWM pin, and they all start off
    def red (self):
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 65535
        # when there is power, the pins defualt value is on, so turning them to 65535 turns them off, not on
    def blue (self):
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 0
    def green (self):
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 65535
    def cyan (self):
        # green + blue
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 0
    def magenta (self):
        # red + blue
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 0
    def yellow (self):
        # red + green
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 65535
