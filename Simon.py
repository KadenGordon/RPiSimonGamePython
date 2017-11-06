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
#stuff to start the game

game.start()
wait(1)
#loop
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
					game.gameOver()
					print "fail " + str(button)
					break
				button.waitUntilNotPressed()
			else:
				game.LEDs[buttonpos].turnOff()
			i += 1
		print "LEVEL COMPLETE"
		game.level += 1
		game.turnOffLEDs()
		wait(1)

except KeyboardInterrupt:
	GPIO.cleanup()
except SystemExit:
	GPIO.cleanup()
