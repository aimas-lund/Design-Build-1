import time
import machine
pin = machine.Pin(13,machine.Pin.OUT)
while True:
    pin.value(1)
    time.sleep(5)
    pin.value(0)
    time.sleep(5)