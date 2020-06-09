import pyautogui, time, datetime, keyboard

run_this = True
runtime_state = 'initial'
runtime_states = ('initial','main_menu','character_menu','in_game_state','guvenli_giris_state','captcha_state'
    ,'change_channel_state','change_character_state','change_account_state','error')
which_account = 0
which_channel = 1
which_character = 1
choose_account = (1200,110)
sabir_tasi = 0
image_step = 0
img_folder = 'C:/Users/Yasin/Desktop/Paytın/CaptchaCollector/img/{}.png'
images = ['baglan_button','basla_button','m2de_button','guvenli_giris_info','guvenli_giris_click'
        ,'sifre_onaylandi_info','svside_info','settings_button','menu_info','ch1_button','karakter_degisikligi_button']
images_and_regions = {"baglan_button":                  ( 731,395, 79,22),
                      "basla_button" :                  ( 600,685, 85,25),
                      "m2de_button" :                   (1222,734, 32,32),
                      "guvenli_giris_info" :            ( 650,300, 60,10),
                      "guvenli_giris_click" :           ( 652,367, 61,18),
                      "sifre_onaylandi_info" :          ( 648,366, 69,10),
                      "sifre_hatali_info" :             ( 651,366, 63,10),
                      "olta_button" :                   ( 600,745,270,22),
                      "svside_info" :                   ( 987,462, 40,10),
                      "settings_button" :               (1324,734, 32,32),
                      "menu_info" :                     ( 671,254, 24, 7),
                      "ch1_button" :                    ( 605,279, 18, 7),
                      "karakter_degisikligi_button" :   ( 641,413, 84,10)}
guvenli_giris_pw = [224135,22435]

def ss_al(_region=None):
    an = datetime.datetime.now()
    ay = an.month
    gun = an.day
    saat = an.hour
    dakika = an.minute
    saniye = an.second
    # ss'lerin adları çekildikleri zaman oluyor.
    save_path = 'C:/Users/Yasin/Desktop/Loglar/{}-{}_{}.{}.{}.png'.format(ay, gun, saat, dakika, saniye)
    pyautogui.screenshot(save_path,region=_region)
    print("SS alındı.")
    time.sleep(0.2)


def format_img_path(_img_name = None):
    if _img_name == None:
        look_for = 'C:/Users/Yasin/Desktop/Paytın/CaptchaCollector/img/{}.png'.format(images[image_step])
    else:
        look_for = 'C:/Users/Yasin/Desktop/Paytın/CaptchaCollector/img/{}.png'.format(_img_name)
    return look_for


def look_find_click(_png_name, _next_state=None, _sleep_time=1, _sabir_power=100):
    global runtime_state
    sabir = 0
    png = pyautogui.locateCenterOnScreen(format_img_path(_png_name)
                                                    ,region=images_and_regions[_png_name])
    while not png:
        sabir += 1
        if sabir > _sabir_power:
            print(_png_name,' bulunamadı.')
            runtime_state = "error"
            return None
        png = pyautogui.locateCenterOnScreen(format_img_path(_png_name)
                                                        ,region=images_and_regions[_png_name])
        print(_png_name,' bekleniyor.')
        time.sleep(_sleep_time)
    if _next_state:
        runtime_state = _next_state
    return png


def go_wait_click(_x, _y, _duration=1, _button='left'):
    pyautogui.moveTo(_x,_y)
    time.sleep(_duration)
    pyautogui.click(button=_button)

