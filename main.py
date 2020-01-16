import pyautogui
import time
from PIL import Image
from ctypes import *

time.sleep(2)
adder = CDLL('butFunctions.dll')
adder.clickLeftBut()
last_key = 'left'
# wood - 161,116,56
# 60 fps - 0,0166666666666667 sec/frame
pause = 0.1  # 0.1
sleep = 0.04  # 0.07
i = 0
while True:
    print('Start new loop')
    start = time.time()

    screen = pyautogui.screenshot('frame\screen' + str(i) + '.png', region=(840, 360, 260, 100))
    # print('Screenshot: '+str(time.time()-start))

    # start = time.time()

    pixels = Image.open('frame\screen' + str(i) + '.png').load()

    # print('Convert: ' + str(time.time() - start))
    # start = time.time()

    if pixels[0, 0] == (126, 173, 79):
        adder.clickRightBut()
        time.sleep(pause)
        last_key = 'right'
    if pixels[259, 0] == (126, 173, 79):
        adder.clickLeftBut()
        time.sleep(pause)
        last_key = 'left'
    if last_key == 'right':
        adder.clickRightBut()
        time.sleep(pause)
    if last_key == 'left':
        adder.clickLeftBut()
        time.sleep(pause)

    time.sleep(sleep)
    i += 1
    print('Processing: ' + str(time.time() - start))
