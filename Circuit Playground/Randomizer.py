from adafruit_circuitplayground import cp

import random
import time
while True:
   shake = 15.0
   if abs(cp.acceleration.x) > shake or abs(cp.acceleration.y) > shake or abs(cp.acceleration.z) > shake:
      for i in range(0,10):
         a = random.randint(0,255)
         b = random.randint(0,255)
         c = random.randint(0,255)
         cp.pixels[i] = (a,b,c)