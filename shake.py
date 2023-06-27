from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

while True:
    color = (255, randint(100, 255), randint(0, 255))
    
    acceleration = sense.get_accelerometer_raw()
    x, y, z = map(abs, [acceleration['x'], acceleration['y'], acceleration['z']])

    if x > 1 or y > 1 or z > 1:
        sense.show_message(str(randint(0,99)), text_colour=(color))
        time.sleep(1)
    else:
        sense.clear()
