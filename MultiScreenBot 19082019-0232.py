import win32gui, win32con, psutil
import os
import logging
import time
import numpy as np
import datetime
import pyautogui
import winsound
from PIL import ImageGrab
from directkeys import *

"""
*NELER YENİ: Öldüğünde başka bir çara geçip o çardan balık tutmaya devam ediyor. 
O çar da ölürse bir önceki çara geçip tutuyor.
*Oyuna girme çıkma işlemleri fonksiyon haline getirildi.
*Oyun ilk başlatıldığında 'game_window_login_timer' değişkeni artık 0 değil time.time() 
"""

"""Traceback (most recent call last):
  File "C:/Users/Yasin/PycharmProjects/Metin2BalıkBotu/MultiScreenBot.py", line 475, in <module>
    bringGameWindow(window)
  File "C:/Users/Yasin/PycharmProjects/Metin2BalıkBotu/MultiScreenBot.py", line 292, in bringGameWindow
    win32gui.SetForegroundWindow(game_window)
pywintypes.error: (1400, 'SetForegroundWindow', 'Geçersiz pencere işleci.')"""

"""
Yapılacaklar:
    Çarlar öldüğünde mal gibi kalıyor: Burada yeniden başla aranması ve ölünmüşse Onedrive'a ss göndermes.
"""



pyautogui.FAILSAFE = False
win32gui.SystemParametersInfo(win32con.SPI_SETFOREGROUNDLOCKTIMEOUT, 0,
                              win32con.SPIF_SENDWININICHANGE | win32con.SPIF_UPDATEINIFILE)
server_ismi = 'Aeldra'
screensize_x, screensize_y = pyautogui.size()
game_number = 3
fish_wait_timers = [2.5, 2.6, 2.7, 3]  # Şuan gayet iyi özellikle 2.6da
state_names = ['initial', 'mainmenu', 'char_select', 'ingame', 'fishing', 'ingame_exiting']
game_window_login_buttons = [F1, F2, F3, F7]
game_window_backup_buttons = [F4, F5, F6, F8]
max_fishing_wait = 100  # 60  # saniye
solucan_skill_barda = True

pencere_baslangici = (562, 104, 804, 636)  # benim pencere offsetim.
win32gui_offset = (4, 4)  # win32 ile benim offsetim.
giris_yap_region = (315, 430, 48, 20)  # giriş yap butonu değişiyor o yüzden giris_F1'i kullanacağız artık.
giris_F1_region = (160, 500, 20, 10)
dc1_region = (340, 310, 85, 5)
dc2_region = (344, 310, 123, 8)
dc3_region = (362, 307, 87, 13)
s_b_region = (341, 306, 118, 15)  # sunucuya_baglaniyorsun_region
c_s_o_g_region = (320, 565, 90, 25)  # char_sec_oyuna_gir_region
b_y_basla_region = (108, 105, 97, 10)
metin2de_region = (663, 595, 32, 32)
envanter_region = (617, 265, 160, 290)
settings_region = (765, 595, 32, 32)
cikis_ingame_region = (395, 425, 25, 15)
balik_ara_region = (408, 250, 1, 20)  # (408, 250, 1, 50) balık görmezse değiştir
skill_bar_region = (320, 595, 272, 33)

deneme = 1
byb_counters = [0] * game_number
balik_gelmedi_counters = [0] * game_number

top_windows = []  # açık olan pencereler.
game_windows = []  # bazı fonksiyonlar hWnd denilen windowHandler numaralarıyla kullanılıyor.
game_window_dcs = []  # bazı fonksiyonlar hdc denilen parametre ile kullanılıyor.
game_window_rects = []  # oyun pencereleri farklı koordinatlarda açılırsa diye offset vermek için
game_window_login_timer = time.time()  # 0.00  # 1 saatte bir fps sorunu için toplu çık-gir yapılacak.
game_states = ['initial'] * game_number  # ileride state kullanarak yapılacak.
current_window = 0  # o anda hangi oyun penceresinde olduğumuz.
fish_control_window = 0  # arkaplandaki hangi pencerede balık aradığımız.
fishing_actives = [False, False, False, False]  # Olta mı atılacak balık mı aranacak.
fish_caughts = [False, False, False, False]  # balık resmi görüldükten sonra zaman karşılaştırmalarında.
game_window_fishing_timers = [0.0] * game_number  # ne kadardır balık beklendiğini tutuyoruz.
fish_catch_time_stamps = [0.00] * game_number  # balık görüldüğü anda değil süre dolunca o pencereye geçilecek.
rod_taken_time_stamps = [0.00] * game_number  # olta çekildikten sonra tekrar atmak için arada beklemek gerekiyor.
rod_takens = [True, True, True, True]  # olta çekildikten sonra zaman damgasını sabit tutabilmek için

