import RPi.GPIO as GPIOControl

class LED:
    def __init__(self, port):
        pin = port
        #GPIOControl.setmode(GPIOControl.BOARD)
        GPIOControl.setup(pin, GPIOControl.OUT)
        
        ON = False
        OFF = True
        
    def turnOn(self):
        GPIOControl.output(pin, ON)
    
    def turnOff(self):
        GPIOControl.output(pin, OFF)
        
    def cleanup(self):
        GPIOControl.cleanup(pin)

    def getPin(self):
        return pin 
        
class Button:
    def __init__(self, port):
        pin = port
        #GPIOControl.setmode(GPIOControl.BOARD)
        GPIOControl.setup(pin, GPIOControl.IN, pull_up_down=GPIOControl.PUD_UP)
        
    def isPressed(self):
        return not GPIOControl.input(pin)
    
    def cleanup(self):
        GPIOControl.cleanup(pin)

    def getPin(self):
        return pin