import pyautogui,keyboard,time,datetime,os,winsound,psutil

run_this = True
runtime_state = 'initial'
which_channel = 1
captcha_counter = 0
states = ["main_menu_state","choose_character_state","is_in_game_state","fishing_state","exit_to_main_menu_state"]
img_folder = 'img/{}.png'
images = ['baglan_button','basla_button','m2de_button','guvenli_giris_info','guvenli_giris_click'
        ,'sifre_onaylandi_info','svside_info','settings_button','menu_info','ch1_button','karakter_degisikligi_button']
images_and_regions = {  "baglan_button":                    ( 731,395, 79, 22),
                        "basla_button" :                    ( 600,685, 85, 25),
                        "m2de_button" :                     (1222,734, 32, 32),
                        "guvenli_giris_info" :              ( 650,300, 60, 10),
                        "guvenli_giris_click" :             ( 652,367, 61, 18),
                        "sifre_onaylandi_info" :            ( 648,366, 69, 10),
                        "sifre_hatali_info" :               ( 651,366, 63, 10),
                        "olta_button" :                     ( 600,745,270, 22),
                        "svside_info" :                     ( 987,462, 40, 10),
                        "settings_button" :                 (1324,734, 32, 32),
                        "menu_info" :                       ( 671,254, 24,  7),
                        "ch1_button" :                      ( 605,279, 18,  7),
                        "karakter_degisikligi_button" :     ( 641,413, 84, 10),
                        "envanter_ici" :                    (1189,387,160,287),
                        "burada_yeniden" :                  ( 102, 79, 95,  7),
                        "cikis_button" :                    ( 673,443, 20, 10),
                        "oyun_sonu_button" :                ( 657,484, 52,  9),
                        "oyunu_baslat_gri" :                ( 819,620,200,100),
                        "oyunu_baslat_yesil" :              ( 819,620,200,100)}
tus_map = {'tus1': (985 + 47 * 0, 345 + 25 * 0),
           'tus2': (985 + 47 * 1, 345 + 25 * 0),
           'tus3': (985 + 47 * 2, 345 + 25 * 0),
           'tus4': (985 + 47 * 0, 345 + 25 * 1),
           'tus5': (985 + 47 * 1, 345 + 25 * 1),
           'tus6': (985 + 47 * 2, 345 + 25 * 1),
           'tus7': (985 + 47 * 0, 345 + 25 * 2),
           'tus8': (985 + 47 * 1, 345 + 25 * 2),
           'tus9': (985 + 47 * 2, 345 + 25 * 2),
           'tusTemizle': (985 + 47 * 0, 345 + 25 * 3),
           'tus0': (985 + 47 * 1, 345 + 25 * 3),
           'tusSil': (985 + 47 * 2, 345 + 25 * 3),
           'tusTamam': (1035,445)
           }
choose_account = (1200,110)
guvenli_giris_pw = [224135,22435]

def ss_al(_region=None):
    an = datetime.datetime.now()
    ay = an.month
    gun = an.day
    saat = an.hour
    dakika = an.minute
    saniye = an.second
    # ss'lerin adları çekildikleri zaman oluyor.
    save_path = 'C:/Users/Yasin/Desktop/Loglar/{:02d}-{:02d}_{:02d}.{:02d}.{:02d}.png'.format(ay, gun, saat, dakika, saniye)
    pyautogui.screenshot(save_path,region=_region)
    print("SS alındı.")
    time.sleep(0.2)

def log_al(_log):
    an = datetime.datetime.now()
    ay = an.month
    gun = an.day
    saat = an.hour
    dakika = an.minute
    saniye = an.second
    # ss'lerin adları çekildikleri zaman oluyor.
    current_time = '{:02d}/{:02d}   {:02d}:{:02d}:{:02d}.png'.format(ay, gun, saat, dakika,saniye)
    with open("log.txt", "a") as f:
        text = str(current_time)+"\t{}\n".format(_log)
        f.write(text)
def format_img_path(_img_name = None):
    if _img_name:
        look_for = img_folder.format(_img_name)
    return look_for


