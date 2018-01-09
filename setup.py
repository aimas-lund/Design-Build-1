from machine import ADC
from machine import Pin
from machine import PWM

def setup():
    #setup light to voltage sensor
    apin = 34  # define analog pin nr (pin A2)
    adc = ADC(Pin(apin))  # define the pin as an analog-to-digital converter
    adc.atten(ADC.ATTN_11DB)  # set the atten..?
    adc.width(ADC.WIDTH_12BIT)  # set the width of the available bits

    #setup measurement LED for PWM
    LEDpin = 12  # define the LED as analog output (pin A1)
    dpin = Pin(LEDpin)
    pwm = PWM(dpin)
    pwm.freq(78000)  # set frequency
    pwm.duty(0)  # set current

    #setup embedded LED
    LEDpin2 = 13 #this pin nr. is fixed (pin 13)
    LED = Pin(LEDpin2, Pin.OUT)

    #setup button 1
    buttomPinNo1 = 33 #insert pin number for button (pin 33)
    button = Pin(buttomPinNo1, Pin.IN, Pin.PULL_UP)

    # setup button 2
    buttomPinNo2 = 27  # insert pin number for button (pin 27)
    button2 = Pin(buttomPinNo2, Pin.IN, Pin.PULL_UP)

    return(adc,pwm,LED,button,button2)