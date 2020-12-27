import pyautogui, time
f = open("bee movie script.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
