import machine
def calibrate(adc): #activate when a button is pushed and held for x seconds
    measurements = []
    for i in range(10):
        reading = adc.read()  # read the value
        measurements.append(reading)
    blank = sum(measurements)/len(measurements) # take the average value
    return(blank)