import keyboard
from mss import mss
import cv2
import time
import numpy as np

bounding_box = {'top': 28, 'left': 0, 'width': 800, 'height': 600}

last_time = time.time()
sct = mss()

for i in range(1000):
    keys = [0, 0, 0, 0]
    if(keyboard.is_pressed('w')):
        keys[0] = 1
    if(keyboard.is_pressed('a')):
        keys[1] = 1
    if(keyboard.is_pressed('s')):
        keys[2] = 1
    if(keyboard.is_pressed('d')):
        keys[3] = 1
    if(keyboard.is_pressed('q')):
        break

    screen = np.array(sct.grab(bounding_box))

    print('Frame took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    cv2.imshow("screen", screen)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
