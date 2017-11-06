from time import sleep as wait #for timing
from GPIO import LED, Button #my own GPIO device classes
from SimonClass import SimonGame
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#creates game object with these pins
#first parameter passed is an array containing all LED pins, etc.
game = SimonGame([3, 5, 8, 10], [11, 13, 16, 18])

## LEDS:
#3: Top Left LED, 5: Top Right LED, 8: Bottom Right LED, 10: Bottom Left LED
## Buttons:
#11: Top Left Button, 13: Top Right Button, 16: Bottom Right Button, 18: Bottom Left Button

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
			button = game.Button[buttonpos]
			if button.isPressed():
				game.LED[buttonpos].turnOn()
				if game.Button[goal].isPressed():
					position += 1
					print "did a thing"

				else: 
					game.gameOver()
					print "fail " + str(button)
					break
				button.waitUntilNotPressed()
			else:
				game.LED[buttonpos].turnOff()
			i += 1
		print "LEVEL COMPLETE"
		game.level += 1
		game.turnOffLEDs()
		wait(1)

except KeyboardInterrupt:
	GPIO.cleanup()
except SystemExit:
	GPIO.cleanup()
