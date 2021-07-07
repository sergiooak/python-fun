from scipy import spatial
import pyautogui
import keyboard
import random
import time

busy = False


def findDots():
    busy = True
    coords = pyautogui.locateAllOnScreen('imgs/ponto.png', confidence=.8)
    arrayCoords = []
    for coord in coords:
        x, y = (coord[0] + (coord[2] / 2), coord[1] + (coord[3] / 2))
        arrayCoords.append((x, y))

    x, y = pyautogui.position()
    next = (x, y)
    started = False
    while(len(arrayCoords) > 0):
        tree = spatial.KDTree(arrayCoords)
        next = arrayCoords.pop((tree.query([next]))[1][0])
        if(not started):
            first = next
            started = True
            pyautogui.moveTo(next[0], next[1], duration=0,
                             tween=pyautogui.easeInOutQuad)
            pyautogui.mouseDown()
        else:
            pyautogui.moveTo(next[0], next[1], duration=0,
                             tween=pyautogui.easeInOutQuad)

    pyautogui.moveTo(first[0], first[1], duration=0,
                     tween=pyautogui.easeInOutQuad)
    pyautogui.mouseUp()
    busy = False


while True:
    try:
        if keyboard.is_pressed('tab'):
            if(not busy):
                findDots()
            time.sleep(0.25)
        if keyboard.is_pressed('q'):
            print('You Pressed "Q"!')
            break  # finishing the loop
    except:
        break
