import pyautogui
import time

from PIL import Image

from ctypes import *
time.sleep(2)
adder = CDLL('buttons.dll')
adder.left()
last_key = 'left'
# 60 fps - 0,0166666666666667 sec/frame
pause = 0.1#0.15
sleep = 0.07
i = 0
while True:
    print('Start new loop')
    start = time.time()

    screen = pyautogui.screenshot('frame\screen'+str(i)+'.png',region=(840,360,260,300))
    #print('Screenshot: '+str(time.time()-start))

    #start = time.time()

    img = Image.open('frame\screen'+str(i)+'.png')
    pixels = img.load()

    #print('Convert: ' + str(time.time() - start))
    #start = time.time()

    if pixels[0, 0] == (126, 173, 79):
        adder.right()
        time.sleep(pause)
        last_key = 'right'
    if pixels[259, 0] == (126, 173, 79):
        adder.left()
        time.sleep(pause)
        last_key = 'left'
    if last_key == 'right':
        adder.right()
        time.sleep(pause)
    if last_key == 'left':
        adder.left()
        time.sleep(pause)

    time.sleep(sleep)
    i=1
    print('Processing: ' + str(time.time() - start))
