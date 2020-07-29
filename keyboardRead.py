import keyboard
import pyautogui
#import cv2
import numpy as np
import time

size = (0, 28, 800, 628)  # This is where the game is located if I lock it top right
last_time = time.time()

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

    screen = np.array(pyautogui.screenshot(region=size))

    print('Frame took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    #cv2.imshow("screen", screen)
    #if cv2.waitKey(20) & 0xFF == ord('q'):
    #    break
#cv2.destroyAllWindows()
