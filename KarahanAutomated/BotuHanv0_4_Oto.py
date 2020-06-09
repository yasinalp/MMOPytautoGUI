import sabitler
import pyautogui,time,winsound,datetime,random,os,psutil,serial

kavim = sabitler.kavim
item_topla = sabitler.item_topla

img_map = { 'hp':       {'img_name': 'hp_empty', 'region': (107-30,7,4+30,12), 'sound_frequency': (1000), 'bar_point':'1'},
            'mp':       {'img_name': 'mp_empty', 'region': (107-30,21,4+10,12), 'sound_frequency': (5000), 'bar_point':'2'},
            'pet':      {'img_name': 'pet_empty', 'region': (1148-18,28,4+30,10), 'sound_frequency': (10000), 'bar_point':'0'},
            '90lik_hp': {'img_name': '90lik_hp', 'region': (487,741,8,8), 'sound_frequency': (11000), 'bar_point':'1'},
            '90lik_mp': {'img_name': '90lik_mp', 'region': (517,741,8,8), 'sound_frequency': (12000), 'bar_point':'2'},
            'buff1':    {'img_name': 'buff1'+kavim, 'region':(230,6,220,70), 'sound_frequency': (13000), 'bar_point':'9'},
            'buff2':    {'img_name': 'buff2'+kavim, 'region': (230, 6, 220, 70), 'sound_frequency': (14000), 'bar_point': '8'},
            'nadir':    {'img_name': 'sari', 'region': (490,130,500,500), 'sound_frequency': (15000), 'bar_point': '"'},
            'yesil_n':  {'img_name': 'yesil_nokta', 'region': (500, 275, 375, 275)},
            'hack':     {'img_name': 'hack', 'region': (120-10,360-10,40+20,14+20)},
            'ticaret':  {'img_name': 'tic_bos', 'region': (1100,250,200,95)}}
inventory_region = (1095,375,210,210)



def is_empty(empty_thing):
    global screen_per_loop
    needle = 'img/{}.png'.format(img_map[empty_thing]['img_name'])
    region = img_map[empty_thing]['region']
    result = pyautogui.locate(needle,screen_per_loop,region=region)
    return result


def empty_control(empty_things=[]):
    empties = []
    for empty_thing in empty_things:
        result = is_empty(empty_thing)
        if result:
            command = '['+img_map[empty_thing]['bar_point']+',2]'
            ardu.write(command.encode('utf-8'))
            duration = int(abs(result[0]-img_map[empty_thing]['region'][0])*1000/int(img_map[empty_thing]['region'][2]))
            winsound.Beep(img_map[empty_thing]['sound_frequency'],duration+100)
            empties.append(empty_thing)
    if empties:
        print(empties)
    return empties


def find_in_inventory(empty_thing):
    global screen_per_loop
    needle = 'img/{}.png'.format(img_map[empty_thing]['img_name'])
    region = inventory_region
    result = pyautogui.locate(needle, screen_per_loop, region=region)
    if result:
        result = centered(result)
    return result


def are_pots_empty_on_bar(pots):
    empties = []
    for pot in pots:
        if is_pot_empty_on_bar(pot):
            empties.append(pot)
    return empties


def is_pot_empty_on_bar(pot):
    global screen_per_loop
    needle = 'img/{}.png'.format(img_map[pot]['img_name'])
    region = img_map[pot]['region']
    result = pyautogui.locate(needle,screen_per_loop,region=region)
    #Eğer bulursak false, bulamazsak true gönderiyor.
    return not bool(result)


def centered(region):
    if len(region)<4:
        print(region,"4'ten az elemana sahip.")
        return region
    center = (region[0]+region[2]/2,region[1]+region[3]/2)
    return center


def yerde_item_var_mi(empty_thing):
    global screen_per_loop
    needle = 'img/{}.png'.format(img_map[empty_thing]['img_name'])
    region = img_map[empty_thing]['region']
    result = pyautogui.locate(needle, screen_per_loop, region=region)
    if result:
        result = centered(result)
        result = (result[0]+random.randint(10,50),result[1]+random.randint(2,10))
    return result


#test fonksiyonu
def yerde_item_var_mi2(empty_thing):
    global screen_per_loop
    minx,maxx = 1366,0 #ekranın son noktaları
    miny,maxy = 768,0
    needle = 'img/{}.png'.format(img_map[empty_thing]['img_name'])
    region = img_map[empty_thing]['region']
    results = list(pyautogui.locateAll(needle, screen_per_loop, region=region))
    if not results:
        return False
    for result in results:
        if result[0] < minx:
            minx = result[0]
        if result[0] > maxx:
            maxx = result[0]
        if result[1] < miny:
            miny = result[1]
        if result[1] > maxy:
            maxy = result[1]
    x = (minx + maxx)/2
    y = (miny + maxy)/2 + 2
    #print("margins: ",minx,' to ',maxx,' and ',miny,' to ',maxy)
    coord = (x, y)
    #print("coord: ", coord)
    return coord





