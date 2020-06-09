import pyautogui, time, win32api, win32con, ctypes, winsound
from PIL import Image

# imaj dosyasını ikinci bir imaj dosyasında yada ekranda belirli bir toleransla aramak.

def lokeyt(needle,haystack=None,tolerans=0,region=None,yuzdtahammul=35):

    nImage = Image.open(needle)
    hImage = Image.open(haystack)
    screenwidth, screenheight = pyautogui.size()
    if region == None:
    # region belirlenmemişse
        if haystack == None:
        #ekranda işlem yapılacaksa haystack olarak ekran görüntüsü; region olarak da ekran çözünürlüğü seçiliyor.
            haystack = pyautogui.screenshot()
            width,height = pyautogui.size()
            region = (0,0,width,height)
        else:
        #haystack varsa region olarak onun sınırları seçiliyor.
            width,height = hImage.size[0],hImage.size[1]
            region = (0,0,width,height)
    else:
        width, height = region[0]+region[2], region[1]+region[3]

    # needle ve haystackin ölçüleri belirleniyor.
    n_width, n_height = nImage.size
    hsmax_x, hsmax_y = (region[0]+region[2],region[1]+region[3])
    #needleın karşılaştırılan piksel koordinatı
    needlex, needley = 0,0
    #needleın taranmaya başlandığı koordinat
    hsoriginx, hsoriginy = region[0], region[1]

    needlepixel = nImage.getpixel((needlex, needley))

    farklılık=0
    tahammül= int((n_width*n_height*yuzdtahammul)/100)

    # haystack satır satır for döngüsüne sokuluyor.
    for hsy in range(hsoriginy, hsmax_y):
        # satırdaki herbir eleman işleme alınıyor.
        for hsx in range(hsoriginx, hsmax_x):
            #print("*",hsx, hsy)

            if hsx + n_width > width and hsy + n_height > height:
                #print("*",hsx, hsy)
                return None

            if hsx + n_width > width:
                break
            hspixel = hImage.getpixel((hsx, hsy))
            #İlk pikseli haystackta bir pikselle eşleştiriyoruz.
            if abs(needlepixel[0]-hspixel[0])<=tolerans and abs(needlepixel[1]-hspixel[1])<=tolerans and abs(needlepixel[2]-hspixel[2])<=tolerans:
                farklılık=0
                #print("İlk piksel eşlendi!",hsx,hsy)
                #print(needlepixel,hspixel)
                #uyan bu piksel bizim arayacağım alanın orijini oluyor.
                NewOriginX, NewOriginY  = hsx, hsy

                nx,ny = 0,0
                #bu orijin noktasından needle'ın boyutlarında bir alanı needle'ımız ile karşılaştırmaya başlıyoruz.
                for columnelement in range(hsy,hsy+n_height):
                    for rowelement in range(hsx,hsx+n_width):
                        #print("**",rowelement,columnelement)

                        if rowelement > width or columnelement > height:
                            #print("**")
                            return None
                        #for döngüsü içerisinde her seferin karşılaştırılacak pikselleri burada belirliyoruz.
                        npix = nImage.getpixel((rowelement-NewOriginX,columnelement-NewOriginY))
                        hpix = hImage.getpixel((rowelement, columnelement))
                        if abs(npix[0] - hpix[0]) <= tolerans and abs(npix[1] - hpix[1]) <= tolerans and abs(npix[2] - hpix[2]) <= tolerans:
                        #eğer pikseller uyuyorsa bir sonraki pikseli karşılaştırmaya geçiyoruz.
                            if rowelement == hsx+n_width-1 and columnelement == hsy+n_height-1:
                            #eğer needle'ın son pikseline kadar eşleşme sağlanmışsa resimler eşleşmiş demektir.
                                return (NewOriginX,NewOriginY,n_width,n_height)
                        else:
                        #eğer pikseller uymuyorsa döngüyü kırıp ilk pikselle eşleşen yeni bir nokta arıyoruz.
                            #print("farklılık:", farklılık)
                            farklılık+=1
                            if farklılık>tahammül:


                                break
                    if farklılık > tahammül:
                        farklılık = 0
                        break

                    if rowelement == hsx+n_width-1 and columnelement == hsy+n_height-1:
                    #bu kısmın gerekli olup olmadığını bilmiyorum.
                        break
            elif hsx == hsmax_x-1 and hsy == hsmax_y-1:
            #eğer region içerisinde ilk pikselle eşleşen bir piksel bulunmazsa False çıktısı verir.
                return None
# C struct redefinitions
SendInput = ctypes.windll.user32.SendInput

TusBir = 0x02
TusIki = 0x03
TusUc = 0x04
W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Z = 0x2C
R = 0x13
I = 0x17
P = 0x19
CTRL = 0x1D
ALT = 0x38
SPACE = 0x39
F1 = 0x3B
F2 = 0x3C
F3 = 0x3D


PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def BasCek(tus, sure=0.2):
    PressKey(tus)
    time.sleep(sure)
    ReleaseKey(tus)

def click(x=-1, y=-1):
    if x == -1 and y == -1:
        x, y = pyautogui.position()
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.1)

def PressMouse(x=-1,y=-1):
    if x == -1 and y == -1:
        x, y = pyautogui.position()
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
def ReleaseMouse(x=-1,y=-1):
    if x == -1 and y == -1:
        x, y = pyautogui.position()
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.1)

def BenzerMi(needle, needlex, needley, screenx=0, screeny=0, tolerans=20):
    benzerlik = 0
    fark = 0
    for i in range(0, needlex):
        for j in range(0, needley):
            im1 = Image.open(needle)
            pik1 = im1.getpixel((i, j))
            pik2 = pyautogui.pixel(screenx + i, screeny + j)
            for k in range(0, 3):
                fark = abs(pik1[k] - pik2[k])
                print(fark)
                if fark < tolerans:
                    benzerlik += 1 / 3
    return benzerlik


###Buradan sonra programı yazacağız.
HTC = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/hedeftamcan.png'
HC = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/HedefÇubuğu.png'
HPbos = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/hpbos.png'
HPdolu = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/hpdolu.png'
MPdolu = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/manadolu.png'
Can0 = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/0can.png'
ConfirmButton = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/confirmbutton.png'
SonEnvSlot = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/sonenvslotu.png'
Envanter = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/envanter.png'
Inventory = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/inventory.png'
PetYem = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/petyem.png'
PetItem = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/petitem.png'
PetinYemi = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/petinyemi.png'
Feedin = 'C:/Users/Yasin/Desktop/Paytın/KınaytGUIDNM/feedin.png'
while True:
#programın sürekli döngüsünü kuruyoruz.
    ...
    #windows çubuğuna bağlı while döngüsü
    #Bu kısımda oyunda olup olmadığımız kontrol edilip gerekli işlemler yapılacak.
        #windows çubuğunu kontrol et.
        #eğer windows çubuğu varsa:
            #oyunun simgesini çubukta ara, oyunu 1.sekmeye taşı.
            #ctrl+win+1 yap
        #eğer windows çubuğu yoksa:
            #'oyunda' resmini ekranda ara.
            #eğer bulamazsan:
                # 'win' tuşuna bas.
            #eğer bulursan:
                # döngüyü sonlandır ve sonraki işlemlere geç
    ...
    #kasma döngüsü başlamadan önce ilk kontroller yapılıyor.
        #pet çağırılmış durumda mı?
        #pet toplama işlevinde mi?
    zaman = 1
    while zaman<:
    #oyun döngüsü başlıyor.
        BasCek(Z)

        hedef = pyautogui.locateOnScreen(HC,region=(660,30,20,40))
        if hedef != None:
            BasCek(R)
            time.sleep(1)
        htamcan = pyautogui.locateOnScreen(HTC,region=(770,30,10,40))
        while hedef != None and htamcan==None:
            time.sleep(0.5)
            hedef = pyautogui.locateOnScreen(HC, region=(660, 30, 20, 40))

        if pyautogui.locateOnScreen(HPbos, region=(73, 35, 2, 14)):
            BasCek(TusBir)

        if not pyautogui.locateOnScreen(MPdolu, region=(73, 52, 2, 12)):
            BasCek(TusIki)
        BasCek(W,0.4)

    if pyautogui.locateOnScreen(Can0,region=(108,36,8,14)):
        confirm = pyautogui.locateCenterOnScreen(ConfirmButton,region=(659,437,45,3))
        winsound.Beep(500,3000)

    BasCek(I)
    if pyautogui.locateOnScreen(Inventory,region=(1147,101,43,7)):
        if pyautogui.locateOnScreen(SonEnvSlot, region=(1325,595,24,24))==None:
            winsound.Beep(1000,100)

    if not pyautogui.locateOnScreen(PetYem,region=(255,53,2,9)):
        BasCek(P)
        petitemx, petitemy = pyautogui.locateCenterOnScreen(PetItem,region=(1140,33,53,18))
        pyautogui.moveTo(petitemx, petitemy)
        click()
        petinyemix, petinyemiy = pyautogui.locateCenterOnScreen(PetinYemi, region=(1030,220,325,190))
        pyautogui.moveTo(petinyemix,petinyemiy)
        PressMouse()
        feedinx, feediny = pyautogui.locateCenterOnScreen(Feedin,region=(1302,143,35,30))
        pyautogui.moveTo(feedinx,feediny,duration=1)
        ReleaseMouse()



