import machine
import utime
import _thread

ledcold = machine.Pin(0, machine.Pin.OUT)
ledwarm = machine.Pin(1, machine.Pin.OUT)
powerled = machine.Pin(25, machine.Pin.OUT)

sensor_temp = machine.ADC(4)

CONVERSION_FACTOR = 3.3 / (65535)

def cold():
    ledcold.high()
    utime.sleep(0.5)
    ledcold.low()
    utime.sleep(0.5)

def warm():
    ledwarm.high()
    utime.sleep(0.5)
    ledwarm.low()
    utime.sleep(0.5)

def second_thread():
    while True:
        powerled.high()
        utime.sleep(0.5)
        powerled.low()
        utime.sleep(0.5)

_thread.start_new_thread(second_thread, ())
        
while True:
    reading = sensor_temp.read_u16() * CONVERSION_FACTOR
    temperature = 27 - (reading - 0.706)/0.001721
    print(round(temperature,2))
    if temperature <= 28.0:
        cold()
    if temperature >= 35.0:
        warm()
    utime.sleep(60)