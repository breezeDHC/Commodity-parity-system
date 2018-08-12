       
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
	    print("获取html失败")

def parserHtml(lst, html):
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find_all('div', 'p-price')
    name = soup.find_all('div', 'p-name')
    for i in range(len(price)):
        lst.append([(float)(price[i].i.string),name[i].a.attrs['title']])

def saveInfo(lst):
    with open('./jd.html','w') as f:
        f.write('<html><head><meta charset="utf-8"></head>')
        f.write('<body><table><tbody><tr><td>序号</td><td>价格</td><td>标题</td></tr>')
        count = 1
        for x in range(len(lst)):
            f.write('<tr><td>')
            f.write((str)(count))
            f.write('</td><td>')
            f.write((str)(lst[x][0]))
            f.write('</td><td>')
            f.write(str(lst[x][1]))
            f.write('</td></tr>')
            count = count + 1
        f.write('</tbody></table></body></html>')
def sortedAndChoice(lst, ifsort, min, max):
    if ifsort == 'yes':
        lst = sorted(lst,key=lambda x:x[0])
    if max != -1:
        ll = lst
        lst = []
        for i in range(len(ll)):
            if ll[i][0] >= float(min) and ll[i][0] <= float(max):
                lst.append(ll[i])
    return lst	

def main():
    goods = input('请输入货物')
    depth = int(input('请输入爬去页面深度'))
    ifsort = input('是否排序')
    ifchoice = input('是否价格筛选')
    min = max = -1
    if ifchoice == 'yes':
        min = input('输入最小值')
        max = input('输入最大值')
    lst = []
    url_start = 'https://search.jd.com/Search?keyword='+goods+'&enc=utf8&page='
    for i in range(depth):
        url_each = url_start + (str)(i*2+1)
        html = getHTMLText(url_each)
        parserHtml(lst, html)
    lst = sortedAndChoice(lst,ifsort,min,max)
    saveInfo(lst)

main()
