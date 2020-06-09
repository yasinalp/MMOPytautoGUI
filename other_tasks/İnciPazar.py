import pyautogui
import time

a=1
while a == 1:
    kırmızıfiyat = int(input('Kırmızı incinin satılacağı fiyat (M cinsinden):'))*1000000
    if kırmızıfiyat == 0:
        print('kırmızı:239M, mavi:79M, beyaz:49M')
        kırmızıfiyat = 239000000
        mavifiyat = 79000000
        beyazfiyat = 49000000
    else:
        mavifiyat = int(input('Mavi incinin satılacağı fiyat (M cinsinden):'))*1000000
        beyazfiyat = int(input('Beyaz incinin satılacağı fiyat (M cinsinden):'))*1000000
    kırmızısınır = int(input('Satılacak kırmızı inci sayısı:'))
    mavisınır = int(input('Satılacak mavi inci sayısı:'))
    beyazsınır = int(input('Satılacak beyaz inci sayısı:'))

    if ((kırmızıfiyat*kırmızısınır)+(mavifiyat*mavisınır)+(beyazfiyat*beyazsınır))>1999999999:

        print('En fazla 2Tlik pazar kurabilirsiniz.')

    else:
        a = 0
    pazardeğeri = ((kırmızıfiyat * kırmızısınır) + (mavifiyat * mavisınır) + (beyazfiyat * beyazsınır))
    print('Mevcut pazar değeri:', (int((pazardeğeri)/1000000)),'M')
    time.sleep(1)
rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)
while rgb == True:
    pyautogui.hotkey('ctrl', 'win', '1')
    time.sleep(1)
    rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)
time.sleep(2)
    
x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/pazarkoord.png')
y = (y1+25)
h = (300)
kırmızıdöngü = 0
mavidöngü = 0
beyazdöngü = 0

time.sleep(1)

if x != None:
    kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
    pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
    while kırmızıdöngü < kırmızısınır and kırmızıkoord != None and pazarboşslot != None:

        pyautogui.moveTo(kırmızıkoord)
        time.sleep(0.3)
        pyautogui.click(kırmızıkoord)
        time.sleep(0.3)
        pyautogui.moveTo(pazarboşslot)
        time.sleep(0.3)
        pyautogui.click(pazarboşslot)
        time.sleep(0.5)

        if kırmızıdöngü == 0:
            pyautogui.press('backspace',presses=10, interval=0.1)
            pyautogui.press('delete', presses=5, interval=0.1)
            pyautogui.typewrite(str(kırmızıfiyat))

        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.3)
        kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
        pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        kırmızıdöngü += 1
    mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
    pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
    while mavidöngü < mavisınır and mavikoord != None and pazarboşslot != None:

        pyautogui.moveTo(mavikoord)
        time.sleep(0.3)
        pyautogui.click(mavikoord)
        time.sleep(0.3)
        pyautogui.moveTo(pazarboşslot)
        time.sleep(0.3)
        pyautogui.click(pazarboşslot)
        time.sleep(0.3)

        if mavidöngü == 0:
            pyautogui.press('backspace', presses=10, interval=0.1)
            pyautogui.press('delete', presses=5, interval=0.1)
            pyautogui.typewrite(str(mavifiyat))
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.5)
        mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
        pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        mavidöngü += 1
    beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
    pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
    while beyazdöngü < beyazsınır and beyazkoord != None and pazarboşslot != None:

        pyautogui.moveTo(beyazkoord)
        time.sleep(0.3)
        pyautogui.click(beyazkoord)
        time.sleep(0.3)
        pyautogui.moveTo(pazarboşslot)
        time.sleep(0.3)
        pyautogui.click(pazarboşslot)
        time.sleep(0.3)

        if beyazdöngü == 0:
            pyautogui.press('backspace', presses=10, interval=0.1)
            pyautogui.press('delete', presses=5, interval=0.1)
            pyautogui.typewrite(str(beyazfiyat))
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.5)
        beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
        pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        beyazdöngü += 1
    time.sleep(0.5)
