import pyautogui
import time

# 1 - Tamanho da tela
print(pyautogui.size())

# 2 - Posição atual do mouse
print(pyautogui.position())
time.sleep(1.5)


# 3 - App para ver a posição do mouse em tempo real
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Movendo o mouse
pyautogui.moveTo(1255, 22, 1)
pyautogui.click()

# 5 - Realizando o scroll
time.sleep(1.5)
pyautogui.moveTo(677, 138, 1)
time.sleep(1.5)
pyautogui.scroll(-200)

