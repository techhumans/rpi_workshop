#!/usr/bin/env python2

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)

led_dict = {
    'led_one': 7,
    'led_two': 11
}

GPIO.setup(led_dict['led_one'], GPIO.OUT)
GPIO.setup(led_dict['led_two'], GPIO.OUT)

if sys.argv[1] == '1':
    GPIO.output(led_dict['led_one'], True)
elif sys.argv[1] == '2':
    GPIO.output(led_dict['led_two'], True)


raw_input('press enter to continue...')

GPIO.output(led_dict['led_one'], False)
GPIO.output(led_dict['led_two'], False)
