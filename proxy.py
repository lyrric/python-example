#!/usr/bin/python
#coding=utf-8
"""
    代理的运用
"""

from urllib import request
from urllib import parse

if __name__ == '__main__':
    url = 'https://www.ip.cn/'
    proxy = {'https':'119.101.117.39:9999'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
    request.install_opener(opener)
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        #my_request = request.Request(url, headers=headers)
        #response = request.urlopen(my_request)
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        print(html)
    except Exception as e:
        print("ops-")
        print(e)

