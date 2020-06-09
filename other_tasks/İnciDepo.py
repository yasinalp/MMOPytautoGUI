import pyautogui
import time

a=1
while a == 1:
    amaç = input("Depodan alacaksanız 'al', depoya koyacaksanız 'koy' yazın.\n")
    kırmızısınır = int(input('Taşınacak kırmızı inci sayısı:'))
    mavisınır = int(input('Taşınacak mavi inci sayısı:'))
    beyazsınır = int(input('Taşınacak beyaz inci sayısı:'))
    if kırmızısınır+mavisınır+beyazsınır>45:
        print('En fazla 45 inci koyabilirsiniz.')
    else:
        a = 0
rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)
while rgb == True:
    pyautogui.hotkey('ctrl', 'win', '1')
    time.sleep(1)
    rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)

if amaç == 'koy':
    x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/depokoord.png')
    y = (y1+25)
    h = (300)
    kırmızıdöngü = 0
    mavidöngü = 0
    beyazdöngü = 0

    time.sleep(3)
    # while döngüsü kur ve incileri ticarete taşı, inputla aldığın sınırı döngü şartı yap.
    if x != None:
        kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
        depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        while kırmızıdöngü < kırmızısınır and kırmızıkoord != None and depoboşslot != None:

            pyautogui.moveTo(kırmızıkoord)
            time.sleep(0.25)
            pyautogui.click(kırmızıkoord)
            time.sleep(0.25)
            pyautogui.moveTo(depoboşslot)
            time.sleep(0.25)
            pyautogui.click(depoboşslot)
            time.sleep(0.5)
            kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
            depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            kırmızıdöngü += 1
        mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
        depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        while mavidöngü < mavisınır and mavikoord != None and depoboşslot != None:

            pyautogui.moveTo(mavikoord)
            time.sleep(0.25)
            pyautogui.click(mavikoord)
            time.sleep(0.25)
            pyautogui.moveTo(depoboşslot)
            time.sleep(0.25)
            pyautogui.click(depoboşslot)
            time.sleep(0.5)
            mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
            depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            mavidöngü += 1
        beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
        depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
        while beyazdöngü < beyazsınır and beyazkoord != None and depoboşslot != None:

            pyautogui.moveTo(beyazkoord)
            time.sleep(0.25)
            pyautogui.click(beyazkoord)
            time.sleep(0.25)
            pyautogui.moveTo(depoboşslot)
            time.sleep(0.25)
            pyautogui.click(depoboşslot)
            time.sleep(0.5)
            beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
            depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            beyazdöngü += 1
        time.sleep(0.5)
elif amaç == 'al':
    pass
else:
    print('Hatalı giriş yaptınız!')