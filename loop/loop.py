#!/usr/bin/env python2

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

led_list = [7, 11]

for led in led_list:
    GPIO.output(led, True)
    time.sleep(1)

    GPIO.output(led, False)
    time.sleep(1)
