import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    ['https://teams.microsoft.com/l/meetup-join/19%3a30ae2a34196542428aa960aec7a95680%40thread.tacv2/1727247141559?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22b86d8394-7d7f-455e-b7ea-7416d0412e1f%22%7d','14:00','15:30']
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
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