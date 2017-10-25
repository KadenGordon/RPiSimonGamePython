import RPi.GPIO as GPIO 
from GPIO import LED, Button
import random
import math

class SimonGame(object):
	def __init__(self, tlLED, trLED, blLED, brLED, tlButton, trButton, blButton, brButton):
		#let's create the LEDs
		self.TlLED = LED(tlLED)
		self.TrLED = LED(trLED)
		self.BlLED = LED(blLED)
		self.BrLED = LED(brLED)
		#okay. Now the buttons
		self.TlButton = Button(tlButton)
		self.TrButton = Button(trButton)
		self.BlButton = Button(blButton)
		self.BrButton = Button(brButton)
		#now for some variables
		self.score = 0
		self.gameIndex = 0
		self.level = 0
		self.levelPattern = []
		self.alive = True
		#lets make some looping easier
		self.LEDs = [TlLED,TrLED,BlLED,BrLED]
		self.Buttons = [TlButton,TrButton,BlButton,BrButton]
		
	
	def start(self):
		self.startSequence()
		self.score = 0
		self.gameIndex = 0


	def createLevel(self, level):
		pattern = []
		for i in range (1,level):
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