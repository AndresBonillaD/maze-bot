from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np

# funciones

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# locateOnScreen busca la imagen en la pantalla
def find_entity():
    print('press q to stop.')
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('car0.png', region=(180, 80, 1000, 500), grayscale=True) != None:
            print('I see it!!!')
            time.sleep(1)
        else:
            print('I cant see shit')
            time.sleep(1)

def mouse_pos():
    # muestra ela posicion del mose hasta oprimir q
    while keyboard.is_pressed('q') == False:
        pyautogui.displayMousePosition()

# prinsipal forma depercibir el ambiente
def screenshot_search():
    pic = pyautogui.screenshot(region=(180, 80, 1000, 500))
    width, height = pic.size
    print('w, h:',width, height)
    width = int(width/25)
    height = int(height/50)
    print('w, h:',width, height)
    map_matrix = np.zeros((height, width), np.int8)

    # usar q para detener el loop
    while keyboard.is_pressed('q') == False:
        print('searching ...')
        stop = input('Stop? ...')
        if stop == 'y':
            break

        pic = pyautogui.screenshot(region=(180, 80, 1000, 500))
        width, height = pic.size
        # buscar en la imagenes
        i=0
        for x in range (0, height, 50):
            j=0
            for y in range(0, width, 25):                
                r, g, b = pic.getpixel((y,x))

                # r = 102 color gris camino
                # r = 136 color gris camino

                if r == 102:
                    #print('---- CAMINO ----')
                    
                    map_matrix[i][j] = 1
                if r in range(50, 59) :
                    #print('---- BUHO ----')y
                    map_matrix[i][j] = 3
                    #time.sleep(0.5)
                if r == 136 :
                    #print('---- CARRO ----')
                    map_matrix[i][j] = 7
                    #time.sleep(0.5)

                j+=1

            i+=1

        print(map_matrix)
        file = open('outfile.txt', 'w+')
        content = str(map_matrix)
        file.write(content)
        file.close()
    return map_matrix


# - Main/Driver code -

# pruebas para encontrar en pantalla una imagen completa
#find_entity()
stagemap = screenshot_search()
#print(stagemap)

# toma un screenshot de la pantalla (x, y, width, Higth)
#map = pyautogui.screenshot(region=(180, 80, 1000, 500))
#map.save(r'C:\Users\andre\Documents\maze-bot\mapscreenshot.png')
