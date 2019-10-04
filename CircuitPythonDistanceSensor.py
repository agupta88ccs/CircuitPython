import time
import board
import neopixel
import adafruit_hcsr04
import simpleio
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)

r = 0
g = 0
b = 0
sonarValue = 0

while True:
    try:
        sonarValue = sonar.distance
        print(sonarValue)
        if sonarValue < 5:
            r = 255
            b = 0
            g = 0

        if sonarValue > 35:
            dot.fill((0, 255, 0))
        if sonarValue > 5 and sonarValue <= 20:
            r = simpleio.map_range(sonarValue, 6, 20, 255, 0)
            b = simpleio.map_range(sonarValue, 6, 20, 0, 255)
            g = 0
        if sonarValue > 20 and sonarValue <= 35:
            g = simpleio.map_range(sonarValue, 21, 35, 0, 255)
            b = simpleio.map_range(sonarValue, 21, 35, 255, 0)
            r = 0
        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)