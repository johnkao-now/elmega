import RPi.GPIO as GPIO


class Control(object):
    def __init__():
        GPIO.setmode(GPIO.BCM)

    def motor_mode(self):
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(22,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)

    def forward(self):
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(23,GPIO.LOW)

    def back(self):
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)

    def left(self):
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)

    def right(self):
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(23,GPIO.LOW)
        