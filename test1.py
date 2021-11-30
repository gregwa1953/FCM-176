# Pyautogui test #1
import pyautogui
import time

sw, sh = pyautogui.size()
print(f'SW: {sw} - SH: {sh}')
pyautogui.moveTo(10, 10, duration=0.50)
time.sleep(2)
pyautogui.moveTo(2550, 10, duration=0.50)
time.sleep(2)
pyautogui.moveTo(2550, 1430, duration=0.50)
time.sleep(2)
pyautogui.moveTo(1024, 768, duration=0.25)
time.sleep(3)
pyautogui.moveTo(127, 159)
pyautogui.click(139, 250)
pyautogui.write('Hello from Python!!!')
pyautogui.alert(text='Finished!', title='PYAUTOGUI TEST', button='OK')
