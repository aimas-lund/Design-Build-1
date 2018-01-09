import machine

def setup():
    #setup light to voltage sensor
    apin = 34  # define analog pin nr (pin A2)
    adc = machine.ADC(machine.Pin(apin))  # define the pin as an analog-to-digital converter
    adc.atten(machine.ADC.ATTN_11DB)  # set the atten..?
    adc.width(machine.ADC.WIDTH_12BIT)  # set the width of the available bits

    #setup LED
    LEDpin2 = 12  # define the LED as analog output (pin A1)
    dpin = machine.Pin(LEDpin2)
    pwm = machine.PWM(dpin)
    pwm.freq(78000)  # set frequency
    current = 0
    pwm.duty(current)  # set current

    #setup embedded LED
    ledPinNo = 13 #this pin nr. is fixed (pin 13)
    LED = machine.Pin(ledPinNo, machine.Pin.OUT)

    #setup button 1
    buttomPinNo = 33 #insert pin number for button (pin 33)
    button = machine.Pin(buttomPinNo, machine.Pin.IN)

    # setup button 2
    buttomPinNo2 = 27  # insert pin number for button (pin 27)
    button2 = machine.Pin(buttomPinNo2, machine.Pin.IN)

    return(adc,dac,LED,button,button2)