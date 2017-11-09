#!/usr/bin/env python
import sys
import time
import traceback
#from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO		# imports the Rasp GPIO module (General Purpose Input/Output)

pinnr = 21			# GPIO pin number

def setupGPIO():
	try:
		#GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
		GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type

		GPIO.setwarnings(False)

		GPIO.setup(pinnr, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		#GPIO.setup(pinnr, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	except Exception as ex:
		traceback.print_exc()
	finally:
		GPIO.cleanup() #this ensures a clean exit

def readPin(pin):
	value = GPIO.input(pin)
	return value

setupGPIO()
while(1):
	state = readPin(pinnr)
	if state == True:
		print("Pin is HIGH\n")
	else:
		print("Pin is LOW\n")
	time.sleep(1)