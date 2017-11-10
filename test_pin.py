#!/usr/bin/env python
import sys
import time
#from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO		# imports the Rasp GPIO module (General Purpose Input/Output)

pinnr1 = 21			# GPIO pin number
pinnr2 = 26			# GPIO pin number

def setupGPIO():
	print ("Setting up the GPIO pins\n")
	#GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
	GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type

	GPIO.setwarnings(False)

	#GPIO.setup(pinnr, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(pinnr1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(pinnr2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def readPin(pin):
	value = GPIO.input(pin)
	return value

setupGPIO()
i = 100
while(i>1):
	print("reading state:....")
	
	state1 = readPin(pinnr1)
	if state1 == True:
		print("Pin1 is HIGH\n")
	else:
		print("Pin1 is LOW\n")

	state2 = readPin(pinnr2)
	if state2 == True:
		print("Pin2 is HIGH\n")
	else:
		print("Pin2 is LOW\n")
	
	time.sleep(1)
	i -= 1

print ("cleanup pins")
GPIO.cleanup() #this ensures a clean exit
sys.exit()