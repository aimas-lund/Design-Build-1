import time
from setup import *
from calibrate import *
from measure import *
import math

comp = setup() #setup components
adc = comp[0]
pwm = comp[1]
b1 = comp[2]
b2 = comp[3]
red = comp[4]
green = comp[5]
blue = comp[6]
green.value(1)
blue.value(1)
red.value(0) #red light before the program is initialized
cBool = False

while True:  # wait for THE BUTTON to be pressed
    if b1.value() == 0:
        if cBool == False:
            init = 2597.82 #if no calibration, set to preset calibration
            current = 330
        else:
            pass
        break
    elif b2.value() == 0: #if 2nd button is pressed, the sensor is calibrated to the current blank
        c = calibrate() #calibrate sensor
        init = c[0]
        current = c[1]
        green.value(0) #turn the LED yellow, if there has been a calibration
        cBool = True
        time.sleep(2)
    else:
        pass

file = open("data.csv", "w")
green.value(0)
red.value(1)
time.sleep(2)
cycle = 0 #a cycle is ~1 second
file.write("Time,ADC Value,Std Deviation,Calibrated OD\n")
while (b1.value() == 1) and (cycle <= 43200): #continue until the button is pushed or when 12 hours worth of data is reached
    blue.value(1)
    if cycle % 30 == 0:
        green.value(1)
        blue.value(0) #flash blue when measurements are made
        data = measure(current, init)
        OD = -1*(math.log10(data[0]/init)) #calculate OD
        ODcali = 4.9905*OD + 0.0396 #change OD to calibrated value
        file.write("{},{},{},{}\n".format(cycle,data[0],data[1],ODcali))
    elif cycle % 2 == 0: #blink green every other second
        if green.value() == 0:
            green.value(1)
        else:
            green.value(0)
    else:
        pass
    time.sleep(1) #wait a second between every cycle
    cycle += 1

file.close() #close file
green.value(1)
blue.value(1)
red.value(0)
time.sleep(2)
red.value(1)
