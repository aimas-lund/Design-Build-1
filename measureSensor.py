import machine
import numpy as np
def measureSensor():
    #measure some samples, remove the biggest deviations, and take the average
    measurements = np.array([])
    for i in range(10):
        reading = adc.read()  # read the value
        np.hstack((measurements, reading)) #stack the readings in an array
    val = np.mean(measurements) #take the average value
    devi = np.std(measurements) #take the standard deviation

    return(val,devi)
