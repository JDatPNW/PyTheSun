import keyboard
from mss import mss
import cv2
import time
import numpy as np
import os

bounding_box = {'top': 28, 'left': 0, 'width': 800, 'height': 600}

last_time = time.time()
sct = mss()

frame_skip = 2
frame = 0

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []

while(True):
    frame = frame + 1
    if(frame % frame_skip == 0):
        keys = [0, 0, 0]
        if(keyboard.is_pressed('a')):
            keys[0] = 1
        elif(keyboard.is_pressed('d')):
            keys[1] = 1
        elif(keyboard.is_pressed('q')):
            break
        if(keys[0] == keys[1]):
            keys[2] == 1

        screen = np.array(sct.grab(bounding_box))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        screen = cv2.resize(screen, (200, 150))
        screen = cv2.ellipse(screen, (100, 100), (42, 28),
                             0, 0, 360, (125, 125, 125), -1)

        training_data.append([screen, keys])

        if(keyboard.is_pressed('o') and len(training_data) > 50):
            for i in range(50):
                training_data.pop()
                print("Popped")

        if len(training_data) % 1000 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

    print('Frame took {} seconds'.format(time.time() - last_time))
    last_time = time.time()

'''


        cv2.imshow("screen", screen)
        if cv2.waitKey(16) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
'''