logging.basicConfig(level=logging.DEBUG, filename=f"log-{datetime.date.today()}.txt",
                    format='*'*30+'\n%(asctime)s\tLine:%(lineno)d\tCreated:%(created)f\t%(levelname)s\n%(message)s\n'+'*'*30)


def resetWindowVariables():
    logging.debug("resetWindowVariables()")
    global top_windows, game_windows, game_window_dcs, game_window_rects, game_window_login_timer, game_states
    top_windows = []  # açık olan pencereler.
    game_windows = []  # bazı fonksiyonlar hWnd denilen windowHandler numaralarıyla kullanılıyor.
    game_window_dcs = []  # bazı fonksiyonlar hdc denilen parametre ile kullanılıyor.
    game_window_rects = []  # oyun pencereleri farklı koordinatlarda açılırsa diye offset vermek için
    game_window_login_timer = 0.00  # 1 saatte bir fps sorunu için toplu çık-gir yapılacak.
    game_states = ['initial'] * game_number  # ileride state kullanarak yapılacak.


def resetFishingVariables():
    logging.debug("resetFishingVariables()")
    global current_window, fish_control_window, fishing_actives, fish_caughts, game_window_fishing_timers
    global fish_catch_time_stamps, rod_taken_time_stamps, rod_takens
    current_window = 0  # o anda hangi oyun penceresinde olduğumuz.
    fish_control_window = 0  # arkaplandaki hangi pencerede balık aradığımız.
    fishing_actives = [False, False, False, False]  # Olta mı atılacak balık mı aranacak.
    fish_caughts = [False, False, False, False]  # balık resmi görüldükten sonra zaman karşılaştırmalarında.
    game_window_fishing_timers = [0.0] * game_number  # ne kadardır balık beklendiğini tutuyoruz.
    fish_catch_time_stamps = [0.00] * game_number  # balık görüldüğü anda değil süre dolunca o pencereye geçilecek.
    rod_taken_time_stamps = [0.00] * game_number  # olta çekildikten sonra tekrar atmak için arada beklemek gerekiyor.
    rod_takens = [True, True, True, True]  # olta çekildikten sonra zaman damgasını sabit tutabilmek için


def klik(_x=None, _y=None, _clicks=1, _interval=0.05, _button='left', _duration=0.0):
    oldx, oldy = pyautogui.position()
    time.sleep(0.05)
    pyautogui.moveTo(_x, _y)
    time.sleep(0.05)
    pyautogui.click(_x, _y, clicks=_clicks, interval=_interval, button=_button, duration=_duration)
    time.sleep(0.05)
    pyautogui.moveTo(oldx, oldy)


def goWaitClick(_x, _y, _duration=0.0, _button='left'):
    pyautogui.moveTo(_x, _y)
    time.sleep(_duration)
    klik(_x, _y, _button=_button)


def bait():  # == yemTak()
    if solucan_skill_barda:
        time.sleep(0.05)
        BasCek(TusBir)
    else:
        solucan = lokeytCenterOnScreen('img/balikyemtus.png')
        if solucan:
            time.sleep(1)
            pyautogui.moveTo(solucan)
            klik(solucan, _button='right', _duration=1)
    time.sleep(0.1)


def oltaAt():
    time.sleep(0.1)
    BasCek(SPACE)
    fishing_actives[current_window] = True
    rod_takens[current_window] = False
    game_window_fishing_timers[current_window] = time.time()
    # pyautogui.press('space')
    time.sleep(0.1)


def oltaCek():
    BasCek(SPACE)
    fishing_actives[current_window] = False
    # pyautogui.press('space')
    time.sleep(0.05)


def ssAl(_region=None):
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


