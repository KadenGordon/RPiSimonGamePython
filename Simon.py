from time import sleep as wait #for timing
from GPIO import LED, Button #my own GPIO device classes
from SimonClass import SimonGame
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
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
		game.createLevel()
		game.flashPattern(game.pattern)
		#play level
		i = 0
		while position < len(game.pattern):
			goal = game.pattern[position]
			keys = game.getKeys()
			#check if it's the right one, if it is, move on to next position, else game over.
			buttonpos = i%4
			button = game.Buttons[buttonpos]
			if button.isPressed():
				game.LEDs[buttonpos].turnOn()
				if game.Buttons[goal].isPressed():
					position += 1
					print "did a thing"

				else: 
					print "fail " + str(button)
			else:
				game.LEDs[buttonpos].turnOff()
			i += 1
			wait(0.05)
		print "LEVEL COMPLETE"
		game.level += 1
		wait(1)
			

		#this is basically my timer
		timeToPress += 100
		wait(0.1)
except KeyboardInterrupt:
	#for LED in cleanups:
	#    object.cleanup()
	#   print(object)
	pass
except SystemExit:
	GPIO.cleanup()
