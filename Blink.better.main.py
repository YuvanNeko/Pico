#import section
import machine
import utime
#pin declaration section
l1 = machine.Pin(0, machine.Pin.OUT)
l2 = machine.Pin(1, machine.Pin.OUT)
l3 = machine.Pin(2, machine.Pin.OUT)
l4 = machine.Pin(3, machine.Pin.OUT)
switch = machine.Pin(4, machine.Pin.OUT, machine.Pin.PULL_DOWN)
LEDs = [l1,l2,l3,l4]
#variables section
delay = 0.25
#loop section
while True:
    if switch.value() == 1:
        for x in LEDs:
            x.high()
            utime.sleep(delay)
            x.low()
