from pulseio import PWMOut
class RGB(object):
    def __init__ (self, Rpin, Gpin, Bpin):
        self.Rpin = PWMOut (Rpin, duty_cycle = 65535, frequency = 500)
        self.Gpin = PWMOut (Gpin, duty_cycle = 65535, frequency = 500)
        self.Bpin = PWMOut (Bpin, duty_cycle = 65535, frequency = 500)
    def red (self):
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 65535
    def blue (self):
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 0
    def green (self):
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 65535
    def cyan (self):
        self.Rpin.duty_cycle = 65535
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 0
    def magenta (self):
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 65535
        self.Bpin.duty_cycle = 0
    def yellow (self):
        self.Rpin.duty_cycle = 0
        self.Gpin.duty_cycle = 0
        self.Bpin.duty_cycle = 65535