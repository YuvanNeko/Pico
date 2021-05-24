import machine
import utime

ledcold = machine.Pin(0, machine.Pin.OUT)
ledwarm = machine.Pin(1, machine.Pin.OUT)

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

def writeFile(a):
    my_file = open("temp.txt", "a")
    my_file = my_file.write(a)
    my_file = my_file.close()
    print("Written sucessfully!")

sensor_temp = machine.ADC(4)

CONVERSION_FACTOR = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * CONVERSION_FACTOR
    temperature = 27 - (reading - 0.706)/0.001721
    #writeFile(temperature)
    my_file = open("temp.txt", "a")
    my_file = my_file.write(temperature)
    my_file = my_file.close()
    print("Written sucessfully!")
    print(temperature)
    if temperature <= 20.0:
        cold()
    if temperature >= 21.0:
        warm()
    utime.sleep(0.5)