def look_find_locate(_png_name, _positive_state=None,_negative_state=None, _sleep_time=1, _sabir_power=5):
    global runtime_state
    sabir = 0
    curr_pos_x,curr_pos_y = pyautogui.position()
    pyautogui.moveTo(1366,768)
    png = pyautogui.locateCenterOnScreen(format_img_path(_png_name)
                                                    ,region=images_and_regions[_png_name])
    while not png:
        sabir += 1
        if sabir > _sabir_power:
            print(_png_name,' bulunamadı.')
            runtime_state = "error"
            break
        png = pyautogui.locateCenterOnScreen(format_img_path(_png_name)
                                                        ,region=images_and_regions[_png_name])
        print(_png_name,' bekleniyor. Runtime State: ',runtime_state)
        time.sleep(_sleep_time)
    if png and _positive_state:
        runtime_state = _positive_state
    elif not png and _negative_state:
        runtime_state = _negative_state
    pyautogui.moveTo(curr_pos_x,curr_pos_y)
    return png


def go_wait_click(_x, _y, _duration=1, _button='left'):
    pyautogui.moveTo(_x,_y)
    time.sleep(_duration)
    pyautogui.click(button=_button)

def su_tusa_bas(_sayi):
    ilkTus = int(_sayi/10)
    ikinciTus = _sayi%10
    go_wait_click(tus_map['tus{}'.format(ilkTus[0],ilkTus[1])])
    go_wait_click(tus_map['tus{}'.format((ikinciTus[0],ikinciTus[1]))])
    go_wait_click(tus_map['tusTamam'][0],tus_map['tusTamam'][1])

def oyunu_sonlandır():
    for p in psutil.process_iter():
        s = p.name().find('Ruya2')
        if s != -1:
            print('{} sonlandırılıyor. İşlem:{}'.format(p.name(), p))
            print(p.exe())
            p.terminate()


def captcha_things():
    global runtime_state
    global captcha_counter
    svside_png = look_find_locate("svside_info", _negative_state="error")  # _negative_state="fishing_state"
    # kepçe gelirse programla aynı dizindeki 'Captchas' klasörünün içerisindeki rakamlarla karşılaştırır.
    if svside_png:
        print("captcha geldi")
        # CAPTCHA KISMI BAŞLANGIÇ
        # Captchas klasörünün içerisindeki rakamların klasörlerini listeye alır.
        klasorler = os.listdir('Captchas')
        kepçe_bulundu = None
        im = pyautogui.screenshot()
        # rakam klasörlerini for'da döndürüyoruz.
        things = []
        for i in klasorler:
            if os.path.isdir('Captchas/{}'.format(i)):
                # 'i' rakamının içerisindeki kırpıklar klasöründeki png dosyalarını listeye alır.
                rakamlar = os.listdir('Captchas/{}/kırpıklar'.format(i))
                # o rakamın png dosyalarını for'da döndürüyoruz.
                for j in rakamlar:
                    # kepçe = pyautogui.locateOnScreen('Captchas/{}/kırpıklar/{}'.format(i,j),region=(968+14-2, 298+9-2, 12+4, 12+4))
                    kepçe = pyautogui.locate('Captchas/{}/kırpıklar/{}'.format(i, j), im,grayscale=True,
                                             region=(968 + 14 - 2, 298 + 9 - 2, 12 + 4, 12 + 4))
                    thing = '{}/{}'.format(i,j)
                    things.append(thing)
                    if kepçe:
                        kepçe_bulundu = i
                        print('kepçe bulundu')
                        winsound.Beep(1000,1000)
                        winsound.Beep(500,500)
                        winsound.Beep(1000,1000)
                        log_al('kepçe bulundu: {}/{}'.format(i, j))
                        break
        print(things)
        # eğer kepçe zaten elimizde varsa kanal değiştirir.
        if kepçe_bulundu:
            # su_tusa_bas(kepçe_bulundu)
            runtime_state = "change_channel_state"
        # yoksa kepçeyi kaydeder ve kanal değiştirir.
        else:
            print('kepçe bulunamadı')
            log_al('...\n')
            pyautogui.moveRel(0, -100, 1)
            ss_al(_region=(968, 298, 40, 30))
            captcha_counter += 1
            runtime_state = "change_channel_state"
        if captcha_counter % 31 == 0:
            runtime_state = "exit_to_main_menu_state"
        if captcha_counter % 90 == 0:
            runtime_state = "close_the_game"
    # CAPTCHA KISMI SON


