from machine import ADC
from machine import Pin
from machine import PWM

def setup():
    #setup light to voltage sensor
    adc = ADC(Pin(34))  # define the pin as an analog-to-digital converter
    adc.atten(ADC.ATTN_11DB)  # set the atten..?
    adc.width(ADC.WIDTH_12BIT)  # set the width of the available bits

    #setup measurement LED for PWM
    dpin = Pin(12)
    pwm = PWM(dpin)
    pwm.freq(78000)  # set frequency
    pwm.duty(0)  # set current

    #setup RGB LED
    red = Pin(15, Pin.OUT)
    green = Pin(32, Pin.OUT)
    blue = Pin(14, Pin.OUT)

    #setup embedded LED
    emb = Pin(13, Pin.OUT)

    #setup button 1
    button = Pin(33, Pin.IN, Pin.PULL_UP)

    # setup button 2
    button2 = Pin(27, Pin.IN, Pin.PULL_UP)

    return(adc,pwm,button,button2,red,green,blue,emb)