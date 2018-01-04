import machine
def LEDactivate():
    pinNr = 9999 #insert pinnumber
    LED = machine.Pin(pinNr,machine.Pin.OUT) #define LED as an output pin
    LED.value(1) #turn on LED

        