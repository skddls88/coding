import requests
import pymysql
from bs4 import BeautifulSoup

url = 'https://pann.nate.com/today'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")

best_talk_list = []
normal_talk_list = []

best_talk = soup.select(".pick_area .title a")
best_talk_list.append("https://pann.nate.com"+best_talk[0].get('href'))

today_talk = soup.select(".bridge_talk .talk-list li") #일반 오늘의톡

for item in today_talk:
    for item2 in item.select("a"):
        if "search" in item2.get('href'):
            pass
        
        elif "channel" in item2.get("href"):
            pass
        
        else:
            normal_talk_list.append("https://pann.nate.com"+item2.get('href'))

for item in normal_talk_list:
    req = requests.get(item)
    soup = BeautifulSoup(req.text,"html.parser")
    
    
    article_title = soup.select(".post-tit-info h4")[0].text
    article_desc = soup.select("#contentArea")[0]
    article_up = soup.select(".updown .up .count")[0].text
    article_down = soup.select(".updown .down .count")[0].text
    
    db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='1111',
                     db='nate',
                     charset='utf8')
    try:
        cursor = db.cursor()
        sql = "INSERT INTO article_board (article_title, article_des, like_up, like_down) VALUES ('{title}','{desc}', {up}, {down});".format(title=article_title, desc=article_desc, up=article_up, down=article_down )
        cursor.execute(sql)
        db.commit()
    except:
        pass
    
    finally:
        db.close()

