import pyautogui
import keyboard
import time
import pyperclip

#tempo para comecar o script
time.sleep(2)

while keyboard.is_pressed('`') == False:
    
    if keyboard.is_pressed('z') == True:
        time.sleep(0.8)
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("j")
        time.sleep(0.1)
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        pyautogui.keyDown("j")
        
        time.sleep(0.8)
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("p")
        time.sleep(0.1)
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("p")
        pyperclip.copy('>screenshot')
        
        
    else:
        continue
        

        



