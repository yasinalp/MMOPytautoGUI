import os
import time
import datetime
import pyautogui
import winsound
from directkeys import *
pyautogui.FAILSAFE = False


server_ismi = 'Aeldra'
deneme = 1
oldurme = 0
envanter = 0
bybsayac = 0
allahallah = 0
olta_barda = None  # Bu sunucuda olta simgesi skill bara konulmuyor
olta_cekilecek = None  # olta çekme tanımlanmamış olabilir uyarısına karşın
svside1 = svside2 = None
time.sleep(2)

screensize_x, screensize_y = pyautogui.size()
rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)


def klik(_x=None, _y=None, _clicks=1, _interval=0.0, _button='left', _duration=0.0):
    oldx, oldy = pyautogui.position()
    time.sleep(0.1)
    pyautogui.click(_x, _y, clicks=_clicks, interval=_interval, button=_button, duration=_duration)
    time.sleep(0.1)
    pyautogui.moveTo(oldx, oldy)


def go_wait_click(_x, _y, _duration=0.5, _button='left'):
    pyautogui.moveTo(_x, _y)
    time.sleep(_duration)
    klik(_button=_button)


def yem_tak():
    # Varsa minik balık, yoksa solucan kullanıyoruz.
    # minikyeni = lokeytCenterOnScreen('img/Baliklar/yeni_minik.png', region=(1130, 385, 236, 360))
    # minikeski = lokeytCenterOnScreen('img/Baliklar/eski_minik.png', region=(1130, 385, 236, 360))
    solucan = lokeytCenterOnScreen('img/balikyemtus.png')
    # if minikyeni:
    #     pyautogui.moveTo(minikyeni)
    #     klik(minikyeni, button='right', duration=1)
    # elif minikeski:
    #     pyautogui.moveTo(minikeski)
    #     klik(minikeski, button='right', duration=1)
    # else:
    if solucan:
        time.sleep(1)
        pyautogui.moveTo(solucan)
        klik(solucan, _button='right', _duration=1)
    time.sleep(0.7)


def olta_at_yada_cek():
    if olta_barda:
        olta = lokeytCenterOnScreen('img/olta.png')
        pyautogui.moveTo(olta[0], olta[1] - 100)
        klik(olta, _button='right', _duration=0.3)
        pyautogui.moveTo(olta[0], olta[1] - 100)
    else:
        BasCek(SPACE)
        # pyautogui.press('space')
    time.sleep(1)


def svside_gecene_kadar_bekle():
    global svside1, svside2
    svside_kontrol()
    if svside1 or svside2:
        svside_vardi = True
        while svside1 or svside2:
            print("Captcha var.1")
            time.sleep(1)
            svside_kontrol()
        return svside_vardi
    else:
        return False


def baliklara_sag_tikla():
    for balik_img_path in os.listdir('img/Baliklar'):
        balik = lokeytCenterOnScreen('img/Baliklar/{}'.format(balik_img_path), region=(1130, 385, 236, 360))
        if balik:
            klik(balik, _button='right')
    pass


def envanter_isleri():
    global envanter, svside1
    envanter += 2  # Hangi çantaya geçileceğini belirler.
    envantergecis = 0  # Kaç çantaya bakılacağını bununla kontrol ediyoruz.
    while (envanter % 5) != 0:  # döngü 2 değeri ile başlayıp 5 değerinde sonlanıyor.3 kez döner.
        baliklara_sag_tikla()
        # Aynı şekilde gereksiz eşyaları da çantadan atıyoruz.
        gereksizleri_at()
        if (deneme % 10) == 0:  # Her 10 döngüde bir ss alıyoruz.
            ss_al()

        ###
        envantergecis += 1  # değerini her döngüde 1 arttırarak diğer çantaya geçiş sağlıyoruz.
        if envantergecis < 4:
            go_wait_click(1210 + 40 * (envanter % 4), 400)
        envanter += 1
        ###


def ss_al(_region=None):
    an = datetime.datetime.now()
    ay = an.month
    gun = an.day
    saat = an.hour
    dakika = an.minute
    saniye = an.second
    # ss'lerin adları çekildikleri zaman oluyor.
    save_path = 'Loglar/{:02d}-{:02d}_{:02d}.{:02d}.{:02d}.png'.format(ay, gun, saat, dakika, saniye)
    pyautogui.screenshot(save_path, region=_region)
    print("SS alındı.")
    time.sleep(0.1)