def cameraReset(_game_rect=pencere_baslangici):
    logging.debug(f"cameraReset(window:{current_window})")
    # Şimdi kameranın açısını ayarlıyoruz.
    pyautogui.moveTo(vectorial_Sum(centerOfRect(_game_rect), (-200, -200)))  # pencerenin merkezinden biraz sol üste
    time.sleep(0.1)
    pyautogui.mouseDown(button='right')
    pyautogui.moveRel(0, 1000)
    pyautogui.mouseUp(button='right')
    time.sleep(1)
    pyautogui.scroll(9000)
    time.sleep(1)
    pyautogui.scroll(-400)
    pyautogui.mouseDown(button='right')
    pyautogui.moveRel(0, -30)
    pyautogui.mouseUp(button='right')
    time.sleep(1)


def centerOfRect(x0, y0=None, x1=None, y1=None, param='distance'):
    if not y0 and len(x0) == 4:
        y0, x1, y1 = x0[1], x0[2], x0[3]
        x0 = x0[0]
    if param == 'distance':
        return x0 + (x1 / 2), y0 + (y1 / 2)
    elif param == 'lastpoint':
        return (x0 + x1) / 2, (y0 + y1) / 2
    else:
        print("centerOfRect else")
        return None


def vectorial_Sum(a, b):  # liste elemanlarını toplayabilmek için. bağıl işlemlerde falan gerekiyor.
    new_list = []
    a = list(a)
    b = list(b)
    if len(a) <= len(b):
        new_list = b
    elif len(a) > len(b):
        new_list = a
    min_len = min(len(a), len(b))
    # print(min_len)
    for _i in range(min_len):
        new_list[_i] = a[_i] + b[_i]
    return tuple(new_list)


def withOffset(_x, _y=None):  # bağıl bir noktaya offset ekleme.
    if _y:  # x,y ayrı ayrı verilmişse liste halinde alıyoruz
        b = list(_x) + list(_y)
    else:
        b = list(_x)  # x,y bir demet(tuple) olarak verilmişse
    return vectorial_Sum(list(pencere_baslangici)[:2], b)  # sadece x,y noktaları lazım diğer 2 parametreyi kesiyoruz.


def muvTuWithOffset(_x, _y):  # pencere farklı bir noktada olsa bile bağıl olarak gidebilme.
    pyautogui.moveTo(withOffset(_x, _y))


def lokeytOnScreen(needle, _region=None):
    oldx, oldy = pyautogui.position()
    pyautogui.moveTo(screensize_x, screensize_y)
    coords = pyautogui.locateOnScreen(needle, region=_region)
    pyautogui.moveTo(oldx, oldy)
    return coords


def lokeytOnWindow(needle, _region=None):
    _region = withOffset(_region)
    coords = pyautogui.locateOnScreen(needle, region=_region)
    return coords


def lokeytCenterOnScreen(needle, _region=None):
    coords = lokeytOnScreen(needle, _region=_region)
    if coords:
        return coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2)
    else:
        return None


def lokeytCenterOnWindow(needle, _region=None):  # tam ekran değil pencere koordinatları ile bağıl işlem.
    coords = lokeytOnWindow(needle, _region=_region)
    if coords:
        return coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2)
    else:
        return None


