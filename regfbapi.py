import requests
import json
import random
import time
import hashlib

def _random_birthday():
    start_date = time.mktime(time.strptime('1980-01-01', '%Y-%m-%d'))
    end_date = time.mktime(time.strptime('1995-12-30', '%Y-%m-%d'))
    random_birth_date = time.strftime('%Y-%m-%d', time.localtime(random.uniform(start_date, end_date)))
    return random_birth_date

def _random_name():
    names = {
        'first': ['Nguyễn', 'Lê', 'Bùi', 'Mã', 'Ngọc', 'Dương'],
        'last': ['Văn', 'Thị', 'An', 'Hoàng', 'Thanh', 'Yến'],
        'mid': ['Phong', 'Lan', 'Dương', 'Ngọc', 'Đạt', 'Nhi']
    }
    _first_name = random.choice(names['first'])
    _last_name = random.choice(names['last'])
    _mid_name = random.choice(names['mid'])
    _full_name = f"{_first_name} {_mid_name} {_last_name}"
    return _full_name

def _password():
    return f'MKFB{random.randint(0, 9999999)}@@@@'

def _email():
    user = ["a","b","c","d","e","f","g","h","u","i","o","y","m","n","l","h","q","x","s","k","p","t","w","v","j","z"]
    mail = ""
    for i in range(4):
        num = str(random.randint(1,100))
        mail += random.choice(user)
        mail += num
    domain = requests.get("https://api.mail.tm/domains?page=1", headers={"content-type":"application/json"}).json()["hydra:member"][0]["domain"]
    mail += "@"+domain
    mk = "MKMail123"
    data = '{"address":"'+mail+'","password":"MKMail123"}'
    acc = requests.post("https://api.mail.tm/accounts", data, headers={"content-type":"application/json"}).json()
    token = requests.post("https://api.mail.tm/token", data, headers={"content-type":"application/json"}).json()["token"]
    return mail

def _gender():
    return 'M' if random.randint(0, 10) > 5 else 'F'

def _reg_instance():
    md5_time = hashlib.md5(str(time.time()).encode()).hexdigest()
    reg_instance = f"{md5_time[:8]}-{md5_time[8:12]}-{md5_time[12:16]}-{md5_time[16:20]}-{md5_time[20:]}"
    return reg_instance

def _request(app_key, secret_key, gender, email_rand, password, reg_instance, name):

    req = {
        'api_key': app_key,
        'attempt_login': True,
        'birthday': _random_birthday(),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': name.split()[0],
        'format': 'json',
        'gender': gender,
        'lastname': name.split()[-1],
        'email': email_rand,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': reg_instance,
        'return_multiple_errors': True 
    }
    return req

def calculate_signature(req, secret_key):
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join([f'{k}={v}' for k, v in sorted_req])
    return hashlib.md5((sig + secret_key).encode()).hexdigest()

def make_request(api_url, req, secret_key, proxy=None):

    req['sig'] = calculate_signature(req, secret_key)
    response = requests.post(api_url, data=req, proxies=proxy)
    return json.loads(response.text)

def register_facebook_account(proxy=None):
    app = {
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'secret': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    
    for i in range(99999):
        name = _random_name()
        email_rand = _email()
        gender = _gender()
        password = _password()
        reg_instance = _reg_instance()

        req = _request(app['api_key'], app['secret'], gender, email_rand, password, reg_instance, name)
        reg = make_request('https://b-api.facebook.com/method/user.register', req, app['secret'], proxy)
        regg = json.dumps(reg)
        reg_dict = json.loads(regg)
        print(reg_dict)
        if reg_dict['error_code'] != 368:
            if 'attempt_login' in req:
                with open('reglogs.log', 'a+') as fp:
                    print(f"{email_rand}|MKMail123|{password}\n")
                    fp.write(f"{email_rand}|MKMail123|{password}\n")
                if 'error_code' not in reg_dict:
                    with open('reglogs.log', 'a+') as fp:
                        print(f"{email_rand}|MKMail123|{password}|{reg_dict['session_info']['access_token']}\n")
                        fp.write(f"{email_rand}|MKMail123|{password}|{reg_dict['session_info']['access_token']}\n")

    print(json.dumps(reg))

if __name__ == "__main__":
    prx = None
    
    if prx != None:
        proxy = prx.split(":")
        if len(proxy) == 2:
            ip = proxy[0]
            po = proxy[1]
            ghep = f"http://{ip}:{po}"
        elif len(proxy) == 4:
            ip = proxy[0]
            po = proxy[1]
            us = proxy[2]
            pa = proxy[3]
            ghep = f"http://{us}:{pa}@{ip}:{po}"
        else:
            pass
        proxies = {
			"https": ghep
		}
    else:
        proxies = {}
    register_facebook_account(proxies)
