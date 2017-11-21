#!/usr/bin/env python
import sys
import time
#from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO		# imports the Rasp GPIO module (General Purpose Input/Output)

pinnr1 = 19			# GPIO pin number
pinnr2 = 21			# GPIO pin number
pinnr3 = 26			# GPIO pin number
pins = {pinnr1, pinnr2, pinnr3}

def setupGPIO_IN(pins):
	print ("Setting up the GPIO pins\n")
	#GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
	GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type
	GPIO.setwarnings(False)

	for pin in pins:
		GPIO.setup(pin, GPIO.IN)

	#GPIO.setup(pinnr1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	#GPIO.setup(pinnr2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	#GPIO.setup(pinnr1, GPIO.IN)
	#GPIO.setup(pinnr2, GPIO.OUT)

def readPin(pin):
	value = GPIO.input(pin)
	return value

setupGPIO()
print("reading state:....")
counter = 0
while(counter < 120):
	for pin in pins:
		state = readPin(pinn)
		print(str(counter) + " - " + str(state1))
	
	time.sleep(0.5)
	counter += 1

print ("cleanup pins")
GPIO.cleanup() #this ensures a clean exit
sys.exit()