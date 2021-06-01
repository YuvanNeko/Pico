import machine
import utime
import _thread

led1 = machine.PWM(machine.Pin(0))
led2 = machine.PWM(machine.Pin(1))

led1.freq(1000)
led2.freq(1000)

def ledrev():
    led3 = machine.PWM(machine.Pin(2))
    led3.freq(1000)
    while True:
        pwmval1 = 65535
        for i in range(65535):
            pwmval1 = pwmval1 - 1000
            print(pwmval)
            led2.duty_u16(pwmval)
            utime.sleep(0.5)
            print("\n led rev")
            print(pwmval1)
            if pwmval1 > 65535:
                pwmval1 = 0
            
_thread.start_new_thread(ledrev, ())

i = 0
pwmval = 0

while True:
    for i in range(65535):
        pwmval = pwmval + 1000
        print(pwmval)
        led1.duty_u16(pwmval)
        led2.duty_u16(pwmval)
        utime.sleep(0.5)
        print("\n led")
        print(pwmval)
        if pwmval > 65535:
            pwmval = 0