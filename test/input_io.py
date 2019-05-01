# This file declares a class to use GPIO pins as inputs


# importing libraries
import Adafruit_BBIO.GPIO as GPIO


# declaring Input_io class to handle GPIO inputs
class Input_io():

    # intitial class function
    def __init__(self, pin, read_state):
        # pin: dictionary containing used input pin
        # read_state: rise, fall, both
        self.sig = pin["sig"]
        if read_state == "rise":
            self.edge = GPIO.RISING
            self.initial = GPIO.LOW
        elif read_state == "fall":
            self.edge = GPIO.FALLING
            self.initial = GPIO.HIGH
        elif read_state == "both":
            self.edge = GPIO.BOTH

    # function to initialize pin
    def init_pin(self):
        GPIO.setup(self.sig, GPIO.IN, self.initial)
        GPIO.add_event_detect(self.sig, self.edge)

    # function to read input
    def read(self):
    	return GPIO.input(self.sig)

    # function to detect event
    def event(self):
        GPIO.event_detected(self.sig)

    # function to clean up pin
    def cleanup(self):
        GPIO.remove_event_detect(self.sig)
        GPIO.cleanup()

