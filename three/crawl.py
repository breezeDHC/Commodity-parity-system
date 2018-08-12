#########################################################################
	#File Name: crawl.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年04月17日 星期二 13时09分20秒
#########################################################################
           
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
        print('获取HTML失败')

def parser_tb(lst_tb, html):
    try:
        price = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        title = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(price)):
            price_ = eval(price[i].split(':')[1])
            title_ = eval(title[i].split(':')[1])
            lst_tb.append([price_,title_])
    except:
        print('tb数据提取失败')

def parser_jd(lst_jd, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find_all('div', 'p-price')
        name = soup.find_all('div', 'p-name')
        for i in range(len(price)):
            lst_jd.append([(float)(price[i].i.string),name[i].a.attrs['title']])
    except:
        print('jd数据提取失败')

def parser_am(lst_am, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find_all('p','productPrice')
        name = soup.find_all('p','productTitle')
        for i in range(len(price)):
            lst_am.append([float(price[i].em.attrs['title']),name[i].a.attrs['title']])
    except:
        print('TMALL数据提取失败')
def saveInfo(lst, goods,website):
    if website == 'jd':
        path = './jd_'+goods+'.html'
    if website == 'tb':
        path = './tb_'+goods+'.html'
    if website == 'am':
        path = './tmall_'+goods+'.html'
    with open(path,'w') as f:
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

def crawler_all(depth, goods):
    crawler_am(depth,goods)
    crawler_tb(depth,goods)
    crawler_jd(depth,goods)

def crawler_am(depth, goods):
    lst_am = []
    url_start = 'https://list.tmall.com/search_product.htm?q='+goods
    for i in range(depth):
        try:
            url_each = url_start +'&s='+str((i-1)*60)
            html = getHTMLText(url_each)
            parser_am(lst_am,html)
        except:
            print('TMALL出现异常')
    saveInfo(lst_am,goods,'am')
def crawler_tb(depth, goods):
    lst_tb = []
    url_start = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        try:
            url_each = url_start + '&s=' + str(44*i)
            html = getHTMLText(url_each)
            parser_tb(lst_tb,html)
        except:
            print('出现异常') 
    saveInfo(lst_tb, goods,'tb')

def crawler_jd(depth, goods):
    lst_jd = []
    url_start = 'https://search.jd.com/Search?keyword='+goods+'&enc=utf8&page='
    for i in range(depth):
        try:
            url_each = url_start + str(i*2+1)
            html = getHTMLText(url_each)
            parser_jd(lst_jd, html)
        except:
            continue
    saveInfo(lst_jd, goods,'jd')
