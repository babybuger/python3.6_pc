import urllib.request
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url='http://tyjs.zwu.edu.cn/tyjs/Student/Club_Score/CWork_m.asp'

    ids=input("输入学号:")
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Cookie':'ASPSESSIONIDAABBQRQQ=JLEHFMBBLJLJINHJPFOHAMBD; Hm_lvt_62f9faa91e1a0697eed2f444c79424b0=1508240537,1510148183; '\
                 'Hm_lpvt_62f9faa91e1a0697eed2f444c79424b0=1510148183; cent%5Fcode='+ids+'; Student%5Fdown=Y; '\
                 'Student%5Fid='+ids+'; Student%5Fnm='+ids
        }
    req=urllib.request.Request(url=url,headers=head)
    rep=urllib.request.urlopen(req)

    html=rep.read().decode('gbk','ignore')

    soup=BeautifulSoup(html,"html.parser")
    soup=soup.find_all("td", bgcolor="#FFFFFF", height="35")
    for tag in soup:
        print(tag.text)#去标签

