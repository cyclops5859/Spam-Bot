# Created by Cyclops!

import pyautogui
import time
import datetime
  
time.sleep(2)
  
while True:
    print(datetime.datetime.now())
    pyautogui.typewrite("what do you want to spam?(enter here)") 
    pyautogui.press("enter")
    time.sleep(1)
