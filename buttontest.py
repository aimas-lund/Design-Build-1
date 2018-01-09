import machine
import time

buttonPinNo = 33 #insert pin number for button (pin 33)
button = machine.Pin(buttonPinNo, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print(button.value())

    time.sleep(0.5)