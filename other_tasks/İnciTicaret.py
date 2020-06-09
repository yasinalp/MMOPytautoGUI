import pyautogui
import time

# hangi inciden kaç adet taşımak istediğini input ile yaz.
a=1
while a == 1:
    kırmızısınır = int(input('Taşınacak kırmızı inci sayısı:'))
    mavisınır = int(input('Taşınacak mavi inci sayısı:'))
    beyazsınır = int(input('Taşınacak beyaz inci sayısı:'))
    if kırmızısınır+mavisınır+beyazsınır>24:
        print('En fazla 24 inci koyabilirsiniz.')
    else:
        a = 0
rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)
while rgb == True:
    pyautogui.hotkey('ctrl', 'win', '1')
    time.sleep(1)
    rgb = pyautogui.pixelMatchesColor(31,615,(0, 55, 132), tolerance = 5)

# envanter ve ticaretin koordinatlarını al.
x,y1,w,h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/tickoord.png')
y = (y1-150)
h = (150)
Kabul = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/Kabul.png')
kırmızıdöngü = 0
mavidöngü = 0
beyazdöngü = 0

time.sleep(3)
# while döngüsü kur ve incileri ticarete taşı, inputla aldığın sınırı döngü şartı yap.
if Kabul != None:
    kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png', region=(1130, 385, 236, 360))
    while kırmızıdöngü < kırmızısınır and kırmızıkoord != None:

        ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x,y,w,h))
        pyautogui.moveTo(kırmızıkoord)
        time.sleep(0.25)
        pyautogui.click(kırmızıkoord)
        time.sleep(0.25)
        pyautogui.moveTo(ticboşslot)
        time.sleep(0.25)
        pyautogui.click(ticboşslot)
        time.sleep(0.5)
        kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
        kırmızıdöngü += 1
    mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
    while mavidöngü < mavisınır and mavikoord != None:

        ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x,y,w,h))
        pyautogui.moveTo(mavikoord)
        time.sleep(0.25)
        pyautogui.click(mavikoord)
        time.sleep(0.25)
        pyautogui.moveTo(ticboşslot)
        time.sleep(0.25)
        pyautogui.click(ticboşslot)
        time.sleep(0.5)
        mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
        mavidöngü += 1
    beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
    while beyazdöngü < beyazsınır and beyazkoord != None:

        ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x,y,w,h))
        pyautogui.moveTo(beyazkoord)
        time.sleep(0.25)
        pyautogui.click(beyazkoord)
        time.sleep(0.25)
        pyautogui.moveTo(ticboşslot)
        time.sleep(0.25)
        pyautogui.click(ticboşslot)
        time.sleep(0.5)
        beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
        beyazdöngü += 1
    time.sleep(0.5)
    pyautogui.moveTo(Kabul)
    time.sleep(0.2)
    pyautogui.click(Kabul)

# hepsini yaptıktan sonra kabul tuşunu tıklat.