import pyautogui, time
time.sleep(5)
x = 0
while x < 100:
    pyautogui.typewrite("Hi, I am a heckr")
    pyautogui.press("enter")
    x = x + 1  