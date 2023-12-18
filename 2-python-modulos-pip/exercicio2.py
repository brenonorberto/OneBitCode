import os

# 1 -Desligar o computador
os.system('shutdown -h now')  # Mac
os.system('shutdown -h /s')  # Windows - desliga o computador em 60 segundos
os.system('shutdown -h /s -t 0')  # Windows - desliga o computador imediamente
os.system('shutdown now')  # Linux

# 2 - Cancelar o desligamento
os.system('shutdown -c')  # Mac
os.system('shutdown /a')  # Windows


def turn_off_one_hour():
    os.system('shutdown -h 1')  # Mac
    os.system('shutdown /s /t 3600')  # Windows


def turn_off_half_an_hour():
    os.system('shutdown -h 30')  # Mac
    os.system('shutdown /s /t 1800')  # Windows


def cancel_shutdown():
    os.system('shutdown -c')  # Mac
    os.system('shutdown /a')  # Windows
