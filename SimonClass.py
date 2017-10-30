import RPi.GPIO as GPIO 
from GPIO import LED, Button
import random
import math
from time import sleep as wait

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
		self.level = 1
		self.levelPattern = []
		alive = True
		#lets make some looping easier
		self.LEDs = [self.tlLED,self.trLED,self.brLED,self.blLED]
		self.Buttons = [self.tlButton,self.trButton,self.brButton,self.blButton]
		
	
	def start(self):
		self.startSequence()
		self.score = 0
		self.gameIndex = 0


	def createLevel(self, level):
		pattern = []
		for i in range (0,level + 1):
			pattern.append(random.randint(0,3))
		return pattern

	def startSequence(self):
		for i in range(0,8):
			LED = self.LEDs[i%4]
			LED.turnOn()
			wait(0.1)
			LED.turnOff()
		wait(0.15)
		for LED in self.LEDs:
			LED.turnOn()
		wait(1)
		for LED in self.LEDs:
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
			keys[i] = button.isPressed()
			i += 1
		return keys

	def gameOver(self):
		pass

	def turnOffLEDs(self):
		for LED in self.LEDs:
			LED.turnOff()

	def flashPattern(self, pattern):
		for flash in pattern:
			print flash
			LED = self.LEDs[flash]
			LED.turnOn()
			wait(1)
			LED.turnOff()
