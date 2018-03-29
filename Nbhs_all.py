import requests
import urllib.request
import re
import _mysql_exceptions
from bs4 import BeautifulSoup

def geturl(url):
    url=url
    session=requests.Session
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    req=urllib.request.Request(url=url,headers=head)
    rep=urllib.request.urlopen(req)
    html=rep.read().decode('utf-8','ignore')
    soup=BeautifulSoup(html,'html.parser')
    return soup


def geturlhttp():
    soup=geturl('http://www.nbmsri.org.cn/')
    soupl = soup.find_all(style='overflow: hidden;padding: 1.2em;')
    for tag in soupl:
        tag=tag.find_all(href=re.compile("/sldt/"))
        arr = []
        for i in tag:
            arr.append('http://www.nbmsri.org.cn'+i.get('href'))
        return arr

a=geturlhttp()
j = 0
for i in a:
    j += 1
    print("打开文件")
    f = open('G:/test//test' + str(j) + '.txt', 'wb') #写入存储位置
    print("获取内容")
    b = geturl(i)
    l=b.find(class_ ="uinn06")
    l=l.text
    Str = l.encode('utf-8')  #从string转换成bytes类型
    print("写入")
    f.write(Str)
    print("关闭")
    f.close()
    # print(j)
