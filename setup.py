import machine

def setup():
    #setup light to voltage sensor
    apin = 34  # define analog pin nr (pin A2)
    adc = machine.ADC(machine.Pin(apin))  # define the pin as an analog-to-digital converter
    adc.atten(machine.ADC.ATTN_11DB)  # set the atten..?
    adc.width(machine.ADC.WIDTH_12BIT)  # set the width of the available bits

    #setup LED
    apin2 = 25 #define the LED as analog output (pin A1)
    dac = machine.DAC(machine.Pin(apin2)) #define as
    adc.atten(machine.ADC.ATTN_11DB)  # set the atten..?
    adc.width(machine.ADC.WIDTH_12BIT) # set the width of the available bits

    #setup embedded LED
    ledPinNo = 13 #this pin nr. is fixed (pin 13)
    LED = machine.Pin(ledPinNo2, machine.Pin.OUT)

    #setup button 1
    buttomPinNo = 27 #insert pin number for button (pin 27)
    button = machine.Pin(buttomPinNo, machine.Pin.IN)

    # setup button 2
    buttomPinNo2 = 12  # insert pin number for button (pin 12)
    button2 = machine.Pin(buttomPinNo2, machine.Pin.IN)

    return(adc,dac,LED,button,button2)