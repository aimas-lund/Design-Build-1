import machine

def measureSensor():
    #measure some samples, remove the biggest deviations, and take the average
'''
measurements = []
for i in range(100):
    reading = adc.read()  # read the value
    measurements.append(reading)
val = sum(measurements)/len(measurements) #take the average value
measurements[:] = [(x - val)**2 for x in measurements]
devi = ((sum(measurements))/(len(measurements)-1))**0.5 #take the standard deviation
print(val)
print(devi)
'''

while True: #true has to be changed
    time =
    measurements = []
    pwm.duty(current)
    for i in range(100):
        reading = adc.read()  # read the value
        measurements.append(reading) #append the reading to a list
    data = sum(measurements) / len(measurements)  # take the average value
    measurements[:] = [(x - data) ** 2 for x in measurements]
    std = ((sum(measurements)) / (len(measurements) - 1)) ** 0.5  # take the standard deviation

    file.write("{},{},{}\n".format(current,data,std)) #write to csv
    current += 1 #increase the current
    return()
