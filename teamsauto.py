import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
     ["Link to Teams meeting", "Start time (24-hour format)", "End time (24-hour format)"],
    # ... add more lectures in the same format ...
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(5)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(8)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                #pyautogui.hotkey('ctrl','shift','m')
                #time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break
