import pyautogui
import time


with pyautogui.hold('command'):
    pyautogui.press('space')
    
time.sleep(2)
pyautogui.write('monitor')
pyautogui.press('enter')

time.sleep(3)
with pyautogui.hold('ctrl'):
    pyautogui.press('right')