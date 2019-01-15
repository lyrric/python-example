"""
    获取豆瓣top250
"""
from urllib import request
from bs4 import BeautifulSoup

original_url = 'https://movie.douban.com/top250'
temp_url = 'https://movie.douban.com/top250?start='
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
start = 0
count = 0
while True:
    req = request.Request(url=(temp_url+str(start)), headers=header)
    rep = request.urlopen(req)
    html = rep.read().decode('UTF-8')
    soup = BeautifulSoup(html, 'html.parser')
    titles = BeautifulSoup.find_all(soup,name='div', attrs={'class':'hd'})
    if len(titles) == 0:
        break
    for x in iter(titles):
        count+=1
        name = x.contents[1].contents[1].contents[0]
        print(name)
    start+=25
    print("已遍历发现影片",count)