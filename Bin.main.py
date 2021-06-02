import machine
import utime

led1 = machine.Pin(3, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(1, machine.Pin.OUT)
led4 = machine.Pin(0, machine.Pin.OUT)
LEDs = [led1, led2, led3, led4]
delay = 0.75

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
    print("0001")

def stage2():
    led1.low()
    led2.high()
    led3.low()
    led4.low()
    print("0010")

def stage3():
    led1.high()
    led2.high()
    led3.low()
    led4.low()
    print("0011")

def stage4():
    led1.low()
    led2.low()
    led3.high()
    led4.low()
    print("0100")

def stage5():
    led1.high()
    led2.low()
    led3.high()
    led4.low()
    print("0101")

def stage6():
    led1.low()
    led2.high()
    led3.high()
    led4.low()
    print("0110")

def stage7():
    led1.high()
    led2.high()
    led3.high()
    led4.low()
    print("0111")
    
def stage8():
    led1.low()
    led2.low()
    led3.low()
    led4.high()
    print("1000")

def stage9():
    led1.high()
    led2.low()
    led3.low()
    led4.high()
    print("1001")

def stage10():
    led1.low()
    led2.high()
    led3.low()
    led4.high()
    print("1010")

def stage11():
    led1.high()
    led2.high()
    led3.low()
    led4.high()
    print("1011")

def stage12():
    led1.low()
    led2.low()
    led3.high()
    led4.high()
    print("1100")

def stage13():
    led1.high()
    led2.low()
    led3.high()
    led4.high()
    print("1101")

def stage14():
    led1.low()
    led2.high()
    led3.high()
    led4.high()
    print("1110")

def stage15():
    led1.high()
    led2.high()
    led3.high()
    led4.high()
    print("1111")

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