#!/usr/bin/env python2

from bottle import route, run, static_file
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)


@route('/')
def home():
    return static_file('index.html', root='./')


@route('/one')
def led_one():
    state = GPIO.input(7)
    GPIO.setup(7, GPIO.OUT)

    if state == True:
        GPIO.output(7, False)
    else:
        GPIO.output(7, True)


@route('/two')
def led_two():
    state = GPIO.input(11)
    GPIO.setup(11, GPIO.OUT)

    if state == True:
        GPIO.output(11, False)
    else:
        GPIO.output(11, True)


run(host='0.0.0.0', port=8080)
