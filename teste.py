import time
import pyautogui


# Move cursor to paint
pyautogui.moveTo(517, 1178, duration=.5, tween=pyautogui.easeInOutQuad)
# Click to open
pyautogui.click()

pyautogui.moveTo(100, 200, duration=.5, tween=pyautogui.easeInOutQuad)

distance = 600
while distance > 0:
    pyautogui.drag(distance, 0)   # move right
    distance -= 10
    pyautogui.drag(0, distance)   # move down
    pyautogui.drag(-distance, 0)  # move left
    distance -= 10
    pyautogui.drag(0, -distance)  # move up
