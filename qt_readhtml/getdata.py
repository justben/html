import urllib.request
from bs4 import BeautifulSoup
import os

def getdata(url):

    response = urllib.request.urlopen(url)

    html = response.read()

    html = html.decode("gb2312")

    soup = BeautifulSoup(html, 'html.parser')

    book = soup.prettify()

    data = book.split('\n')

    num = len(data)
    i = 0
    ii = 1

    s = []
    ss = []

    while i < num:
        if data[i] == ' GPS控制点WGS84坐标':
            while ii == 1:
                if data[i] ==  ' 采集数据':
                    ii = 0
                else:
                    if data[i] !=  ' 采集数据':
                        s.append(data[i])
                        i += 1
        else:
            i += 1

    i = 0
    num = len(s)

    while i < num:
        ii = 0
        n = len(s[i])
        while ii < n:
            if s[i][ii] != '<':
                flag = 0
                ii += 1
            else:
                flag = 1
                ii = n
        if flag == 0:
            ss.append(s[i].strip())
            i += 1
        else:
            i += 1

    d = [ss[11]+'\n',
         ss[13].replace('.','#')+' '+ss[14].replace('.','#')+' '+ss[15]+'\n',
         ss[20].replace('.','#')+' '+ss[21].replace('.','#')+' '+ss[22]+'\n',
         ss[24].replace('.','#')+' '+ss[25].replace('.','#')+' '+ss[26]+'\n',
         ss[28].replace('.','#')+' '+ss[29].replace('.','#')+' '+ss[30]+'\n',
         ss[16].replace('.','#')+' '+ss[17].replace('.','#')+' '+ss[18]+'\n']

    i = 0
    num = len(d)

    while i < num:
        d[i] = d[i].replace('°','.')
        d[i] = d[i].replace('′','')
        d[i] = d[i].replace('″','')
        d[i] = d[i].replace('#','')
        d[i] = d[i].replace(':','.',1)
        d[i] = d[i].replace(':','',1)
        d[i] = d[i].replace(':','.',1)
        d[i] = d[i].replace(':','',1)
        i += 1

    
    f_write = open('WGS84坐标.txt','a')
    for i in d:
        f_write.write(i)

    f_write.close()



