import machine
import utime

led1 = machine.Pin(3, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(1, machine.Pin.OUT)
led4 = machine.Pin(0, machine.Pin.OUT)
LEDs = [led1, led2, led3, led4]
delay = 0.5

def alloff():
    i = 0
    for x in LEDs:
            x.low()
            utime.sleep(0.2)
def stage1():
    led1.high()
    led2.low()
    led3.low()
    led4.low()

def stage2():
    led1.low()
    led2.high()
    led3.low()
    led4.low()

def stage3():
    led1.high()
    led2.high()
    led3.low()
    led4.low()

def stage4():
    led1.low()
    led2.low()
    led3.high()
    led4.low()

def stage5():
    led1.high()
    led2.low()
    led3.high()
    led4.low()

def stage6():
    led1.low()
    led2.high()
    led3.high()
    led4.low()

def stage7():
    led1.high()
    led2.high()
    led3.high()
    led4.low()
    
def stage8():
    led1.low()
    led2.low()
    led3.low()
    led4.high()

def stage9():
    led1.high()
    led2.low()
    led3.low()
    led4.high()

def stage10():
    led1.low()
    led2.high()
    led3.low()
    led4.high()

def stage11():
    led1.high()
    led2.high()
    led3.low()
    led4.high()

def stage12():
    led1.low()
    led2.low()
    led3.high()
    led4.high()

def stage13():
    led1.high()
    led2.low()
    led3.high()
    led4.high()

def stage14():
    led1.low()
    led2.high()
    led3.high()
    led4.high()

def stage15():
    led1.high()
    led2.high()
    led3.high()
    led4.high()

while True:
    stage1()
    utime.sleep(delay)
    stage2()
    utime.sleep(delay)
    stage3()
    utime.sleep(delay)
    stage4()
    utime.sleep(delay)
    stage5()
    utime.sleep(delay)
    stage6()
    utime.sleep(delay)
    stage7()
    utime.sleep(delay)
    stage8()
    utime.sleep(delay)
    stage9()
    utime.sleep(delay)
    stage10()
    utime.sleep(delay)
    stage11()
    utime.sleep(delay)
    stage12()
    utime.sleep(delay)
    stage13()
    utime.sleep(delay)
    stage14()
    utime.sleep(delay)
    stage15()
    utime.sleep(delay)
    alloff()