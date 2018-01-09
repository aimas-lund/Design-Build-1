from setup import *
#from calibrate import *
import math
import time

b = setup()[3]
b2 = setup()[4]
LED = setup()[1]
adc = setup()[0]

print("Press the button")
while True:  # wait for THE BUTTON to be pressed
    if b.value() == 0:
        print("Let's get ready to rumble!\n")
        break
    else:
        pass

#c = calibrate()
#LED.duty(c[1]) #set current to calibrated value
#initVal = c[0]
initVal = 2662.72
LED.duty(421)
file = open("OD.csv","w")
abort = False

while abort == False:
    time.sleep(3)
    print("Press button 2 to measure. Press button 1 to finish!")
    while True:
        if b2.value() == 0: #if button 2 is pressed, do a measurement
            print("Thanks")
            measurements = []
            for i in range(100):  # take an average of 100 readings
                reading = adc.read()  # read the value
                measurements.append(reading)
            val = sum(measurements) / len(measurements)  # take the average value
            OD = -1*(math.log10(val/initVal)) #calculate OD
            print("OD: {}".format(OD))
            file.write("{}\n".format(OD))
            break

        elif b.value() == 0: #if button 1 is pressed, finish the session
            abort = True
            file.close()
            print("\nBye")
            break
        else:
            pass