while run_this:
    if runtime_state == 'initial':
        look_find_click("baglan_button","main_menu")
        """baglan_png = pyautogui.locateOnScreen(format_img_path('baglan_button')
                                                    ,region=images_and_regions['baglan_button'])
        while not baglan_png:
            baglan_png = pyautogui.locateOnScreen(format_img_path('baglan_button')
                                                        ,region=images_and_regions['baglan_button'])
            print("program baglan_png'yi arıyor.")
            time.sleep(1)
        if baglan_png:
            runtime_state = 'main_menu'"""
    if runtime_state == 'main_menu':
        which_F = 'f{}'.format(which_account+1)
        print('which_F: ', which_F)
        go_wait_click(545,410)
        go_wait_click(choose_account[0],choose_account[1]+48*which_account)
        #pyautogui.click(choose_account[0],choose_account[1]+48*which_account,duration=1)
        basla_png = look_find_click("basla_button","character_menu")
        """basla_png = pyautogui.locateCenterOnScreen(format_img_path('basla_button')
                                                    ,region=images_and_regions['basla_button'])
        while not basla_png:
            basla_png = pyautogui.locateCenterOnScreen(format_img_path('basla_button')
                                                        ,region=images_and_regions['basla_button'])
            print("program basla_png'yi arıyor.")
            time.sleep(1)
        if basla_png:
            runtime_state = 'character_menu'"""
        if basla_png:
            go_wait_click(basla_png[0],basla_png[1])
    if runtime_state == 'character_menu':
        #keyboard.send('{}'.format(which_character),'enter')
        #pyautogui.press('enter')
        #pyautogui.moveTo(basla_png[0],basla_png[1],1)
        #pyautogui.click()
        look_find_click("m2de_button","in_game_state")
        """m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                    ,region=images_and_regions['m2de_button'])
        while not m2de_png:
            m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                        ,region=images_and_regions['m2de_button'])
            print("program m2de_png'yi arıyor.")
            time.sleep(1)
            #pyautogui.press('enter')
        if m2de_png:
            runtime_state = 'in_game_state'"""
    if runtime_state == 'in_game_state':
        look_find_click("guvenli_giris_info","guvenli_giris_state")
        """guvenli_giris_png = pyautogui.locateOnScreen(format_img_path("guvenli_giris_info")
                                                    ,region=images_and_regions["guvenli_giris_info"])
        while not guvenli_giris_png:
            guvenli_giris_png = pyautogui.locateOnScreen(format_img_path("guvenli_giris_info")
                                                        ,region=images_and_regions["guvenli_giris_info"])
            print("program guvenli_giris_png'yi arıyor.")
            time.sleep(1)
        if guvenli_giris_png:
            runtime_state = 'guvenli_giris_state'"""
    if runtime_state == 'guvenli_giris_state':
        guvenli_click_png = look_find_click("guvenli_giris_click")
        """guvenli_click_png = pyautogui.locateCenterOnScreen(format_img_path("guvenli_giris_click")
                                                    ,region=images_and_regions["guvenli_giris_click"])
        while not guvenli_click_png:
            guvenli_click_png = pyautogui.locateOnScreen(format_img_path("guvenli_giris_click")
                                                        ,region=images_and_regions["guvenli_giris_click"])
            print("program guvenli_click_png'yi arıyor.")
            time.sleep(1)"""
        if guvenli_click_png:
            go_wait_click(guvenli_click_png[0],guvenli_click_png[1])
            """pyautogui.moveTo(guvenli_click_png[0],guvenli_click_png[1],1)
            pyautogui.click()
            time.sleep(0.5)"""
            #pyautogui.typewrite(str(guvenli_giris_pw[which_account]),interval=0.25)
            keyboard.write(str(guvenli_giris_pw[which_account]))
            keyboard.send('enter')
        sifre_onaylandi_png = look_find_click("sifre_onaylandi_info","captcha_state")
        """sifre_onaylandi_png = pyautogui.locateOnScreen(format_img_path('sifre_onaylandi_info')
                                                    ,region=images_and_regions['sifre_onaylandi_info'])
        while not sifre_onaylandi_png:
            sifre_onaylandi_png = pyautogui.locateOnScreen(format_img_path('sifre_onaylandi_info')
                                                        ,region=images_and_regions['sifre_onaylandi_info'])
            print("program sifre_onaylandi_png'yi arıyor.")
            sabir_tasi += 1
            if sabir_tasi >5:
                sifre_hatali_png = pyautogui.locateOnScreen(format_img_path('sifre_hatali_info')
                                                    ,region=images_and_regions['sifre_hatali_info'])
                if sifre_hatali_png:
                    runtime_state = 'error'
                    break
            time.sleep(1)
        if sifre_onaylandi_png:
            keyboard.send('enter')
            runtime_state = 'captcha_state'"""
        if sifre_onaylandi_png:
            keyboard.send('enter')
        else:
            look_find_click("sifre_hatali_info","error")
    if runtime_state == 'captcha_state':
        for i in range(4):
            if runtime_state == 'captcha_state':
                #keyboard.send('space')
                olta_png = look_find_click("olta_button")
                """olta_png = pyautogui.locateCenterOnScreen(format_img_path("olta_button")
                                                    ,region=images_and_regions["olta_button"])
                while not olta_png:
                    olta_png = pyautogui.locateCenterOnScreen(format_img_path("olta_button")
                                                        ,region=images_and_regions["olta_button"])
                if olta_png:
                    pyautogui.moveTo(olta_png[0],olta_png[1],1)
                    pyautogui.click(button='right')"""
                go_wait_click(olta_png[0],olta_png[1],_button='right')
                svside_png = look_find_click("svside_info","change_channel_state")
                """svside_png = pyautogui.locateOnScreen(format_img_path("svside_info")
                                                    ,region=images_and_regions["svside_info"])
                while not svside_png:
                    svside_png = pyautogui.locateOnScreen(format_img_path("svside_info")
                                                        ,region=images_and_regions["svside_info"])
                if svside_png:
                    print("captcha geldi")
                    ss_al(_region=(968,298,40,30))
                    runtime_state = 'change_channel_state'"""
                if svside_png:
                    print("captcha geldi")
                    ss_al(_region=(968, 298, 40, 30))
            if runtime_state == 'change_channel_state':
                settings_png = look_find_click("settings_button")
                """settings_png = pyautogui.locateCenterOnScreen(format_img_path("settings_button")
                                                    ,region=images_and_regions["settings_button"])
                while not settings_png:
                    settings_png = pyautogui.locateCenterOnScreen(format_img_path("settings_button")
                                                        ,region=images_and_regions["settings_button"])
                    print("program settings_png'yi arıyor.")
                if settings_png:
                    pyautogui.moveTo(settings_png[0],settings_png[1],1)
                    pyautogui.click()"""
                if settings_png:
                    go_wait_click(settings_png[0],settings_png[1])
                menu_png = look_find_click("menu_info")
                """menu_png = pyautogui.locateCenterOnScreen(format_img_path("menu_info")
                                                    ,region=images_and_regions["menu_info"])
                while not menu_png:
                    menu_png = pyautogui.locateCenterOnScreen(format_img_path("menu_info")
                                                        ,region=images_and_regions["menu_info"])
                    print("program menu_png'yi arıyor.")"""
                if menu_png:
                    ch1_png = look_find_click("ch1_button")
                    """ch1_png = pyautogui.locateCenterOnScreen(format_img_path("ch1_button")
                                                    ,region=images_and_regions["ch1_button"])
                    while not ch1_png:
                        ch1_png = pyautogui.locateCenterOnScreen(format_img_path("ch1_button")
                                                        ,region=images_and_regions["ch1_button"])
                    if ch1_png:
                        pyautogui.moveTo(ch1_png[0]+46*(which_channel%4),ch1_png[1],1)
                        pyautogui.click()"""
                    if ch1_png:
                        go_wait_click(ch1_png[0]+46*(which_channel%4),ch1_png[1])

                    m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                    ,region=images_and_regions['m2de_button'])
                    while m2de_png:
                        m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                        ,region=images_and_regions['m2de_button'])
                    while not m2de_png:
                        m2de_png = pyautogui.locateOnScreen(format_img_path('m2de_button')
                                                        ,region=images_and_regions['m2de_button'])
                    #channel değişkenini 1 arttırıyoruz
                    which_channel += 1
                    runtime_state = 'captcha_state'
        which_character += 1
        runtime_state = "change_character_state"
    if runtime_state == "change_character_state":
        settings_png = look_find_click("settings_button")
        if settings_png:
            go_wait_click(settings_png[0],settings_png[1])
        karakter_degisikligi_png = look_find_click("karakter_degisikligi_button")
        if karakter_degisikligi_png:
            go_wait_click(karakter_degisikligi_png[0],karakter_degisikligi_png[1])
        """karakter_degisikligi_png = pyautogui.locateCenterOnScreen(format_img_path("karakter_degisikligi_button")
                                                    ,region=images_and_regions["karakter_degisikligi_button"])
        while not karakter_degisikligi_png:
            karakter_degisikligi_png = pyautogui.locateCenterOnScreen(format_img_path("karakter_degisikligi_button")
                                                        ,region=images_and_regions["karakter_degisikligi_button"])
            pyautogui.moveTo(karakter_degisikligi_png[0],karakter_degisikligi_png[1])
            time.sleep(0.5)
            pyautogui.click()"""
        basla_png = look_find_click("basla_button","character_menu")
        if basla_png:
            go_wait_click(88,288+45*((which_character-1)%4))
            go_wait_click(basla_png[0],basla_png[1])
        """basla_png = pyautogui.locateCenterOnScreen(format_img_path('basla_button')
                                                   , region=images_and_regions['basla_button'])
        while not basla_png:
            basla_png = pyautogui.locateCenterOnScreen(format_img_path('basla_button')
                                                       , region=images_and_regions['basla_button'])
            print("program basla_png'yi arıyor.")
            time.sleep(1)
        if basla_png:
            runtime_state = 'character_menu'"""

    print('******************************')
    print('*program buraya kadar çalıştı*')
    print('******************************')
    print('runtime_state: ', runtime_state)