import pyautogui, time
f = open("bee movie script.txt", "r")
for word in f:
    pyautogui.typewrite(f"@CoolTomato {word}")
    pyautogui.press("enter")
