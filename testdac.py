import machine
import time

apin2 = 12 #define the LED as analog output (pin A1)
pin = machine.Pin(apin2)
pwm = machine.PWM(pin)
pwm.freq(78000)
pwm.duty(0)
current = 0
for i in range(100):
    current = current + 1
    pwm.duty(current)
    time.sleep(0.1)
pwm.duty(0)
current = 0

