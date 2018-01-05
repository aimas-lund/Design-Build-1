import machine
import time

adc = machine.ADC(Pin(34))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_12BIT)

while True:
    val = adc.read()
    print(val)
    time.sleep(0.5)