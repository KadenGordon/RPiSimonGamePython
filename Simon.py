import RPi.GPIO as GPIO #for GPIO functions not directly related to LEDs and buttons
import time #for timing
from GPIO import LED, Button #my own GPIO pin classes
from SimonClass import SimonGame

GPIO.setmode(GPIO.BOARD)

#creates game object with these pins
game = SimonGame(
	3,
	5,
	8,
	10,
	11,
	13,
	16,
	18)



#set stuff up for a timer
timeBetweenPresses = 750
timeToPress = timeBetweenPresses
#loop
try:
    #forever
    while True:
        
        
        #this is basically my timer
        timeToPress += 1
        time.sleep(0.001)
except KeyboardInterrupt:
    #for object in cleanups:
    #    object.cleanup()
    #   print(object)
    
except SystemExit:
    GPIO.cleanup()