def ss_al(_region=None):
    an = datetime.datetime.now()
    ay = an.month
    gun = an.day
    saat = an.hour
    dakika = an.minute
    saniye = an.second
    # ss'lerin adları çekildikleri zaman oluyor.
    save_path = 'SSler/{:02d}-{:02d}_{:02d}.{:02d}.{:02d}.png'.format(ay, gun, saat, dakika, saniye)
    pyautogui.screenshot(save_path,region=_region)
    print("SS alındı.")
    time.sleep(0.2)




# test fonksiyonu
def baglanti_koptu_mu2():
    # y,ymax = 492,552
    global screen_per_loop
    in_scope_sayac = 0
    yler = [491+15*i for i in range(5)]
    needle = 'img/yesil_nokta.png'
    for yesil_nokta in pyautogui.locateAll(needle,screen_per_loop):
        if yesil_nokta[0] == 152 and yesil_nokta[1] in yler:
            in_scope_sayac += 1
    return in_scope_sayac == 5


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


def hack_koruma_geldi_mi():
    global screen_per_loop
    needle = 'img/{}.png'.format(img_map['hack']['img_name'])
    region = img_map['hack']['region']
    result = pyautogui.locate(needle,screen_per_loop,region=region)
    return result


def ticarette_bos_slot_var_mi():
    global screen_per_loop
    for i in range(4):
        for j in range(2):
            needle = 'img/tic/tic{}{}.png'.format(j+1,i+1)
            region = (1093+54*i,243+j*55,5,5)
            result = pyautogui.locate(needle, screen_per_loop, region=region)
            if result:
                return centered(result)
    return None


def nerdeyim_ben():
    needle = 'img/beyaz_piksel.png'
    region = (1250,7,55,8)  # (1250,7,32,8)
    result = list(pyautogui.locateAll(needle,screen_per_loop,region=region))
    print('result: ', result)
    for sehir,sehir_ismi in zip(sabitler.kara_liste,sabitler.kara_string):
        if result == sehir:
            print("nerdesin sen: ", sehir_ismi)
            return sehir_ismi
    return None


def oyunu_sonlandir():
    ss_al()
    for p in psutil.process_iter():
        s = p.name().find('TwelveSky2')
        if s != -1:
            print('{} sonlandırılıyor. İşlem:{}'.format(p.name(), p))
            print(p.exe())
            p.terminate()


def pcyi_kapat():
    log_al("Bilgisayar kapatılıyor.")
    winsound.Beep(500,5000)
    time.sleep(0.5)
    os.system("shutdown /s /t 1")


def just_drag_maan(from_where,to_where):
    pyautogui.moveTo(from_where)
    ardu.write(b'[0,3]')
    time.sleep(1)
    print('aranıyor: ')
    read_line = (ardu.readline().decode('utf-8'))
    print(read_line.find('Mouse pressed'))
    while (read_line.find('Mouse pressed') == -1):
        time.sleep(0.1)
        read_line = (ardu.readline().decode('utf-8'))
        print(read_line)
        print("Mouse basılacak...")
    pyautogui.moveTo(to_where, duration=0.1)
    ardu.write(b'[0,4]')
    read_line = ardu.readline().decode('utf-8')
    while read_line.find('Mouse released') == -1:
        time.sleep(0.1)
        print("Mouse bırakılacak...")
    pyautogui.moveTo(1366, 768)


def just_click_maan(to_where):
    pyautogui.moveTo(to_where)
    ardu.write(b'[0,5]')
    time.sleep(0.5)
    print('is clicked?: ')
    read_line = (ardu.readline().decode('utf-8'))
    if read_line.find('Mouse pressed') != -1:
        pyautogui.moveTo(1366, 768)
    pass


def baglanti_koptu_mu():
    x,y = 153,492
    sayac = 0
    for i in range(5):
        dc = pyautogui.pixelMatchesColor(x,(y+15*i),(168,164,0))
        empty_control(['hp', 'mp', 'pet'])
        time.sleep(0.2)
        if dc:
            sayac+=1
        else:
            break
    if sayac==5:
        return True
    else:
        return False


def gereksizler_ticarete():
    global screen_per_loop
    gereksizler = ["vecize", "amazon", "selestin", "e_altin", "e_demir"]
    for gereksiz in gereksizler:
        needle = 'img/{}.png'.format(gereksiz)
        region = inventory_region
        result = pyautogui.locate(needle, screen_per_loop, region=region)
        if result:
            ticaret_slot = ticarette_bos_slot_var_mi()
            if ticaret_slot:
                print("ticarette boş slot var.")
                just_drag_maan(centered(result),centered(ticaret_slot))
                return True
            else:
                print("ticarette boş slot yok.")
    return False


