from setup import *

def measure(current):
    adc = setup()[0]
    pwm = setup()[1]
    measurements = []
    pwm.duty(current)
    for i in range(100):
        reading = adc.read()  # read the value
        measurements.append(reading) #append the reading to a list
    data = sum(measurements) / len(measurements)  # take the average value
    measurements[:] = [(x - data) ** 2 for x in measurements] #calculate standard deviation from a list comprehention
    std = ((sum(measurements)) / (len(measurements) - 1)) ** 0.5

    pwm.deinit()
    return(data,std)