def windowEnumerationHandler(hwnd, _top_windows):  # varolan pencereleri dönmek için gerekli
    global top_windows
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def findGameWindows():  # programın başlangıcında mevcut oyun pencerelerini bulmak için
    print("findGameWindows()")
    logging.debug("findGameWindows()")
    global game_windows, game_window_dcs, game_window_rects, game_window_login_timer, game_states, pencere_baslangici, top_windows
    _top_windows = []
    game_windows = []
    game_window_dcs = []
    game_window_rects = []
    game_states = []
    game_counter = 0
    win32gui.EnumWindows(windowEnumerationHandler, None)
    for window_info in top_windows:
        # halihazırda açık olan oyun pencerelerini sayıyoruz.
        if "aeldra" in window_info[1].lower():
            game_counter += 1
    if game_counter < game_number:
        # !!! Şöyle bir sorun var: pencerelerden biri kapandığında hangisi kapandığını bilmiyoruz.
        # yanlış hesabı açmaya çalışabilir, stateler ve değişkenler karışabilir.
        print("oyun pencereleri açılıyor.")
        logging.debug("game_counter < game_number")
        open_games((game_number - game_counter))
    top_windows = []  # windowEnumerationHandler her çalıştırıldığında buraya pencereleri ekliyor tekrar tekrar yazma olmasın diye.
    win32gui.EnumWindows(windowEnumerationHandler, None)
    for window_info in top_windows:
        if "aeldra" in window_info[1].lower():
            game_windows.append(window_info[0])  # window_info[0] = w = hWnd -> win32gui
            dc_ith = win32gui.GetWindowDC(window_info[0])  # dc = hdc -> win32gui
            game_window_dcs.append(dc_ith)  # 1459688067  type: <class 'int'>
            rect_ith = win32gui.GetWindowRect(window_info[0])
            print('rect_ith: ', rect_ith)
            # benim pencerenin koordinatlarına, offset ile.
            if rect_ith != (566, 108, 1372, 736):
                win32gui.MoveWindow(window_info[0], 566, 108, 806, 628, True)
                rect_ith = win32gui.GetWindowRect(window_info[0])
                print('rect_ith(yeni): ', rect_ith)
            game_window_rects.append(rect_ith)  # rect:  (566, 108, 1372, 736)
            game_states.append('initial')
    list_pencere_extent = list(pencere_baslangici)[2:]  # pencere boyutunu sabit bırakmak için
    list_pencere_origin = list(vectorial_Sum(list(game_window_rects[0])[:2], (-4, -4)))
    pencere_baslangici = tuple(list_pencere_origin + list_pencere_extent)
    print("Pencere başlangıcı: {}".format(pencere_baslangici))
    print('game_windows: ', game_windows)
    if game_counter > game_number:
        print(f"oyun pencereleri olması gerekenden fazla: {game_counter}")
        logging.debug(f"game_counter ({game_counter}) > game_number ({game_number}) | game_windows:{game_windows}")
    # game_window_login_timer = time.time()  # 15.08.2019 23:21   yorum haline getirildi, test edilmedi.


def open_games(_game_number=game_number):
    logging.debug("open_games()")
    for _i in range(_game_number):
        os.startfile('aeldra_bin.lnk')
        print('Client başlatıldı.')
        time.sleep(3)


def close_games():
    logging.debug("close_games()")
    for p in psutil.process_iter():
        s = p.name().lower().find('aeldra_bin')
        if s != -1:
            print('{} sonlandırılıyor. İşlem:{}'.format(p.name(), p))
            print(p.exe())
            p.terminate()
            time.sleep(1)


def gameReset():
    logging.debug("gameReset()")
    print(" Oyun resetleniyor.")
    resetWindowVariables()
    resetFishingVariables()
    close_games()
    open_games()
    findGameWindows()
    for _i, _window in enumerate(game_windows):
        makeSureItIsInGame(_i)
        initializeTheWindow(_i)


def bringGameWindow(game_window):  # o pencereyi ekrana getir ve güncel pencere yap
    global current_window
    logging.debug(f"bringGameWindow({current_window})")
    win32gui.ShowWindow(game_window, 5)
    win32gui.SetForegroundWindow(game_window)
    win32gui.SetActiveWindow(game_window)
    current_window = game_windows.index(game_window)


def rgbint2rgbtuple(RGBint):  # hex olarak gelen renk bilgisini rgb'ye çevir.
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return red, green, blue


def lookForFish(_f_c_w=fish_control_window):  # arkaplandaki bir pencerede balık ara,
    for y in range(balik_ara_region[1], balik_ara_region[3] + balik_ara_region[1], 10):
        pix = win32gui.GetPixel(game_window_dcs[_f_c_w], 408, y)
        pix = vectorial_Sum(rgbint2rgbtuple(pix), (-245, -245, -245))
        pix_abs = [-pik if pik < 0 else pik for pik in pix]
        if pix_abs[0] < 10 and pix_abs[1] < 10 and pix_abs[2] < 10:  # varsa zaman damgası bas.
            print("{} | Balık algılandı! (408,{})".format(_f_c_w, y))
            #  balık çekilecek falan filan...
            fish_catch_time_stamps[_f_c_w] = time.time()
            fish_caughts[_f_c_w] = True
            break  # balık bulunduysa hala arayıp zaman damgasını bozma.


def takeTheRod(_f_c_w):  # ekranı öne getirip oltayı çek
    bringGameWindow(game_windows[_f_c_w])
    time.sleep(0.1)  # normalde 2sn ama burada gecikme olacak
    oltaCek()
    rod_takens[_f_c_w] = True
    fishing_actives[_f_c_w] = False
    fish_caughts[_f_c_w] = False
    rod_taken_time_stamps[_f_c_w] = time.time()
    pass


