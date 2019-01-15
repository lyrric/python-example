from urllib import request
from bs4 import BeautifulSoup

"""
    获取btbtt的种子
"""
#http://www.btbtt.us/forum-index-fid-951-page-1.htm
url = 'http://www.btbtt.us/forum-index-fid-951-page-'
thread_prefix_url = 'http://www.btbtt.us/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
i = 1
temp_url = url+str(i)+'.htm'
req = request.Request(temp_url,headers=header)
rep = request.urlopen(req)
thread_list_html = rep.read().decode('utf-8')
soup = BeautifulSoup(thread_list_html, 'html.parser')
tables = BeautifulSoup.find_all(soup, name='a', attrs={'class':'subject_link thread-new'})
it = iter(tables)
#循环遍历每个帖子,获取附件名称和地址
for x in it:
    thread_url = x.attrs['href']
    req = request.Request(thread_prefix_url+thread_url,headers=header)
    thread_html = request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(thread_html,'html.parser')
    div = soup.find_all(name='div',attrs={'class':'attachlist'})
    attach = div[0].contents[1].contents[5].contents[1].contents[1]
    attach_href = attach.attrs['href']
    attach_href = attach_href.replace('dialog','download')
    attach_name = attach.text
    print("attach_name =",attach_name,',attach_href =',attach_href)

#http://www.btbtt.us/attach-download-fid-951-aid-4741003.htm

