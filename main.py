import machine
import time
from setup import *
from calibrate import *
from measureSensor import *

components = setup() #setup the sensors
components[1].value(1) #turn on LED to indicate that it is connected
components[2].value(1) #turn on embedded LED to indicate calibration

while True: #calibrate the light-to-voltage sensor
    if components[3].value() == 1 #if the button is pressed, do the calibration
        blank = calibrate(components[0]) #define the calibration value
        components[1].value(0) #turn off LED
        components[2].value(0) #turn off embedded LED
        break
    else:
        pass

while True: #now do some measurements...


        