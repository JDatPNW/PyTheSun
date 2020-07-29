import keyboard
while True:
    keys = [0, 0, 0, 0]
    if(keyboard.is_pressed('w')):
        keys[0] = 1
    if(keyboard.is_pressed('a')):
        keys[1] = 1
    if(keyboard.is_pressed('s')):
        keys[2] = 1
    if(keyboard.is_pressed('d')):
        keys[3] = 1
    print(keys)
