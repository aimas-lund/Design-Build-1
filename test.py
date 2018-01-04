import machine
import time
while True:
    pin = machine.Pin(39) #define the pin
    adc = machine.ADC(pin) #define the pin as an ADC pin
    adc.atten(machine.ADC.ATTN_11DB) #gibberish
    adc.width(machine.ADC.WIDTH_12BIT) #more gibberish
    val = adc.read() #read the value
    print(val) #print the value
    time.sleep(1) #wait one second
