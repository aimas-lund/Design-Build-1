from setup import *
def calibrate(): #activate when a button is pushed and held for x seconds
    comp = setup() #get pinvalues
    adc = comp[0]
    LED = comp[1]
    current = 450 #overestimate current

    while True: #repetedly decrease the current and measure, until a value is reached of which we know we can measure
        LED.duty(current)
        measurements = []
        for i in range(100): #take an average of 100 readings
            reading = adc.read()  # read the value
            measurements.append(reading)
        blank = sum(measurements) / len(measurements)  # take the average value

        if blank < 2600: #if the blank value preceeds 2600, stop the loop
            break
        else:
            pass
        current -= 1 #gradually reduce current through LED

    LED.duty(0)
    print("Current: {}\nMeasured Value: {}".format(current,blank))
    return(blank,current)