def initializeTheWindow(_i):  # program açıldığında pencere ilklendirme
    global current_window
    bringGameWindow(game_windows[_i])
    cameraReset()


def lookFindClickOnWindow(fname, _region=None):
    _found = lokeytCenterOnWindow('img/800e600/{}.png'.format(fname), _region=_region)
    if _found:
        klik(_found)
        return True
    return False


def lookFindPressOnWindow(fname, _pyautogui=None, _hexCode=None, _region=None):  # pyautogui çalışmıyor...
    _found = lokeytCenterOnWindow('img/800e600/{}.png'.format(fname), _region=_region)
    if _found and _pyautogui:
        pyautogui.press('{}'.format(_pyautogui))
        return True
    if _found and _hexCode:
        BasCek(_hexCode)
        return True
    return False


def logIntoAccount():
    # hata gelmeyip mal gibi ana menüde kalırsa program da mal gibi bekliyor.
    logging.debug(f"logIntoAccount({current_window})")
    _wait_seconds = time.time()
    _loop_breaker = 10
    _logged_in = False
    while not _logged_in:
        detectState(current_window)
        if game_states[current_window] == 'mainmenu':
            _found = lookFindPressOnWindow('giris_F1', _hexCode=game_window_login_buttons[current_window], _region=giris_F1_region)
            if _found:
                print("{} | logIntoAccount>if>if | Hesaba giriş yapıldı.".format(current_window))
                game_states[current_window] = 'mainmenu'
                time.sleep(3)
                _logged_in = False  # while döngüsü için
                _login_wait_timer = time.time()
                while not _logged_in:
                    dc1 = lookFindPressOnWindow('dc1', _hexCode=ENTER, _region=dc1_region)
                    dc2 = lookFindPressOnWindow('dc2', _hexCode=ENTER, _region=dc2_region)
                    dc3 = lookFindPressOnWindow('dc3', _hexCode=ENTER, _region=dc3_region)
                    if dc1 or dc2 or dc3:
                        # hata ile karşılaştıysak tekrar girmeye çalışıyoruz.
                        # BasCek(ENTER)  # !!! 16.08.2019 00:23 yorum haline getirildi.
                        lookFindPressOnWindow('giris_F1', _hexCode=game_window_login_buttons[current_window], _region=giris_F1_region)
                        time.sleep(3)
                    else:
                        sunucuya_baglaniyorsun = lokeytOnWindow('img/800e600/sunucuya_baglaniyorsun.png', _region=s_b_region)
                        s_b_timer = time.time()
                        while sunucuya_baglaniyorsun:
                            if time.time() - s_b_timer > 10:
                                print("{} saniyedir sunucuya bağlanılamıyor.".format(time.time() - s_b_timer))
                                if time.time() - s_b_timer > 30:
                                    logging.critical("BURAYA DİKKAT")
                                    gameReset()  # logIntoAccount recursive hale geliyor...
                            time.sleep(1)
                            sunucuya_baglaniyorsun = lokeytOnWindow('img/800e600/sunucuya_baglaniyorsun.png', _region=s_b_region)
                        time.sleep(3)
                        _found = lokeytOnWindow('img/800e600/char_sec_oyuna_gir.png', _region=c_s_o_g_region)
                        if _found:
                            game_states[current_window] = 'char_select'
                            _logged_in = True
                        else:
                            print("{} | logIntoAccount>while>else>else | Giriş butonu görülmüyor".format(current_window))
                            logging.warning("{} | logIntoAccount>while>else>else | Giriş butonu görülmüyor".format(current_window))
                            if time.time() - _login_wait_timer > _loop_breaker:
                                print("{} | logIntoAccount>while>else>else>if | lookFindPressOnWindow('giris_F1)".format(current_window))
                                logging.warning("{} | logIntoAccount>while>else>else>if | lookFindPressOnWindow('giris_F1)".format(current_window))
                                lookFindPressOnWindow('giris_F1', _hexCode=game_window_login_buttons[current_window],
                                                      _region=giris_F1_region)
                                break
            else:
                print("logIntoAccount()>while>if>else | F1 resmini göremiyor")
                logging.warning("logIntoAccount()>while>if>else | F1 resmini göremiyor")
        else:
            logging.warning("logIntoAccount()>while>else | BU İMKANSIZ!!!")
            print("oyun ana menüde değil")
            if time.time() - _wait_seconds > _loop_breaker:
                logging.warning(f"logIntoAccount({current_window}) | {_loop_breaker} saniye geçti ve state belirlenemedi.")
                print(f"logIntoAccount({current_window}) | {_loop_breaker} saniye geçti ve state belirlenemedi.")
                break