def gereksizleri_at():
    for gereksiz_img_path in os.listdir('img/Gereksizler'):
        gereksiz = lokeytCenterOnScreen('img/Gereksizler/{}'.format(gereksiz_img_path),
                                        region=(1130, 385, 236, 360))
        if gereksiz:
            pyautogui.moveTo(gereksiz)
            time.sleep(0.2)
            klik(gereksiz)
            time.sleep(0.2)
            pyautogui.moveTo(800, 400)
            klik(_clicks=2, _interval=0.25)


def svside_kontrol():
    global svside1, svside2
    svside1 = lokeytOnScreen('img/svside1.png', region=(1070, 457, 98, 18))
    svside2 = lokeytOnScreen('img/svside2.png', region=(1070, 457, 98, 18))


def olduysek_ch_at():
    global bybsayac
    bybsayac += 1
    pyautogui.moveTo(bybasla)
    time.sleep(0.5)
    klik()
    time.sleep(3)
    pyautogui.moveTo(ayarlar)
    time.sleep(1)
    klik()
    time.sleep(1)
    oyunsecenek = lokeytCenterOnScreen('img/ChAt/OyunSecenekleri.png')
    pyautogui.moveTo(oyunsecenek)
    time.sleep(0.5)
    klik()
    ch = str((bybsayac % 4) + 1)
    ch_at = lokeytCenterOnScreen('img/ChAt/CH{}.png'.format(ch))
    if ch_at:
        go_wait_click(ch_at[0], ch_at[1])
    time.sleep(5)


def kamera_reset():
    # Şimdi kameranın açısını ayarlıyoruz.
    pyautogui.moveTo(300, 300)
    pyautogui.mouseDown(button='right')
    pyautogui.moveRel(0, 200)
    pyautogui.mouseUp(button='right')
    time.sleep(1)
    pyautogui.scroll(1500)
    time.sleep(1)
    pyautogui.scroll(-400)
    pyautogui.mouseDown(button='right')
    pyautogui.moveRel(0, -50)
    pyautogui.mouseUp(button='right')
    time.sleep(1)


def lokeytOnScreen(needle, region=None):
    oldx, oldy = pyautogui.position()
    pyautogui.moveTo(screensize_x, screensize_y)
    coords = pyautogui.locateOnScreen(needle, region=region)
    pyautogui.moveTo(oldx, oldy)
    return coords


def lokeytCenterOnScreen(needle, region=None):
    coords = lokeytOnScreen(needle, region=region)
    if coords:
        return coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2)
    else:
        return None


while rgb:
    # Bu while döngüsünde önce sol başlat çubuğu ön planda mı diye kontrol ediyoruz.
    print("Başlat çubuğu açık")

    m2piks = pyautogui.pixelMatchesColor(30, 90, (122, 12, 9))
    # Ardından  M2'nin soldaki başlat çubuğunda ilk sırada olup olmadığı kontrol ediliyor.
    if m2piks is False:
        # Eğer değilse nerede olduğu algılanıp, ilk sıraya sürükleniyor.
        for baslatsira in range(0, 500):
            print("M2 başlat çubuğunda aranıyor.", baslatsira, "/700")
            ilkpiks = pyautogui.pixelMatchesColor(30, (90 + baslatsira), (122, 12, 9), tolerance=15)
            if ilkpiks is not False:
                print('ilk piksel(30,', (90 + baslatsira), '):', ilkpiks)
                ikincipiks = pyautogui.pixelMatchesColor(32, (84 + baslatsira), (250, 214, 110), tolerance=15)
                print('ikinci piksel:', ikincipiks)
                if ikincipiks is not False:
                    print('Metin2 algılandı.')
                    pyautogui.moveTo(30, (90 + baslatsira))
                    pyautogui.dragTo(x=30, y=90, duration=1)
                    time.sleep(0.25)
                    pyautogui.hotkey('ctrl', 'win', '1')
                    break
            if baslatsira == 499:
                print("M2 bulunamadı, açılıyor.")
                time.sleep(1)
                # Eğer başlat çubuğunda M2 bulunamazsa, oyunun kapandığı tahmin edilip tekrar açılıyor.
                os.startfile('C:/Users/Yasin/Desktop/M2/MilasMt2.lnk')
                time.sleep(2.5)
                klik(1075, 670, 1)
                time.sleep(0.25)
                pyautogui.press('win')
                time.sleep(0.5)
                pyautogui.moveTo(5, 765)
                klik(5, 765)
                break
    else:
        # Daha sonra oyuna geçilip başlat çubuğunun yok olup olmadığı kontrol ediliyor.
        print('M2 zaten ilk sırada.')
        pyautogui.hotkey('ctrl', 'win', '1')
    time.sleep(1)
    rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)

