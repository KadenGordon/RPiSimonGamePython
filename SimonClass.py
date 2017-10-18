import RPi.GPIO as GPIO 
from GPIO import LED, Button
import random
import math

class SimonGame(object):
	def __init__(self, upLED, rightLED, downLED, leftLED, upButton, rightButton, downButton, leftButton):
		#let's create the LEDs
		self.UpLED = LED(upLED)
		self.RightLED = LED(RightLED)
		self.DownLED = LED(downLED)
		self.LeftLED = LED(leftLED)
		#okay. Now the buttons
		self.UpButton = Button(upButton)
		self.RightButton = Button(rightButton)
		self.DownButton = Button(downButton)
		self.LeftButton = Button(leftButton)
		#now for some variables
		self.score = 0
		self.game_index = 0
		#lets make some looping easier
		self.LEDs = [UpLED,RightLED,DownLED,LeftLED]
		self.level = 0
		self.pattern = []
		self.alive = True
	def start(self):
		self.startSequence()
		self.score = 0
		self.game_index = 0
		while self.alive:
			self.createLevel(level)
			self.createLevel += 1

		
	def createLevel(self, level):
		self.pattern = []
		for i in range (1,level):
			self.pattern.append(random.randint(1,4))

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
