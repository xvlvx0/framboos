#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time
import traceback
from GPIOEmulator.EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
#import RPi.GPIO as GPIO			# imports the Rasp GPIO module (General Purpose Input/Output)

LEDpinOne = 6
LEDpinTwo = 21
print("Starting the LED test")

def setupGPIO():
	try:
		GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
		#GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type

		GPIO.setwarnings(False)

		GPIO.setup(LEDpinOne, GPIO.OUT, initial = GPIO.HIGH)
		GPIO.setup(LEDpinTwo, GPIO.OUT, initial = GPIO.LOW)

		counter = 10
		while(counter>1):
			print ("Counter: " + str(counter) + "\n")

			GPIO.output(LEDpinOne,GPIO.HIGH)
			GPIO.output(LEDpinTwo,GPIO.HIGH)
			
			time.sleep(10)
			
			GPIO.output(LEDpinOne,GPIO.LOW)
			GPIO.output(LEDpinTwo,GPIO.LOW)
			
			counter -= 1
	except Exception as ex:
		traceback.print_exc()
	finally:
		GPIO.cleanup() #this ensures a clean exit

def main():
	print("Going to blink....")
	setupGPIO()
	print("....exit")
	sys.exit()	


if __name__ == '__main__':
	main()
