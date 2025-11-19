from adafruit_circuitplayground import cp

while True:
    for i in range(1, 4):
        if cp.acceleration.x > 0:
            cp.pixels[i] = ((0,1,0))
            cp.pixels[i] = (0,0,0)
    for i in range(6, 9):
        if cp.acceleration.x < 0:
            cp.pixels[i] = ((1,0,0))
            cp.pixels[i] = (0,0,0)