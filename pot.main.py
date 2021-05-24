from machine import Pin, ADC
import utime

pot = ADC(Pin(28))

while True:
    print(pot.read_u16())
    utime.sleep(0.2)