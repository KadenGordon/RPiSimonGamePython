from time import sleep as wait #for timing
from GPIO import LED, Button #my own GPIO device classes
from SimonClass import SimonGame
import RPi.GPIO as GPIO


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


#set stuff up for a timer
timeBetweenPresses = 750
timeToPress = timeBetweenPresses
#loop
game.start()
wait(3)
try:
	#forever
	while True:
		position = 0
		pattern = game.createLevel(game.level)
		game.flashPattern(pattern)
		#play level
		while position <= len(pattern):
			goal = pattern[position]
			keys = game.getKeys()
			i = position
			
			for button in range(0,len(pattern) + 1):
			#check if it's the right one, if it is, move on to next position, else game over.
				if game.Buttons[button].isPressed():
					if keys[position] == game.Buttons[position]:
						position += 1
						print "did a thing"
					else: 
						print "fail " + str(button)
				print 
			

		#this is basically my timer
		timeToPress += 10
		wait(0.01)
except KeyboardInterrupt:
	#for LED in cleanups:
	#    object.cleanup()
	#   print(object)
	pass
except SystemExit:
	GPIO.cleanup()
