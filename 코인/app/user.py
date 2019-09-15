import requests
import json
from bs4 import BeautifulSoup
import threading


def price():
    url = "https://api.bithumb.com/public/ticker/all"
    req = requests.get(url).content 
    data = json.loads(req)
    # print(data)
    # print(data.keys(),'\n')    
    
    try:
        for i in data['data']:
            print(i+"의 종가는 "+data['data'][i]["closing_price"]+"원 입니다.")
    
    except:
        pass
    

    

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(price, 3)

