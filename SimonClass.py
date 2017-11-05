import RPi.GPIO as GPIO 
from GPIO import LED, Button
import random
import math
from time import sleep as wait

class SimonGame(object):
	def __init__(self, leds, buttons):
		#Pass the LEDs as a dict, please.
		
		#let's create the LEDs
		#Okay. Personally, this is gross. Please don't use this lol
		self.LED = []
		for i in range(1, 4):
			self.LED.append(LED(leds[i]))
			
		# self.tlLED = LED(leds[1])
		# self.trLED = LED(leds[2])
		# self.brLED = LED(leds[3])
		# self.blLED = LED(leds[4])
		#okay. Now the buttons
		self.Button = []
		for i in range(1, 4):
			self.Button.append(Button(buttons[i]))
		
		#self.tlButton = Button(tlButtonpin)
		#self.trButton = Button(trButtonpin)
		#self.brButton = Button(brButtonpin)
		#self.blButton = Button(blButtonpin)
		#now for some variables
		self.score = 0
		self.gameIndex = 0
		self.level = 1
		self.pattern = []
		alive = True
		#lets make some looping easier
		# self.LEDs = [self.tlLED,self.trLED,self.brLED,self.blLED]
		# self.Buttons = [self.tlButton,self.trButton,self.brButton,self.blButton]
		
	 
	def start(self):
		self.startSequence()
		self.score = 0
		self.gameIndex = 0


	def createLevel(self):
		self.pattern.append(random.randint(0,3))

	def startSequence(self):
		for i in range(0,8):
			LED = self.LED[i%4]
			LED.turnOn()
			wait(0.1)
			LED.turnOff()
		wait(0.15)
		for LED in self.LED:
			LED.turnOn()
		wait(1)
		for LED in self.LED:
			LED.turnOff()

	def cleanup(self):
		for LED in self.LED:
			LED.cleanup()
		for Button in self.BUTTON:
			Button.cleanup()

	def getKeys(self):
		keys = [0,0,0,0]
		i = 0
		for button in self.BUTTON:
			keys[i] = button.isPressed()
			i += 1
		return keys

	def gameOver(self):
		pass

	def turnOffLEDs(self):
		for LED in self.LED:
			LED.turnOff()

	def flashPattern(self, pattern):
		for flash in pattern:
			print flash
			LED = self.LED[flash]
			LED.turnOn()
			wait(0.6)
			LED.turnOff()
			wait(0.2)