def logIntoGame():
    logging.debug(f"logIntoGame({current_window})")
    _found = lookFindPressOnWindow('char_sec_oyuna_gir', _hexCode=ENTER, _region=c_s_o_g_region)
    if _found:
        print("{} | logIntoGame>if | Karakter seçildi".format(current_window))
        game_states[current_window] = 'char_select'
    else:
        detectState(current_window)
        print("{} | logIntoGame>else".format(current_window))
    time.sleep(5)
    _wait_seconds = time.time()
    _loop_breaker = 10
    _found = lokeytOnWindow('img/800e600/metin2de.png', _region=metin2de_region)
    while not _found:
        _found = lokeytOnWindow('img/800e600/metin2de.png', _region=metin2de_region)
        if _found:
            game_states[current_window] = 'ingame'
            time.sleep(3)  # oyun yüklenmeden kamera ayarlamaya çalışıyor.
        elif time.time() - _wait_seconds > _loop_breaker:
            logging.warning(f"logIntoGame({current_window})>while>elif | İlginç sonuçlar doğurabilir.")
            break
    return _found


def detectState(_i):
    logging.debug(f"detectState({_i})")
    bringGameWindow(game_windows[_i])
    _state_detected = False
    _wait_seconds = time.time()
    _loop_breaker = 10
    while not _state_detected:
        _found = lokeytOnWindow('img/800e600/metin2de.png', _region=metin2de_region)
        if _found:
            game_states[current_window] = 'ingame'
            return game_states[current_window]
        _found = lokeytOnWindow('img/800e600/char_sec_oyuna_gir.png', _region=c_s_o_g_region)
        if _found:
            game_states[current_window] = 'char_select'
            return game_states[current_window]
        _found = lokeytOnWindow('img/800e600/giris_F1.png', _region=giris_F1_region)
        print("{} | detectState/lokeytOnWindow('giris_F1'): ".format(_i), _found)
        if _found:
            game_states[current_window] = 'mainmenu'
            return game_states[current_window]
        else:
            logging.warning(f"detectState({_i}) | else: state belirlenemedi.")
            print('{} | state belirlenemedi'.format(_i))
            if time.time()-_wait_seconds > _loop_breaker:
                logging.warning(f"detectState({current_window}) | {_loop_breaker} saniye geçti ve state belirlenemedi.")
                print(f"detectState({current_window}) | {_loop_breaker} saniye geçti ve state belirlenemedi.")
                break
    return False


def makeSureItIsInGame(_i):
    logging.debug(f"makeSureItIsInGame({_i})")
    bringGameWindow(game_windows[_i])
    game_states[_i] = 'initial'
    while game_states[_i] != 'ingame':
        if game_states[_i] == 'initial':
            detectState(_i)
        if game_states[_i] == 'mainmenu':
            logIntoAccount()
        elif game_states[_i] == 'char_select':  # or game_states[_i] == 'ingame_exiting':
            logIntoGame()
        else:
            print("{} | makeSureItIsInGame>while>else | state:{}".format(_i, game_states[_i]))
            logging.debug("{} | makeSureItIsInGame>while>else | state:{}".format(_i, game_states[_i]))
            detectState(_i)
    if lokeytOnWindow('img/800e600/metin2de.png', _region=metin2de_region):
        return True
    else:
        return False


logging.info("Program started.")


