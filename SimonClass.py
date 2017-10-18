import RPi.GPIO as GPIO 
from GPIO import LED, Button

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
			self.type.Button = GPIO.IN 
			self.type.LED = GPIO.OUT
			self.on = False
			self.off = True
			