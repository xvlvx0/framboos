#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time
#from EmulatorGUI import GPIO	# imports the GPIO emulator, for testing only
import RPi.GPIO as GPIO			# imports the Rasp GPIO module (General Purpose Input/Output)

LEDpinOne = 6
LEDpinTwo = 21

def setupGPIO():
	try:
		GPIO.setmode(GPIO.BOARD) 		# sets input to unified board pin numbers
		#GPIO.setmode(GPIO.BCM)			# sets input to chip numbers, can differ per poard type

		GPIO.setwarnings(False)

		GPIO.setup(LEDpinOne, GPIO.OUT, initial = GPIO.HIGH)
		GPIO.setup(LEDpinTwo, GPIO.OUT, initial = GPIO.LOW)

		while(True):
			GPIO.output(LEDpinOne,GPIO.HIGH)
			GPIO.output(LEDpinTwo,GPIO.HIGH)
			time.sleep(10)
			GPIO.output(LEDpinOne,GPIO.LOW)
			GPIO.output(LEDpinTwo,GPIO.LOW)
	except Exception as ex:
		traceback.print_exc()
	finally:
		GPIO.cleanup() #this ensures a clean exit


sys.exit()