import board
import pulseio
led = pulseio.PWMOut(board.D13)
import time

while True:
    for i in range(100):
        led.duty_cycle = int(i / 100 * 65535) #turns led fully bright
        time.sleep(0.01) #time when led is fully on
    for i in range(100, -1, -1): #turns led fully dark
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01) #time when led is fully off