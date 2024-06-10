from pywinauto import Application, mouse
import time

#not actual unit tests, this is too simple of a program for that
# just to get used to pywinauto, never used it before

app = Application(backend="uia").connect(title="Roblox")
roblox_window = app.top_window()


roblox_window.set_focus()

rect = roblox_window.rectangle()
center_x = (rect.left + rect.right) // 2
center_y = (rect.top + rect.bottom) // 2

mouse.press(button='left', coords=(center_x, center_y))


time.sleep(1)


mouse.release(button='left', coords=(center_x, center_y))

print("Released 'W' key")



