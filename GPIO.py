import RPi.GPIO as GPIO

class LED:
    def __init__(self, port):
        self.pin = port
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.ON = False
        self.OFF = True
        
    def turnOn(self):
        GPIO.output(self.pin, self.ON)
    
    def turnOff(self):
        GPIO.output(self.pin, self.OFF)
        
    def cleanup(self):
        GPIO.cleanup(self.pin)

    def getPin(self):
        return self.pin 
        
class Button:
    def __init__(self, port):
        self.pin = port
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def isPressed(self):
        return not GPIO.input(self.pin)
    
    def cleanup(self):
        GPIO.cleanup(self.pin)

    def getPin(self):
        return self.pin