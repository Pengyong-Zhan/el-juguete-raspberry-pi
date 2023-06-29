from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

Y = [255, 255, 0]
B = [0, 0, 255]
X = [0, 0, 0]

s = 10

timer = [Y] * s + [X] * (64 - s)
    
sense.set_pixels(timer)

for i in range(s-3):
  sleep(1)
  timer[i] = B
  sense.set_pixels(timer)
  
for i in range(3, -1, -1):
  sleep(1)
  sense.clear()
  sense.show_letter(str(i), B)
  
for i in range(0, 10):
  sense.clear()
  sleep(0.1)
  sense.show_letter(str(1), B)
  sleep(0.1)
