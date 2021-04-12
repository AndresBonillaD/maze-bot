from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# funciones

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# locateOnScreen busca la imagen en la pantalla
def find_entity():
    print('press q to stop.')
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('meta.png', region=(180, 80, 1000, 500), grayscale=True) != None:
            print('I see it!!!')
            time.sleep(1)
        else:
            print('I cant see shit')
            time.sleep(1)

def mouse_pos():
    # muestra ela posicion del mose hasta oprimir q
    while keyboard.is_pressed('q') == False:
        pyautogui.displayMousePosition()







# - Main/Driver code -

# pruebas para encontrar en pantalla una imagen completa
# find_entity()

# toma un screenshot de la pantalla (x, y, width, Higth)
map = pyautogui.screenshot(region=(53, 111, 893, 398))
map.save(r'E:\Unal\16 Semestre\Sistemas Inteligentes\maze-bot\mapscreenshot.png')
