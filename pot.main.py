from machine import Pin, ADC
import utime

pot = ADC(Pin(26))

while True:
    print(pot.read_u16())
    utime.sleep(0.2)