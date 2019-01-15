"""
 模仿登陆cookie
"""
import json
from http import cookiejar
from urllib import request

if __name__ == '__main__':
    #登陆地址
    login_url = 'http://154.8.153.163/api/v1.0/login'
    #user-agent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    header = {'User-Agent':user_agent,'Content-Type':'application/json'}
    #登陆信息
    login_form = {'account':'admin','passwd':'123456'}
    login_json = bytes(json.dumps(login_form), 'utf-8')
    #cookie
    cookie = cookiejar.CookieJar()
    cookie_support = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_support)
    req1 = request.Request(url=login_url, data=login_json, headers=header)

    #列表地址
    data_url = 'http://154.8.153.163/api/v1.0/report_infos?pageNum=1&pageSize=10'
    req2=request.Request(url=data_url,headers={'User-Agent':user_agent})
    rep1 = opener.open(req1)
    print(rep1.read().decode('utf-8'))
    rep2 = opener.open(req2)
    json = rep2.read().decode('utf-8')
    print(json)