def orijinal_kisim():
    global screen_per_loop
    pyautogui.moveRel(50, 50, 0.5)
    ardu.write(b'[1,9]')
    for i in range(4):
        screen_per_loop = pyautogui.screenshot()
        time.sleep(0.5)
        empty_control(['hp', 'mp', 'pet'])
    ardu.write(b'[3,1]')
    print("3 basılı durumda.")

def farkli_kisim():
    global ardu
    time.sleep(2)
    try:
        time.sleep(1)
        ardu.write(b'[1,9]')
        # Farklılık burada
        time.sleep(3)
        pyautogui.hotkey('alt', 'tab')
        just_click_maan((400, 300))
        just_click_maan((1225, 160))
        for i in range(4):
            screen_per_loop = pyautogui.screenshot()
            time.sleep(0.5)
            empty_control(['hp', 'mp', 'pet'])
        ardu.write(b'[3,0]')
        time.sleep(0.5)
        ardu.write(b'[3,1]')
        print("3 basılı durumda.")

    except:
        print("Connection Error")
        log_al("Connection Error")


def time_sleep(second):
    global screen_per_loop
    time.sleep(second)
    screen_per_loop = pyautogui.screenshot()


run_this = True
screen_per_loop = pyautogui.screenshot()
sayac = 0
ardu = serial.Serial('COM8', 9600, timeout=1)
orijinal_kisim()
last_time = time.time()
try:
    while run_this:
        current_time = time.time()
        if current_time - last_time > 60 * 10:
            ss_al()
            last_time = current_time
        sayac += 1
        screen_per_loop = pyautogui.screenshot()
        if sayac % 50 == 0:
            winsound.Beep(3000,500)
            neresi = nerdeyim_ben()
            print('neresi: ',neresi)
            if neresi:
                print("Karakterin yeri: {}.".format(neresi))
                log_al("Karakterin yeri: {}.".format(neresi))
                oyunu_sonlandir()
                pcyi_kapat()
                break
            if hack_koruma_geldi_mi():
                ss_al()
                log_al("hack_koruma görüldü!!!")
                oyunu_sonlandir()
                pcyi_kapat()
                break
            if baglanti_koptu_mu():
                ardu.write(b'[0,9]')
                ardu.close()
                print("Bağlantı hatası.")
                log_al("Bağlantı hatası. Oyun kapatıldı")
                oyunu_sonlandir()
                pcyi_kapat()
                break
        empties = are_pots_empty_on_bar(['90lik_hp', '90lik_mp'])
        for empty in empties:
            full_pot = find_in_inventory(empty)
            if full_pot:
                print(full_pot)
                just_drag_maan(full_pot, centered(img_map[empty]['region']))
            else:
                print('else. ', full_pot)
        empties = are_pots_empty_on_bar(['buff1', 'buff2'])
        for empty in empties:
            empty_control(['hp', 'mp', 'pet'])
            ardu.write(b'[3,0]')
            time_sleep(0.5)
            command = '[' + img_map[empty]['bar_point'] + ',1]'
            ardu.write(command.encode('utf-8'))
            for i in range(5):
                empty_control(['hp', 'mp', 'pet'])
                time_sleep(0.5)
            # command = '[' + img_map[empty]['bar_point'] + ',2]'
            command = '[' + img_map[empty]['bar_point'] + ',0]'
            ardu.write(command.encode('utf-8'))
            empty_control(['hp', 'mp', 'pet'])
            # time_sleep(2.5)
            for i in range(3):
                empty_control(['hp', 'mp', 'pet'])
                time_sleep(0.5)
            ardu.write(b'[3,1]')
        empty_control(['hp', 'mp', 'pet'])
        nadir_item = None
        if item_topla:
            if sayac % 10 == 0:
                gereksizler_ticarete()
            nadir_item = yerde_item_var_mi2('nadir')
            if nadir_item:
                ss_al()
                print(nadir_item)
                # ardu.write(b'[126,2]') ->çalışmıyor.
                just_click_maan(nadir_item)
        time.sleep(1)

except ConnectionError as err:
    print('ConnectionError.')
    log_al(err.args)

except OSError as err:
    print(err.args)
    log_al("OS Error: image grabbing failed")
    log_al(err.args)
    os.startfile('BotuHanv0_4_Oto.py')


except ValueError as err:
    print('Non-numeric data found in the file.')
    log_al(err.args)

except ImportError as err:
    print("NO module found")
    log_al(err.args)

except EOFError as err:
    print('Why did you do an EOF on me?')
    log_al(err.args)

except KeyboardInterrupt as err:
    print('You cancelled the operation.')
    log_al(err.args)

except Exception as err:
    print('An error occured.')
    log_al(err.args)

finally:
    ardu.close()
    pyautogui.moveRel(0, -100, 0.1)
    log_al("Program Sonlandırıldı")
