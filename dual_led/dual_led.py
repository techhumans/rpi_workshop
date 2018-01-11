#!/usr/bin/env python2

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

if sys.argv[1] == '1':
    GPIO.output(7, True)
elif sys.argv[1] == '2':
    GPIO.output(11, True)


raw_input('press enter to continue...')

GPIO.output(7, False)
GPIO.output(11, False)
