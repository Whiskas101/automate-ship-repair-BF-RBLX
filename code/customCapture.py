
import numpy as np
import win32gui, win32ui, win32con

class CustomCapture:
    
    w = 0
    h = 0
    
    
    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        
        if not self.hwnd:
            raise Exception(f"Window not found: {window_name}")
        
        self.w, self.h = 483, 25
        
        
    @staticmethod    
    def listProcesses():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows( winEnumHandler, None )     
        
    def get_screenshot(self):
        
        
        
        #getting window image data (raw)
        
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0), (483, 25), dcObj, (719,835), win32con.SRCCOPY) #width, height = > 483, 125
        
        #savedata
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        
        #freeing allocated resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        img = img[:, :, :3]
        img = np.ascontiguousarray(img)
        return img
    
    
    
                
    
        
      
        
        
        
    


