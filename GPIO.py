import RPi.GPIO as GPIO
from time import sleep as wait

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
        self.pressed = 0
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.pressed) 
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.released())

    def pressed(self):
        #this runs in a seperate thread thank god
        self.pressed = 1

    def released(self):
        self.pressed = 0

    def isPressed(self):
        return self.pressed
    
    def cleanup(self):
        GPIO.cleanup(self.pin)

    def getPin(self):
        return self.pin

    def waitUntilNotPressed(self):
        while self.isPressed():
            pass
        wait(0.005)
