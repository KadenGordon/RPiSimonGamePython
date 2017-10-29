import RPi.GPIO as GPIO

class LED:
    def __init__(self, port):
        pin = port
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        
        ON = False
        OFF = True
        
    def turnOn(self):
        GPIO.output(pin, ON)
    
    def turnOff(self):
        GPIO.output(pin, OFF)
        
    def cleanup(self):
        GPIO.cleanup(pin)

    def getPin(self):
        return pin 
        
class Button:
    def __init__(self, port):
        pin = port
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def isPressed(self):
        return not GPIO.input(pin)
    
    def cleanup(self):
        GPIO.cleanup(pin)

    def getPin(self):
        return pin