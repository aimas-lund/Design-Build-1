import machine
import numpy as np
def calibrate(adc): #activate when a button is pushed and held for x seconds
    measurements = np.array([])
    for i in range(10):
        reading = adc.read()  # read the value
        np.hstack((measurements, reading))  # stack the readings in an array
    blank = np.mean(measurements)  # take the average value
    return(blank)