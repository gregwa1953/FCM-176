# Pyautogui test #2
import pyautogui
import time

pyautogui.click(982, 480)
pyautogui.write('Greg')
time.sleep(10)
pyautogui.click(1015, 546)
pyautogui.write('password')
time.sleep(10)
pyautogui.click(1042, 621)
pyautogui.alert(text='Finished!', title='PYAUTOGUI TEST', button='OK')