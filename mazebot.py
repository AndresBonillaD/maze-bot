from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# toma un screenshot de la pantalla (x, y, width, Higth)
map = pyautogui.screenshot(region=(125, 79, 800, 400))
map.save(r'C:\Users\andre\Documents\maze-bot\mapscreenshot.png')

# locateOnScreen busca la imagen en la pantalla
print('press q to stop.')
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('car.png') != None:
        print('I see it!!!')
        time.sleep(0.5)
    else:
        print('I cant see shit')
        time.sleep(0.5)

#while keyboard.is_pressed('q') == False:
#    map = pyautogui.screenshot(region=(125, 79, 800, 400))
#    map.save(r'C:\Users\andre\Documents\maze-bot\mapscreenshot.png')