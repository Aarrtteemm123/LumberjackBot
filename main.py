import pyautogui
import time
from PIL import Image
from ctypes import *


def search_pixel(pixels, depth, x_vertical):
    for y in range(depth):
        if pixels[x_vertical, y] == (161, 116, 56) \
                or pixels[x_vertical, y] == (136, 99, 50):  # color texture wood
            return True
    return False


clicker = CDLL('butFunctions.dll')  # loading c++ function
clicker.clickLeftBut()  # press left button
last_key = 'left'  # last clicked key
pause = 0.03  # pause for loading game animation

while True:
    start = time.time()  # counter

    # screenshot left and right part tree
    pyautogui.screenshot('left_frame.png', region=(840, 220, 80, 220))
    pyautogui.screenshot('right_frame.png', region=(1000, 220, 80, 220))

    # loading pixels from image
    left_pixels = Image.open('left_frame.png').load()
    right_pixels = Image.open('right_frame.png').load()

    if search_pixel(left_pixels, 200, 40):  # search wood color pixel
        clicker.clickRightBut()  # press right button
        time.sleep(pause)
        last_key = 'right'
    if search_pixel(right_pixels, 200, 40):
        clicker.clickLeftBut()  # press left button
        time.sleep(pause)
        last_key = 'left'
    if last_key == 'right':
        clicker.clickRightBut()
        time.sleep(pause)
    if last_key == 'left':
        clicker.clickLeftBut()
        time.sleep(pause)

    print('Processing: ' + str(time.time() - start))  # processing time (sec)
