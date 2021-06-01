import machine
import utime

led = machine.PWM(machine.Pin(0))

led.freq(1000)

i = 0
pwmval = 0

while True:
    for i in range(65535):
        pwmval = pwmval + 250
        print(pwmval)
        led.duty_u16(pwmval)
        utime.sleep(0.5)
        if pwmval > 65535:
            pwmval = 0