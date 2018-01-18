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
emb = comp[7]
red.value(1)
blue.value(1)
green.value(1)
cBool = False

while True:  # wait for THE BUTTON to be pressed
    if (b1.value() == 0):
        if cBool == False:
            init = 2350 #if no calibration, set to preset calibration 2600 with water
            current = 340
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
print("Engaging...")
file = open("data.csv", "w")
embblink = PWM(emb, freq=4)
time.sleep(10)

embblink.deinit()
cycle = 0 #a cycle is ~1 second
file.write("Time,ADC Value,Std Deviation,Calibrated OD\n")
while (b1.value() == 1) and (cycle <= 64800): #continue until the button is pushed or when 18 hours worth of data is reached
    blue.value(1)
    if cycle % 30 == 0:
        data = measure(current, init)
        OD = -1*(math.log10(data[0]/init)) #calculate OD
        ODcali = 5.5099*OD + 0.0471 #change OD to calibrated value
        file.write("{},{},{},{}\n".format(cycle,data[0],data[1],ODcali))
        print("{},{},{},{}\n".format(cycle,data[0],data[1],ODcali))
    elif cycle % 2 == 0: #blink green every other second
        if green.value() == 0:
            pass
            #green.value(1)
        else:
            pass
            #green.value(0)
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
