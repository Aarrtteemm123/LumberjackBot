import pyautogui
import time

from PIL import Image

last_key = 'left'
pyautogui.keyDown('left')
pyautogui.keyUp('left')

while True:
    start = time.time()

    screen = pyautogui.screenshot('screen.png',region=(840,360,260,1))

    print('Screenshot: '+str(time.time()-start))

    start = time.time()
    img = Image.open("screen.png")
    pixels = img.load()

    print('Convert: ' + str(time.time() - start))
    start = time.time()
    
    if pixels[0, 0] == (126, 173, 79):
        start = time.time()
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
        last_key = 'right'
    elif pixels[259, 0] == (126, 173, 79):
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        last_key = 'left'
    if last_key == 'right':
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
    elif last_key == 'left':
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')

    print('Processing: ' + str(time.time() - start))
