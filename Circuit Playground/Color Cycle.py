from adafruit_circuitplayground import cp

import time
color = 0
while True:
    if cp.button_a:
        color += 1
        time.sleep(.075)
    if color%7 == 0:
        cp.pixels.fill((255, 0, 0))
        time.sleep(.075)
    if color%7 == 1:
        cp.pixels.fill((255, 50, 0))
        time.sleep(.075)
    if color%7 == 2:
        cp.pixels.fill((200, 100, 0))
        time.sleep(.075)
    if color%7 == 3:
        cp.pixels.fill((0, 255, 0))
        time.sleep(.075)
    if color%7 == 4:
        cp.pixels.fill((0, 0, 255))
        time.sleep(.075)
    if color%7 == 5:
        cp.pixels.fill((100, 0, 100))
        time.sleep(.075)
    if color%7 == 6:
        cp.pixels.fill((250, 10, 123))
        time.sleep(.075)