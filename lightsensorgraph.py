import machine
import time

apin = 34  # define analog pin nr (pin A2)
adc = machine.ADC(machine.Pin(apin))  # define the pin as an analog-to-digital converter
adc.atten(machine.ADC.ATTN_11DB)  # set the attenuation
adc.width(machine.ADC.WIDTH_12BIT)  # set the width of the available bits

buttonPinNo = 33 #insert pin number for button (pin 33)
button = machine.Pin(buttonPinNo, machine.Pin.IN, machine.Pin.PULL_UP)

apin2 = 12 #define the LED as analog output (pin A1)
dpin = machine.Pin(apin2)
pwm = machine.PWM(dpin)
pwm.freq(78000) #set frequency
current = 0
pwm.duty(current) #set current

while True: #wait for THE BUTTON to be pressed
    print(button.value())
    if button.value() == 0:
        file = open("data.csv", "w") #open csv data file
        break
    else:
        pass

while current <= 450:
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
    print(int(current/450*100)) #display the percentile completion rate

pwm.duty(0)
print("Done!")
file.close()