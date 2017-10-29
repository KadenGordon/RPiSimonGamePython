import RPi.GPIO as GPIO 
from GPIO import LED, Button
import random
import math

class SimonGame(object):
	def __init__(self, tlLEDpin, trLEDpin, brLEDpin, blLEDpin, tlButtonpin, trButtonpin, brButtonpin, blButtonpin):
		#let's create the LEDs
		self.tlLED = LED(tlLEDpin)
		self.trLED = LED(trLEDpin)
		self.brLED = LED(brLEDpin)
		self.blLED = LED(blLEDpin)
		#okay. Now the buttons
		self.tlButton = Button(tlButtonpin)
		self.trButton = Button(trButtonpin)
		self.brButton = Button(brButtonpin)
		self.blButton = Button(blButtonpin)
		#now for some variables
		self.score = 0
		self.gameIndex = 0
		self.level = 0
		self.levelPattern = []
		alive = True
		#lets make some looping easier
		self.LEDs = [tlLED,trLED,brLED,blLED]
		self.Buttons = [tlButton,trButton,brButton,blButton]
		
	
	def start(self):
		self.startSequence()
		self.score = 0
		self.gameIndex = 0


	def createLevel(self, level):
		pattern = []
		for i in range (0,level):
			pattern.append(random.randint(1,4))
		return pattern

	def startSequence(self):
		for i in range(1,5):
			LED = self.LEDs[i%4]
			LED.turnOn()
			wait(0.5)
			LED.turnOff()
		for LED in LEDs:
			LED.turnOn()
		wait(1)
		for LED in LEDs:
			LED.turnOff()

	def cleanup(self):
		for LED in self.LEDs:
			LED.cleanup()
		for Button in self.Buttons:
			Button.cleanup()

	def getKeys(self):
		keys = [0,0,0,0]
		i = 0
		for button in self.Buttons:
			keys[i] = button.isPresseed()
			i += 1
		return keys

	def gameOver(self):
		pass

	def 

	