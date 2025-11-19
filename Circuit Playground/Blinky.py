from adafruit_circuitplayground import cp

import time 
while True:
    cp.pixels.fill((0, 255, 0))
    time.sleep(.367)
    cp.pixels.fill((0, 0, 0))
    time.sleep(.367)
    
'''
- **Red**: `(255, 0, 0)`
- **Green**: `(0, 255, 0)`
- **Blue**: `(0, 0, 255)`
- **Yellow**: `(255, 255, 0)`
- **Purple**: `(128, 0, 128)`
- **White**: `(255, 255, 255)`
'''
