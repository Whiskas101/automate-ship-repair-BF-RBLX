import cv2
import numpy as np

import win32gui

from customCapture import CustomCapture

import time
from pywinauto import Application, mouse
import time
import win32api, win32con
import keyboard


#hacky solution but I'm not familiar with lower level windows api so this is it
def wait_for_left_click_hold():
    print("Waiting for left mouse button hold...", flush=True)
    while True:
        # Check if the left mouse button is held down
        if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
            time.sleep(0.2)
            break
        time.sleep(0.05)
        print("Waiting for a left click hold", flush=True)
    print("Left mouse button held.",flush=True)



# CustomCapture.listProcesses()


def app():
    Recorder = CustomCapture(window_name="Roblox")
   

    app = Application(backend="uia").connect(title="Roblox")
    roblox_window = app.top_window()

    # Bring the Roblox window to the foreground
    roblox_window.set_focus()

    rect = roblox_window.rectangle()
    center_x = (rect.left + rect.right) // 2
    center_y = (rect.top + rect.bottom) // 2


    GREEN = np.array([133, 248,  95])
    YELLOW = np.array([84, 207, 255])

    paused = False

    while True:
        time.sleep(0.01) # Checking only 100 times per second, to reduce CPU usage.
        
        if keyboard.is_pressed('='):
            cv2.destroyAllWindows()
            break
            
        if keyboard.is_pressed("-"):
            paused = not paused
            time.sleep(0.3)
            
        if paused:
            print("paused, press  -  again to unpause",flush=True)
            continue
        else:
            print("Running. Press  - to pause.", flush=True)
        
        screenshot = Recorder.get_screenshot()
        

        
        match = np.all(screenshot[:,:,:3] == GREEN,  axis=-1)
        
        y, x = np.where(match)

    
        
        if len(x) == 0:
            continue
        else:    
            
            # print(f"Pixel at ({x[0]}, {y[0]}) has value {screenshot[y[0], x[0]]}")
            # print(f"Pixel next is ({x[0]-3}, {y[0]}) has value {screenshot[y[0], x[0]-3]}")
            
            if all(screenshot[y[0], x[0]-3] == YELLOW):
                print("In Green Zone", flush=True)
                mouse.release(button='left', coords=(center_x, center_y))
                time.sleep(0.2)
                
                wait_for_left_click_hold()
                
            
            
        
        #Uncomment this to see the screen section
        # cv2.imshow('Test', screenshot)

app()
    
if __name__ == "__main__":
    app()

