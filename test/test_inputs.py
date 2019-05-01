# This is test code for reading inputs from test code


# importing libraries
from input_io import Input_io
import Adafruit_BBIO.GPIO as GPIO
import config
import time

# initializing  classes
print("Initializing Classes")
near_switch = Input_io(config.limit_near_pin, "fall")
far_switch = Input_io(config.limit_far_pin, "fall")

# initializing pins
print("Initializing Pins")
near_switch.init_pin()
far_switch.init_pin()

# confirming power
input("Press any key after motors are connected to power.")

# reading inputs
for x in range(30):
    print("Near switch: ", near_switch.read())
    print("Far switch: ", far_switch.read(), "\n")
    # print("Near switch: ", GPIO.input(config.limit_near_pin["sig"]))
    # print("Far switch: ", GPIO.input(config.limit_far_pin["sig"]), "\n")
    time.sleep(1)

# cleaning up pins
print("Cleaning up pins.")
near_switch.cleanup()
far_switch.cleanup()