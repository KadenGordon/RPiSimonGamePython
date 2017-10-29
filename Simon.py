import time #for timing
from GPIO import LED, Button #my own GPIO pin classes
from SimonClass import SimonGame

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
		while position <= len(pattern)
			pattern = game.createLevel(level)
			goal = pattern[position]
			keys = game.getKeys()
			for button in game.Buttons:
				if button.isPressed():


		#this is basically my timer
		timeToPress += 1
		time.sleep(0.001)
except KeyboardInterrupt:
	for LED in cleanups:
	#    object.cleanup()
	#   print(object)
	pass
except SystemExit:
	GPIO.cleanup()