def inGameReLogin():
    global i, window, game_window_login_timer
    in_game_relogin_flag = False  # yeni boolean
    # Oyundan çık, tekrar gir, ilklendirmeleri yap
    print("Burada oyundan çıkma işlemleri")
    logging.debug("Burada oyundan çıkma işlemleri")
    for i, window in enumerate(game_windows):  # Burada oyundan çıkma işlemleri
        takeTheRod(i)
        bringGameWindow(window)
        found = lookFindClickOnWindow('ayarlar', _region=settings_region)  # return bool
        if found:
            game_states[i] = 'ingame'
        else:
            print(f"{i} | Oyundan çıkılacakken ayarlar simgesi bulunamadı.")
            logging.warning(f"{i} | Oyundan çıkılacakken ayarlar simgesi bulunamadı.")
        found = lookFindClickOnWindow('cikis_ingame', _region=cikis_ingame_region)
        if found:
            game_states[i] = 'mainmenu'
        else:
            print(f"{i} | Ayarlar simgesi bulunamadığı için 'cikis_ingame de bulunamadı.")
            logging.warning(f"{i} | Ayarlar simgesi bulunamadığı için 'cikis_ingame de bulunamadı.")
    print("Burada oyuna girme işlemleri")
    logging.debug("Burada oyuna girme işlemleri")
    for i, window in enumerate(game_windows):  # Burada oyuna girme işlemleri
        bringGameWindow(window)
        makeSureItIsInGame(i)
        # logIntoAccount()
        # lookFindPressOnWindow('char_sec_oyuna_gir', _hexCode=ENTER, _region=c_s_o_g_region)
    print("Burada oyun-içi son rötuşlar.")
    logging.debug("Burada oyun-içi son rötuşlar.")
    for i, window in enumerate(game_windows):  # Burada oyun-içi son rötuşlar.
        bringGameWindow(window)
        ingame = lokeytOnWindow('img/800e600/metin2de.png', _region=metin2de_region)
        if ingame:
            game_states[i] = 'ingame'
            initializeTheWindow(i)
            game_window_login_timer = time.time()

in_game_relogin_flag = False
while True:
    try:
        time.sleep(1)
        findGameWindows()
        for i, window in enumerate(game_windows):
            makeSureItIsInGame(i)
            initializeTheWindow(i)
        while True:
            for i, window in enumerate(game_windows):
                if not fishing_actives[i] and time.time() - rod_taken_time_stamps[i] > 5:  # balık tutulmuyorsa yem takıp olta at
                    bringGameWindow(window)
                    bait()
                    oltaAt()
                    print("{} | Olta atıldı".format(i))
                elif fish_caughts[i] and time.time() - fish_catch_time_stamps[i] > fish_wait_timers[i]:
                    # print("{} | Balık görüldü süre doldu balık çekiliyor".format(i))
                    takeTheRod(i)
                    balik_gelmedi_counters[i] = 0
                elif not fish_caughts[i] and time.time() - game_window_fishing_timers[i] < max_fishing_wait:
                    lookForFish(i)
                    # print("{} | Balık bekleniyor".format(i))
                elif not fish_caughts[i] and time.time() - game_window_fishing_timers[i] > max_fishing_wait:
                    state = detectState(i)
                    byb = lookFindClickOnWindow("b_y_basla", _region=b_y_basla_region)
                    if byb:
                        logging.WARNING(f"{i} | Çar yatmış.")
                        _temp = game_window_login_buttons[i]
                        game_window_login_buttons[i] = game_window_backup_buttons[i]
                        game_window_backup_buttons[i] = _temp
                        in_game_relogin_flag = True
                    initializeTheWindow(i)
                    if not state == 'ingame':
                        print('Pencere oyun-içinde değil, oyuna sokuluyor.')
                        makeSureItIsInGame(i)
                        initializeTheWindow(i)
                    if not rod_takens[i]:
                        takeTheRod(i)
                        # print(time.time() - game_window_fishing_timers[i])
                        print("{} | Balık {}sn boyunca gelmedi.".format(i, max_fishing_wait))
                        logging.warning("{} | Balık {}sn boyunca gelmedi.".format(i, max_fishing_wait))
                        balik_gelmedi_counters[i] += 1
                        if balik_gelmedi_counters[i] > 3:
                            logging.warning(f"balik_gelmedi_counters[{i}] > 3 | Oyun resetleniyor.")
                            gameReset()  # !!! 10.08.2019 test edilmedi.
            if time.time() - game_window_login_timer > 1800 or in_game_relogin_flag:  # 3600:  # oyuna gireli yarım saat oldu ise
                logging.debug("time.time() - game_window_login_timer > 1800")
                print(time.time() - game_window_login_timer)
                inGameReLogin()  # Oyundan çıkma işlemleri fonksiyon haline getirildi.
    except Exception as e:
        logging.exception("Exception occurred", exc_info=True)
        close_games()
        # gameReset()
