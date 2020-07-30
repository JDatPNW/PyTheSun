import numpy as np
from mss import mss
import cv2
import time
from pykeyboard import PyKeyboard
from dmnet import dmnet

WIDTH = 200
HEIGHT = 150
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'PyTheSun-{}-{}-{}-epochs-data.model'.format(
    LR, 'dmnet', EPOCHS)

bounding_box = {'top': 28, 'left': 0, 'width': 800, 'height': 600}
sct = mss()

t_time = 0.09

k = PyKeyboard()


model = dmnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while(True):

        if not paused:
            screen = np.array(sct.grab(bounding_box))
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            screen = cv2.resize(screen, (200, 150))
            screen = cv2.ellipse(screen, (100, 100), (42, 28),
                                 0, 0, 360, (125, 125, 125), -1)
            # print('loop took {} seconds'.format(time.time() - last_time))
            # last_time = time.time()

            prediction = model.predict([screen.reshape(200, 150, 1)])[0]
            # print(prediction)

            turn_thresh = .55

            if(prediction[0] > turn_thresh and prediction[0] > prediction[1] and prediction[0] > prediction[2]):
                k.tap_key("a")
                k.tap_key("a")
                k.tap_key("a")
                print("Left!\t\t" + str(prediction[0]))
            elif(prediction[1] > turn_thresh and prediction[1] > prediction[0] and prediction[1] > prediction[2]):
                k.tap_key("d")
                k.tap_key("d")
                k.tap_key("d")
                print("Right!\t\t" + str(prediction[1]))
            else:
                print("Straight!\t" + str(prediction[2]))
                pass


main()
