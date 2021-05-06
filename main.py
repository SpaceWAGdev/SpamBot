import time
import keyboard
from playsound import playsound
import pyautogui

time.sleep(3)
pyautogui.typewrite('--Spam messages will apear here--')
time.sleep(1)
pyautogui.press('backspace', presses =33)
time.sleep(5)
f= open("beemovie.txt", 'r')
errorsound = "beep2.wav"

for word in f:
    if keyboard.is_pressed('esc'):
        playsound(errorsound)
        raise KeyboardInterrupt
    pyautogui.typewrite(word)
    pyautogui.press("enter")