time.sleep(3)
kamera_reset()
balik_bekleme = 300
while oldurme == 0:  # oldurme sayacı program hata verdiğinde 1 değerini alıyor ve program sonlanıyor.
    try:
        print("Deneme:", deneme)  # Programın kaçıncı defa döngüyü sürdürdüğünü okumak için.
        # Şimdi kontrol edeceğimiz görüntüleri tarıyoruz.
        metin2de = lokeytOnScreen('img/metin2de.png', region=(1222, 734, 32, 32))
        svside_kontrol()  # svside1, svside2 <- svside_kontrol()
        time.sleep(0.5)
        if metin2de and not(svside1 or svside2):
            # M2'deysek ve captcha yoksa; yemleri kontrol ediyoruz ve ardından oltayı atıyoruz.
            yem_tak()
            olta_at_yada_cek()
            # oltayı atıp captcha'yı tekrar kontrol ediyoruz.
            olta_atilamadi = svside_gecene_kadar_bekle()  # svside vardı ise True döndürür
            if olta_atilamadi:  # olta_atilamadi'nın True olması demek olta atarken captcha gelmiş demektir.
                # Captcha geldiyse olta atılmamış demektir. Oltayı captcha'dan sonra tekrar atıyoruz.
                olta_at_yada_cek()
            ###
            #envanter_isleri()
            pikselsinir = 0
            # Balık gelip gelmediğini her an kontrol ediyoruz.Uzun süre gelmezse döngü kırılacak.
            while pikselsinir < balik_bekleme:  # pikselsinir sayacı ile kaç sefer balığın kontrol edileceğine bakıyoruz.
                time.sleep(0.01)
                # 8 belirli noktada balık resmine uygun renk tonları olup olmadığını kontrol ediyoruz.
                pik1 = pyautogui.pixelMatchesColor(683, 110, (245, 245, 245), tolerance=10)
                pik2 = pyautogui.pixelMatchesColor(683, 140, (245, 245, 245), tolerance=10)
                pik3 = pyautogui.pixelMatchesColor(683, 170, (245, 245, 245), tolerance=10)
                pik4 = pyautogui.pixelMatchesColor(683, 200, (245, 245, 245), tolerance=10)
                pik5 = pyautogui.pixelMatchesColor(683, 225, (245, 245, 245), tolerance=10)
                pik6 = pyautogui.pixelMatchesColor(683, 240, (245, 245, 245), tolerance=10)
                pik7 = pyautogui.pixelMatchesColor(683, 270, (245, 245, 245), tolerance=10)
                pik8 = pyautogui.pixelMatchesColor(683, 300, (245, 245, 245), tolerance=10)
                if pik1 is not False or pik2 is not False or pik3 is not False or pik4 is not False or \
                        pik5 is not False or pik6 is not False or pik7 is not False or pik8 is not False:
                    # Uygun renk tonu bulduysak döngüyü kırıyor ve çıktılarımızı veriyoruz.
                    pikselsinir = balik_bekleme + 1
                    print("Balık Bulundu!")
                    print(pik1, pik2, pik3, pik4, pik5, pik6, pik7, pik8)
                    olta_cekilecek = True  # Bu değer oltanın çekilip çekilmeyeceğini belirliyor.
                    winsound.Beep(5000, 100)
                else:  # Eğer uygun renk bulunmadıysa kaçıncı kez bakıldığı çıktı veriliyor.
                    pikselsinir += 1
                    print("Balık bekleniyor...", pikselsinir)
                    if pikselsinir == balik_bekleme - 1:
                        # Uzun zaman balık resmi algılanmadığında oltayı çektirmeden döngüyü kırıyoruz.
                        olta_cekilecek = False
                        pikselsinir = balik_bekleme + 1
                    if pikselsinir == balik_bekleme - 5:  # Her denemede bir kez ölüp ölmediğimizi kontrol ediyoruz.
                        bybasla = lokeytCenterOnScreen('img/ChAt/BuradaYeniden.png')
                        ayarlar = lokeytCenterOnScreen('img/ChAt/ayarlar.png', region=(1320, 730, 40, 38))
                        if bybasla:
                            # Eğer öldürülmüşsek 'burada başla' deyip, kanal değiştiriyoruz.
                            olduysek_ch_at()
                            Envanter = lokeytOnScreen('img/ChAt/Envanter.png')
                            if Envanter is None:
                                # Kanal değiştirdikten sonra çantayı tekrar açıyoruz.
                                go_wait_click(1270, 750, _duration=1)
                            kamera_reset()
                            break
            if olta_cekilecek:  # Bu değer 1 olduğunda oltayı belirlediğimiz sürede çekiyoruz.
                time.sleep(2)
                svside_kontrol()
                if not(svside1 or svside2):
                    olta_at_yada_cek()
                    winsound.Beep(5000, 100)
                else:
                    time.sleep(7)
            else:
                allahallah += 1
                if allahallah > 3:
                    ayarlar = lokeytCenterOnScreen('img/ChAt/ayarlar.png', region=(1320, 730, 40, 38))
                    if ayarlar:
                        go_wait_click(ayarlar[0], ayarlar[1])
                        go_wait_click(680, 430)
                else:
                    print("Alla alla...")
                print("Balık 15sn gelmedi,döngü kırıldı.")
        elif metin2de and (svside1 or svside2):
            print("Captcha var...")
        else:
            deneme -= 1
            print("Oyunda değilsiniz.")
            time.sleep(1)

            giriskont1 = lokeytOnScreen('img/giriskont1{}.png'.format(server_ismi))
            if giriskont1:
                pyautogui.press('f1')
                hatakont = lokeytCenterOnScreen('img/hata2.png')
                if hatakont:
                    pyautogui.moveTo(hatakont)
                    klik(hatakont, _duration=0.2)
            giriskont2 = lokeytOnScreen('img/giriskont2{}.png'.format(server_ismi))
            if giriskont2:
                go_wait_click(672, 694)
                time.sleep(4)
                Envanter = lokeytOnScreen('img/ChAt/Envanter.png')
                if Envanter is None:
                    go_wait_click(1270, 750)  # Envantere tıkla
                kamera_reset()
            rgb = pyautogui.pixelMatchesColor(31, 615, (0, 55, 132), tolerance=5)
            print("rgb:", rgb)
            if rgb is not False:
                print("Oyunun açık olup olmadığı kontrol edilecek.")
                #
                m2piks = pyautogui.pixelMatchesColor(30, 90, (122, 12, 9))
                # Ardından  M2'nin soldaki başlat çubuğunda ilk sırada olup olmadığı kontrol ediliyor.
                if m2piks is False:
                    # Eğer değilse nerede olduğu algılanıp, ilk sıraya sürükleniyor.
                    for baslatsira in range(0, 500):
                        ilkpiks = pyautogui.pixelMatchesColor(30, (90 + baslatsira), (122, 12, 9), tolerance=15)
                        if ilkpiks is not False:
                            print('ilk piksel(30,', (90 + baslatsira), '):', ilkpiks)
                            ikincipiks = pyautogui.pixelMatchesColor(32, (84 + baslatsira), (250, 214, 110),
                                                                     tolerance=15)
                            print('ikinci piksel:', ikincipiks)
                            if ikincipiks is not False:
                                print('Metin2 algılandı.')
                                pyautogui.moveTo(30, (90 + baslatsira))
                                pyautogui.dragTo(x=30, y=90, duration=1)
                                time.sleep(0.25)
                                pyautogui.hotkey('ctrl', 'win', '1')
                                break
                        if baslatsira == 499:
                            print("Oyun algılanamadı. Tekrar açılacak.")
                            # Eğer başlat çubuğunda M2 bulunamazsa, oyunun kapandığı tahmin edilip tekrar açılıyor.
                            os.startfile('C:/Users/Yasin/Desktop/M2/MilasMt2.lnk')
                            time.sleep(2.5)
                            klik(1075, 670, 1)
                            time.sleep(0.25)
                            pyautogui.press('win')
                            time.sleep(0.5)
                            pyautogui.moveTo(5, 765)
                            klik(5, 765)
                            break
                else:
                    # Daha sonra oyuna geçilip başlat çubuğunun yok olup olmadığı kontrol ediliyor.
                    print('M2 zaten ilk sırada.')
                    pyautogui.hotkey('ctrl', 'win', '1')
                    time.sleep(1)
            #
            print("Giris1:", giriskont1, "2:", giriskont2)
        print("Deneme:", deneme)
        time.sleep(0.25)
        deneme += 1

    except OSError as e:
        print(e)
        # olta_at_yada_cek()
        # os.startfile('SuMotoru  v9nokta5.py')
        # time.sleep(0.5)
        # pyautogui.moveTo((31, 600))
        # time.sleep(0.1)
        # klik((31, 600))
        # time.sleep(0.2)
        # pyautogui.moveTo((31, 85))
        # time.sleep(0.5)
        # klik((31, 85))
        break
