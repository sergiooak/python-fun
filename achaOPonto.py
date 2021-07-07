import pyautogui

# Move cursor to paint
pyautogui.moveTo(517, 1178, duration=.5, tween=pyautogui.easeInOutQuad)
# Click to open
pyautogui.click()

coords = pyautogui.locateAllOnScreen('ponto.png', confidence=.95)
for coord in coords:
        x,y = (coord[0] + (coord[2] / 2), coord[1] + (coord[3] / 2))
        print(x,y)
        # pyautogui.moveTo(x, y)
        pyautogui.click(x,y)