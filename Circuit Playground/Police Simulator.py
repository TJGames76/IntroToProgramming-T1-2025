from adafruit_circuitplayground import cp

import time 
while True:
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.play_tone(500, 1.0)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)
    cp.play_tone(900, 1.0)