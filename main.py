import pyautogui
import time
from PIL import Image
from ctypes import *


def search_pixel(pixels, depth, x_vertical):
    for y in range(depth):
        if pixels[x_vertical, y] == (161, 116, 56) or pixels[x_vertical, y] == (136, 99, 50):
            return True
    return False


time.sleep(2)
clicker = CDLL('butFunctions.dll')
clicker.clickLeftBut()
last_key = 'left'
pause = 0.03  # 0.1
sleep = 0.00  # 0.07
i = 0
while True:
    print('Start new loop')
    start = time.time()

    left = pyautogui.screenshot('left_frames\screen' + str(i) + '.png', region=(840, 220, 80, 220))
    right = pyautogui.screenshot('right_frames\screen' + str(i) + '.png', region=(1000, 220, 80, 220))
    # print('Screenshot: '+str(time.time()-start))

    # start = time.time()

    left_pixels = Image.open('left_frames\screen' + str(i) + '.png').load()
    right_pixels = Image.open('right_frames\screen' + str(i) + '.png').load()

    # print('Convert: ' + str(time.time() - start))
    # start = time.time()

    if search_pixel(left_pixels, 200, 40):
        clicker.clickRightBut()
        time.sleep(pause)
        last_key = 'right'
    if search_pixel(right_pixels, 200, 40):
        clicker.clickLeftBut()
        time.sleep(pause)
        last_key = 'left'
    if last_key == 'right':
        clicker.clickRightBut()
        time.sleep(pause)
    if last_key == 'left':
        clicker.clickLeftBut()
        time.sleep(pause)

    time.sleep(sleep)
    i = 1
    print('Processing: ' + str(time.time() - start))
