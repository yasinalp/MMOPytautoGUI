import pyautogui
import time
açıklama = """
Programa hoşgeldiniz.
Yeniden başlatmak için: 'restart' yazınız.
Pazarda standart fiyatları kullanmak için 
    kırmızı incinin fiyatına '0' yazınız.
    
Pazar kurmak için:         1'e basınız.
Ticarete inci koymak için: 2'e basınız.
Depoya inci koymak için:   3'e basınız.
Depodan inci almak için:   4'e basınız.
Gümüş Bar istiflemek için: 5'e basınız.

"""

a=0
while a==0:
    a=1
    program = input(açıklama)

    if program == '1':
        a = 1
        while a == 1:
            kırmızıfiyat = int(input('Kırmızı incinin satılacağı fiyat (M cinsinden):')) * 1000000
            if kırmızıfiyat == 0:
                print('kırmızı:299M, mavi:79M, beyaz:39M')
                kırmızıfiyat = 299000000
                mavifiyat = 79000000
                beyazfiyat = 39000000
            else:
                mavifiyat = int(input('Mavi incinin satılacağı fiyat (M cinsinden):')) * 1000000
                beyazfiyat = int(input('Beyaz incinin satılacağı fiyat (M cinsinden):')) * 1000000
            kırmızısınır = int(input('Satılacak kırmızı inci sayısı:'))
            mavisınır = int(input('Satılacak mavi inci sayısı:'))
            beyazsınır = int(input('Satılacak beyaz inci sayısı:'))

            if ((kırmızıfiyat * kırmızısınır) + (mavifiyat * mavisınır) + (beyazfiyat * beyazsınır)) > 1999999999:

                print('En fazla 2Tlik pazar kurabilirsiniz.')

            else:
                a = 0
            pazardeğeri = ((kırmızıfiyat * kırmızısınır) + (mavifiyat * mavisınır) + (beyazfiyat * beyazsınır))
            print('Mevcut pazar değeri:', (int((pazardeğeri) / 1000000)), 'M')
            time.sleep(1)
        rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        while rgb == True:
            pyautogui.hotkey('ctrl', 'win', '1')
            time.sleep(1)
            rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        time.sleep(2)

        x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/pazarkoord.png')
        y = (y1 + 25)
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
                time.sleep(0.1)
                pyautogui.click(kırmızıkoord)
                time.sleep(0.2)
                pyautogui.moveTo(pazarboşslot)
                time.sleep(0.1)
                pyautogui.click(pazarboşslot)
                time.sleep(0.5)

                if kırmızıdöngü == 0:
                    pyautogui.press('backspace', presses=10, interval=0.01)
                    pyautogui.press('delete', presses=5, interval=0.01)
                    pyautogui.typewrite(str(kırmızıfiyat))

                time.sleep(0.3)
                pyautogui.press('enter')
                time.sleep(0.15)
                pyautogui.moveTo(1366,768)
                time.sleep(0.15)
                kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
                pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                kırmızıdöngü += 1
            mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
            pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            while mavidöngü < mavisınır and mavikoord != None and pazarboşslot != None:

                pyautogui.moveTo(mavikoord)
                time.sleep(0.1)
                pyautogui.click(mavikoord)
                time.sleep(0.2)
                pyautogui.moveTo(pazarboşslot)
                time.sleep(0.1)
                pyautogui.click(pazarboşslot)
                time.sleep(0.3)

                if mavidöngü == 0:
                    pyautogui.press('backspace', presses=10, interval=0.01)
                    pyautogui.press('delete', presses=5, interval=0.01)
                    pyautogui.typewrite(str(mavifiyat))
                time.sleep(0.3)
                pyautogui.press('enter')
                time.sleep(0.15)
                pyautogui.moveTo(1366, 768)
                time.sleep(0.15)
                mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
                pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                mavidöngü += 1
            beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
            pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            while beyazdöngü < beyazsınır and beyazkoord != None and pazarboşslot != None:

                pyautogui.moveTo(beyazkoord)
                time.sleep(0.1)
                pyautogui.click(beyazkoord)
                time.sleep(0.2)
                pyautogui.moveTo(pazarboşslot)
                time.sleep(0.1)
                pyautogui.click(pazarboşslot)
                time.sleep(0.3)

                if beyazdöngü == 0:
                    pyautogui.press('backspace', presses=10, interval=0.01)
                    pyautogui.press('delete', presses=5, interval=0.01)
                    pyautogui.typewrite(str(beyazfiyat))
                time.sleep(0.3)
                pyautogui.press('enter')
                time.sleep(0.15)
                pyautogui.moveTo(1366, 768)
                time.sleep(0.15)
                beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
                pazarboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                beyazdöngü += 1
            time.sleep(0.5)
    elif program == '2':
        # hangi inciden kaç adet taşımak istediğini input ile yaz.
        a = 1
        while a == 1:
            kırmızısınır = int(input('Taşınacak kırmızı inci sayısı:'))
            mavisınır = int(input('Taşınacak mavi inci sayısı:'))
            beyazsınır = int(input('Taşınacak beyaz inci sayısı:'))
            if kırmızısınır + mavisınır + beyazsınır > 24:
                print('En fazla 24 inci koyabilirsiniz.')
            else:
                a = 0
        rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        while rgb == True:
            pyautogui.hotkey('ctrl', 'win', '1')
            time.sleep(1)
            rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)

        # envanter ve ticaretin koordinatlarını al.
        x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/tickoord.png')
        y = (y1 - 150)
        h = (150)
        Kabul = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/Kabul.png')
        kırmızıdöngü = 0
        mavidöngü = 0
        beyazdöngü = 0

        time.sleep(3)
        # while döngüsü kur ve incileri ticarete taşı, inputla aldığın sınırı döngü şartı yap.
        if Kabul != None:
            kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
            while kırmızıdöngü < kırmızısınır and kırmızıkoord != None:
                ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                pyautogui.moveTo(kırmızıkoord)
                time.sleep(0.1)
                pyautogui.click(kırmızıkoord)
                time.sleep(0.2)
                pyautogui.moveTo(ticboşslot)
                time.sleep(0.1)
                pyautogui.click(ticboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
                kırmızıdöngü += 1
            mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
            while mavidöngü < mavisınır and mavikoord != None:
                ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                pyautogui.moveTo(mavikoord)
                time.sleep(0.1)
                pyautogui.click(mavikoord)
                time.sleep(0.2)
                pyautogui.moveTo(ticboşslot)
                time.sleep(0.1)
                pyautogui.click(ticboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
                mavidöngü += 1
            beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(1130, 385, 236, 360))
            while beyazdöngü < beyazsınır and beyazkoord != None:
                ticboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                pyautogui.moveTo(beyazkoord)
                time.sleep(0.1)
                pyautogui.click(beyazkoord)
                time.sleep(0.2)
                pyautogui.moveTo(ticboşslot)
                time.sleep(0.1)
                pyautogui.click(ticboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
                beyazdöngü += 1
            time.sleep(0.2)
            pyautogui.moveTo(Kabul)
            time.sleep(0.2)
            pyautogui.click(Kabul)
    elif program == '3':
        a = 1
        while a == 1:
            kırmızısınır = int(input('Taşınacak kırmızı inci sayısı:'))
            mavisınır = int(input('Taşınacak mavi inci sayısı:'))
            beyazsınır = int(input('Taşınacak beyaz inci sayısı:'))
            if kırmızısınır + mavisınır + beyazsınır > 45:
                print('En fazla 45 inci koyabilirsiniz.')
            else:
                a = 0
        rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        while rgb == True:
            pyautogui.hotkey('ctrl', 'win', '1')
            time.sleep(1)
            rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)

        x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/depokoord.png')
        y = (y1 + 25)
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
                time.sleep(0.1)
                pyautogui.click(kırmızıkoord)
                time.sleep(0.2)
                pyautogui.moveTo(depoboşslot)
                time.sleep(0.1)
                pyautogui.click(depoboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(1130, 385, 236, 360))
                depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                kırmızıdöngü += 1
            mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(1130, 385, 236, 360))
            depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            while mavidöngü < mavisınır and mavikoord != None and depoboşslot != None:
                pyautogui.moveTo(mavikoord)
                time.sleep(0.1)
                pyautogui.click(mavikoord)
                time.sleep(0.2)
                pyautogui.moveTo(depoboşslot)
                time.sleep(0.1)
                pyautogui.click(depoboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png',region=(1130, 385, 236, 360))
                depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                mavidöngü += 1
            beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
            depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
            while beyazdöngü < beyazsınır and beyazkoord != None and depoboşslot != None:
                pyautogui.moveTo(beyazkoord)
                time.sleep(0.1)
                pyautogui.click(beyazkoord)
                time.sleep(0.2)
                pyautogui.moveTo(depoboşslot)
                time.sleep(0.1)
                pyautogui.click(depoboşslot)
                time.sleep(0.21)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(1130, 385, 236, 360))
                depoboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-tic.png', region=(x, y, w, h))
                beyazdöngü += 1
            time.sleep(0.5)
            print("Program gerçekleştirildi.")
        else:
            print("Depo tanımlanamadı.")
    elif program == '4':

        a = 1
        while a == 1:
            kırmızısınır = int(input('Taşınacak kırmızı inci sayısı:'))
            mavisınır = int(input('Taşınacak mavi inci sayısı:'))
            beyazsınır = int(input('Taşınacak beyaz inci sayısı:'))
            if kırmızısınır + mavisınır + beyazsınır > 45:
                print('En fazla 45 inci alabilirsiniz.')
            else:
                a = 0
        rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        while rgb == True:
            pyautogui.hotkey('ctrl', 'win', '1')
            time.sleep(1)
            rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
        time.sleep(1)
        x, y1, w, h1 = pyautogui.locateOnScreen('C:/Python34/Ticaret/depokoord.png')
        y = (y1 + 25)
        h = (300)
        kırmızıdöngü = 0
        mavidöngü = 0
        beyazdöngü = 0

        time.sleep(1)
        # while döngüsü kur ve incileri ticarete taşı, inputla aldığın sınırı döngü şartı yap.
        if x != None:
            kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png',region=(x, y, w, h))
            envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png', region=(1190, 400, 176, 325))
            while kırmızıdöngü < kırmızısınır and kırmızıkoord != None and envboşslot != None:
                pyautogui.moveTo(kırmızıkoord)
                time.sleep(0.1)
                pyautogui.click(kırmızıkoord)
                time.sleep(0.2)
                pyautogui.moveTo(envboşslot)
                time.sleep(0.1)
                pyautogui.click(envboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                kırmızıkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incikırmızı.png', region=(x, y, w, h))
                envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png',region=(1190, 400, 176, 325))
                kırmızıdöngü += 1
            mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png',region=(x, y, w, h))
            envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png', region=(1190, 400, 176, 325))
            while mavidöngü < mavisınır and mavikoord != None and envboşslot != None:
                pyautogui.moveTo(mavikoord)
                time.sleep(0.1)
                pyautogui.click(mavikoord)
                time.sleep(0.2)
                pyautogui.moveTo(envboşslot)
                time.sleep(0.1)
                pyautogui.click(envboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                mavikoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incimavi.png', region=(x, y, w, h))
                envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png',region=(1190, 400, 176, 325))
                mavidöngü += 1
            beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png',region=(x, y, w, h))
            envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png', region=(1190, 400, 176, 325))
            while beyazdöngü < beyazsınır and beyazkoord != None and envboşslot != None:
                pyautogui.moveTo(beyazkoord)
                time.sleep(0.1)
                pyautogui.click(beyazkoord)
                time.sleep(0.2)
                pyautogui.moveTo(envboşslot)
                time.sleep(0.1)
                pyautogui.click(envboşslot)
                time.sleep(0.2)
                pyautogui.moveRel(1366, 768)
                time.sleep(0.25)
                beyazkoord = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/incibeyaz.png', region=(x, y, w, h))
                envboşslot = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/boşslot-env.png',region=(1190, 400, 176, 325))
                beyazdöngü += 1
            time.sleep(0.5)
            print("Program gerçekleştirildi.")
        else:
            print("Depo tanımlanamadı.")
    elif program == '5':
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
        gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png', region=(1130, 385, 236, 360))
        pyautogui.moveTo(gumusbar)
        time.sleep(0.1)
        pyautogui.click(gumusbar)
        gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png', region=(1130, 385, 236, 360))
        while gumusbar != None:
            gbx, gby = gumusbar
            pyautogui.moveTo(gumusbar)
            time.sleep(0.1)
            pyautogui.click(gbx, gby)
            time.sleep(0.25)
            gumusbar = pyautogui.locateCenterOnScreen('C:/Python34/Ticaret/100Mbar.png', region=(1130, 385, 236, 360))
            time.sleep(0.1)
            pyautogui.click(gbx, gby)
    elif program =='restart':
        a=0
        continue
    else:
        print("Yanlış giriş yaptınız!")
        a=0
