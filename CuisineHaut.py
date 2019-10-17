#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #monter  chp
GPIO.setup(23, GPIO.OUT) #descente chp

GPIO.output(18, GPIO.LOW) #monter on
GPIO.output(23, GPIO.HIGH) #descente off
