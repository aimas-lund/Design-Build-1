import machine

def setup():
    #setup light to voltage sensor
    apin = 39  # define analog pin nr.
    sensor = machine.Pin(apin)  # define the pin
    adc = machine.ADC(sensor)  # define the pin as an analog-to-digital converter
    adc.atten(machine.ADC.ATTN_11DB)  # set the atten..?
    adc.width(machine.ADC.WIDTH_12BIT)  # set the width of the available bits

    #setup LED
    ledPinNr = 9999  # insert pin number
    LED = machine.Pin(ledPinNr, machine.Pin.OUT)  # define LED as an output pin

    #setup embedded LED
    ledPinNr2 = 13 #this pin nr. is fixed
    LED2 = machine.Pin(ledPinNr2, machine.Pin.OUT)

    #setup button
    ledPinNr3 = 27 #insert pin number for button
    button = machine.Pin(ledPinNr3, machine.Pin.IN)

    return(adc,LED,LED2,button)