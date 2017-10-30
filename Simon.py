from time import sleep as wait #for timing
from GPIO import LED, Button #my own GPIO device classes
from SimonClass import SimonGame
import RPi.GPIO as GPIO
print GPIO.RPI_INFO
GPIO.setmode(GPIO.BOARD)
#creates game object with these pins
game = SimonGame(
	3,  #Top Left LED
	5,  #Top Right LED
	8,  #Bottom Right LED
	10, #Bottom Left LED
	11, #Top Left Button
	13, #Top Right Button
	16, #Bottom Right Button
	18) #Bottom Left Button

game.turnOffLEDs()
wait(3)
#stuff to start the game
level = 1
position = 0
#set stuff up for a timer
timeBetweenPresses = 750
timeToPress = timeBetweenPresses
#loop
game.start()
try:
	#forever
	while True:
		pattern = game.createLevel(level)
		#play level
		while position <= len(pattern):
			goal = pattern[position]
			keys = game.getKeys()
			for button in keys:
				#check if it's the right one, if it is, move on to next position, else game over.
				if button and keys[button] == pattern[position]:
					pass

		#this is basically my timer
		timeToPress += 1
		wait(0.001)
except KeyboardInterrupt:
	#for LED in cleanups:
	#    object.cleanup()
	#   print(object)
	pass
except SystemExit:
	GPIO.cleanup()
