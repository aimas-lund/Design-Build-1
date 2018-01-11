from setup import *
import math
#def calibrate(): #activate when a button is pushed and held for x seconds
comp = setup() #get pinvalues
adc = comp[0]
LED = comp[1]
current = 1 #overestimate current
init = 2660

while True: #repetedly decrease the current and measure, until a value is reached of which we know we can measure
    LED.duty(current)
    measurements = []
    for i in range(100): #take an average of 100 readings
        reading = adc.read()  # read the value
        measurements.append(reading)
    blank = sum(measurements) / len(measurements)  # take the average value
    #blankOD = -1*(math.log10(blank/init))

    if blank >= 2600: #if the blank value preceeds 2600, stop the loop
        break
    elif current == 0:
        print("fail")
        break
    else:
        pass
    current += 1 #gradually reduce current through LED

LED.duty(0)
print("Current: {}\nMeasured Value: {}".format(current,blank))
#return(blank,current) 0.56