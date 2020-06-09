import pyautogui
import time
rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
while rgb == True:
    pyautogui.hotkey('ctrl', 'win', '1')
    time.sleep(1)
    rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
time.sleep(1)
pyautogui.moveTo(1250, 400)  # Çanta2
time.sleep(0.1)
pyautogui.click(1250, 400)
time.sleep(0.1)
pyautogui.moveTo(1210, 400)  # Çanta1
time.sleep(0.1)
pyautogui.click(1210, 400)
gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png',region=(1130, 385, 236, 360))
pyautogui.moveTo(gumusbar)
time.sleep(0.1)
pyautogui.click(gumusbar)
gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png',region=(1130, 385, 236, 360))
while gumusbar != None:
    gbx, gby = gumusbar
    pyautogui.moveTo(gumusbar)
    time.sleep(0.1)
    pyautogui.click(gbx, gby)
    time.sleep(0.2)
    gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png',region=(1130, 385, 236, 360))
    pyautogui.click(gbx, gby)