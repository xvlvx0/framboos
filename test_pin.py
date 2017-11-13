#!/usr/bin/env python
import sys
import time
#from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO		# imports the Rasp GPIO module (General Purpose Input/Output)

pinnr1 = 19			# GPIO pin number
pinnr2 = 21			# GPIO pin number
pinnr3 = 26			# GPIO pin number

def setupGPIO():
	print ("Setting up the GPIO pins\n")
	#GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
	GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type

	GPIO.setwarnings(False)

	#GPIO.setup(pinnr, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	#GPIO.setup(pinnr1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(pinnr1, GPIO.IN)
	GPIO.setup(pinnr2, GPIO.IN)
	GPIO.setup(pinnr3, GPIO.IN)

def readPin(pin):
	value = GPIO.input(pin)
	return value

setupGPIO()
print("reading state:....")
while(1):
	state1 = readPin(pinnr1)
	state2 = readPin(pinnr2)
	state3 = readPin(pinnr3)

	print("Pin1 is %,\tPin2 is %,\tPin3 is %.\n", str(state1), str(state2), str(state3))
	
	time.sleep(1)

print ("cleanup pins")
GPIO.cleanup() #this ensures a clean exit
sys.exit()