# -------------------------------------------
try:
    while run_this:
        #program ilk açıldığında bu durumdadır ve oyunun anamenüsünde olup olmadığımızı kontrol eder.
        if runtime_state == 'initial':
            look_find_locate("baglan_button","main_menu","error")
        #oyunun ana ekranında olduğumuz durum.
        if runtime_state == 'main_menu':
            #kanal1'e tıklar.
            go_wait_click(545, 410)
            which_channel = 1
            #kayıtlı ilk hesabı seçer.
            go_wait_click(choose_account[0], choose_account[1])
            basla_png = look_find_locate("basla_button", "character_menu","initial")
            #başla butonu varsa karakter ekranı durumuna geçer ve başla'ya tıklar.
            if basla_png:
                go_wait_click(basla_png[0],basla_png[1])
        #15 saniye boyunca oyuna girmeyi bekler, girerse oyuniçi durumuna geçer giremezse hata durumuna geçer.
        if runtime_state == 'character_menu':
            m2_png = look_find_locate("m2de_button","in_game_state","error",_sabir_power=15)
        #5 saniye boyunca güvenli girişin gelmesini bekler, girerse güvenli girişe tıklamaya geçer giremezse kepçe bekler.
        if runtime_state == 'in_game_state':
            look_find_locate("guvenli_giris_info","guvenli_giris_state","captcha_state", _sabir_power=5)
        #güvenli giriş varsa tıklar, şifreyi yazar.
        if runtime_state == 'guvenli_giris_state':
            guvenli_click_png = look_find_locate("guvenli_giris_click")
            if guvenli_click_png:
                go_wait_click(guvenli_click_png[0],guvenli_click_png[1])
                keyboard.write(str(guvenli_giris_pw[0]))
                keyboard.send('enter')
            sifre_onaylandi_png = look_find_locate("sifre_onaylandi_info", "captcha_state")
            if sifre_onaylandi_png:
                keyboard.send('enter')
                runtime_state = "captcha_state"
            #şifre hatalı derse tekrar şifreyi girer.
            else:
                sifre_hatali_png = look_find_locate("sifre_hatali_info","guvenli_giris_state")
                if sifre_hatali_png:
                    keyboard.send('enter')
                    olta_png = look_find_locate("olta_button")
                    go_wait_click(olta_png[0], olta_png[1], _button='right')
        #oltaya tıklayarak kepçe getirmeye çalışır.
        if runtime_state == 'captcha_state':
            #captcha_things()
            #print("1. captcha_things() bitti.")
            olta_png = look_find_locate("olta_button")
            if olta_png:
                go_wait_click(olta_png[0], olta_png[1], _button='right')
            captcha_things()
        #oyunu kapatıyoruz.
        if runtime_state == "close_the_game":
            settings_png = look_find_locate("settings_button")
            if settings_png:
                go_wait_click(settings_png[0], settings_png[1])
                menu_png = look_find_locate("menu_info")
                # menü ekranı açılırsa ch1'i bulmaya çalışır.
                if menu_png:
                    oyun_sonu_png = look_find_locate("oyun_sonu_button","game_is_closed")
                    if oyun_sonu_png:
                        go_wait_click(oyun_sonu_png[0],oyun_sonu_png[1])
                        time.sleep(3)
        #ana menüye geçiş yapıyoruz.
        if runtime_state == "exit_to_main_menu_state":
            settings_png = look_find_locate("settings_button")
            if settings_png:
                go_wait_click(settings_png[0], settings_png[1])
                menu_png = look_find_locate("menu_info")
                # menü ekranı açılırsa ch1'i bulmaya çalışır.
                if menu_png:
                    cikis_png = look_find_locate("cikis_button")
                    if cikis_png:
                        go_wait_click(cikis_png[0],cikis_png[1])
                        runtime_state = "initial"
        #kanal değiştirme durumundaysak ayarlar'a tıklar
        if runtime_state == 'change_channel_state':
            settings_png = look_find_locate("settings_button")
            if settings_png:
                go_wait_click(settings_png[0], settings_png[1])
                menu_png = look_find_locate("menu_info")
                #menü ekranı açılırsa ch1'i bulmaya çalışır.
                if menu_png:
                    ch1_png = look_find_locate("ch1_button")
                    #ch1'i bulursa hangi kanalda ise bir sonraki kanala geçer.
                    if ch1_png:
                        go_wait_click(ch1_png[0] + 46 * (which_channel % 4), ch1_png[1])
                    m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                        , region=images_and_regions['m2de_button'])
                    m2de_sabir = 0
                    #kanal değiştirmeye tıkladıktan sonra yükleme ekranına geçene kadar (max 15sn) burada döner.
                    while m2de_png:
                        m2de_sabir += 1
                        time.sleep(1)
                        m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                            , region=images_and_regions['m2de_button'])
                        if not m2de_png:
                            print("m2de kayboldu")
                        #15sn'den fazla olduysa beklemeyi bırakır.
                        if m2de_sabir > 15:
                            print("m2de sabır taştı #1")
                            break
                    #while'dan çıktıktan sonra programı hata durumuna getirip en başa döndürür.
                    if m2de_sabir >=15:
                        runtime_state = 'error'
                        continue
                    m2de_sabir=0
                    #oyun yükleme ekranından tekrar oyuna geçene kadar (max 15sn) burada döner.
                    while not m2de_png:
                        m2de_sabir += 1
                        time.sleep(1)
                        m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                            , region=images_and_regions['m2de_button'])
                        #Eğer kanal düzgün şekilde değiştirilmişse hangi kanalda olduğunu güncelle ve durumu değiştir.
                        if m2de_png:
                            which_channel += 1
                            runtime_state = 'in_game_state'
                            print("m2de bulundu")
                        if m2de_sabir > 15:
                            print("m2de sabır taştı #2")
                            break
                    #while'dan çıktıktan sonra programı hata durumuna getirip en başa döndürür.
                    if m2de_sabir >=15:
                        runtime_state = 'error'
                        continue
        if runtime_state == 'error':
            winsound.Beep(1000,1000)
            m2_png = look_find_locate("m2de_button", "in_game_state", _sabir_power=5)
            if not m2_png:
                basla_png = look_find_locate("basla_button", "character_menu")
                if basla_png:
                    print('Karakter ekranındasın.')
                    go_wait_click(basla_png[0], basla_png[1])
                if not basla_png :
                    look_find_locate("baglan_button", "main_menu", "game_is_closed")
        if runtime_state == "game_is_closed":
            time.sleep(3)
            oyunu_sonlandır()
            os.startfile('Rüya2.lnk')
            print('Client başlatıldı.')
            time.sleep(3)
            while look_find_locate("oyunu_baslat_gri",_sabir_power=1):
                print("Client'ın hazır olması bekleniyor.")
            baslat_yesil_png = look_find_locate("oyunu_baslat_yesil","initial")
            if baslat_yesil_png:
                go_wait_click(baslat_yesil_png[0],baslat_yesil_png[1])
                time.sleep(3)
                pyautogui.keyDown('alt')
                while not look_find_locate("baglan_button",_sabir_power=2): #or not look_find_locate("basla_button",_sabir_power=2) or not look_find_locate("m2de_button",_sabir_power=2):
                    pyautogui.press('tab')
                pyautogui.keyUp('alt')

except (NameError,ValueError,AttributeError,WindowsError,OSError,IOError) as h:
    print('ERROR: ',h)
    winsound.Beep(5000,3000)
