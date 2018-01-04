import machine
import time
import numpy as np
def measureSensor(devi=None):
    if pinBool == False:
        apin = 39 #define analog pin nr.
        sensor = machine.Pin(apin) #define the pin
        adc = machine.ADC(sensor) #define the pin as an analog-to-digital converter
        adc.atten(machine.ADC.ATTN_11DB)  #set the atten..?
        adc.width(machine.ADC.WIDTH_12BIT)  #set the width of the available bits
    else:
        pass

    #measure some samples, remove the biggest deviations, and take the average
    measurements = np.array([])
    for i in range(10):
        reading = adc.read()  # read the value
        np.hstack((measurements, reading)) #stack the readings in an array
    val = np.mean(measurements) #take the average value
    devi = np.std(measurements) #take the standard deviation

    return(val,devi)
