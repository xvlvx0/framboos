#!/usr/bin/env python
import sys
import time
#from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO		# imports the Rasp GPIO module (General Purpose Input/Output)

conn01 = 18			# GPIO pin number
conn02 = 23			# GPIO pin number
conn03 = 24			# GPIO pin number
conn04 = 25			# GPIO pin number
conn05 = 12			# GPIO pin number
conn06 = 5			# GPIO pin number
conn07 = 19			# GPIO pin number
conn08 = 13			# GPIO pin number
conn09 = 6			# GPIO pin number
conn10 = 26			# GPIO pin number
conn11 = 22			# GPIO pin number
conn12 = 27			# GPIO pin number
conn13 = 17			# GPIO pin number
conn14 = 4			# GPIO pin number
pins = { conn01, conn02, conn03, conn04,
		conn05, conn06, conn07, conn08,
		conn09, conn10, conn11, conn12,
		conn13, conn14 }

def setupGPIO_INPUT(pins):
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

setupGPIO_INPUT(pins)
print("reading state:....")
counter = 0
while(counter < 120):
	for pin in pins:
		state = readPin(pin)
		print(str(counter) + " - " + str(state))
	
	time.sleep(0.5)
	counter += 1

print ("cleanup pins")
GPIO.cleanup() #this ensures a clean exit
sys.exit()