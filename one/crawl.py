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
from database import *
class crawl(object):
    def getHTMLText(self,url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print('获取HTML失败')

    def parser_tb(self, html):
        lst_tb = []
        try:
            price = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
            title = re.findall(r'\"raw_title\"\:\".*?\"',html)
            for i in range(len(price)):
                price_ = eval(price[i].split(':')[1])
                title_ = eval(title[i].split(':')[1])
                lst_tb.append([price_,title_])
        except:
            print('tb数据提取失败')
        return lst_tb

    def parser_jd(self, html):
        lst_jd = []
        try:
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find_all('div', 'p-price')
            name = soup.find_all('div', 'p-name')
            for i in range(len(price)):
                lst_jd.append([(float)(price[i].i.string),name[i].a.attrs['title']])
        except:
            print('jd数据提取失败')
        return lst_jd

    def parser_am(self, html):
        lst_am = []
        try:
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find_all('p','productPrice')
            name = soup.find_all('p','productTitle')
            for i in range(len(price)):
                lst_am.append([float(price[i].em.attrs['title']),name[i].a.attrs['title']])
        except:
            print('TMALL数据提取失败')
        return lst_am

    def crawler_all(self,depth, goods):
        self.crawler_am(depth,goods)
        self.crawler_tb(depth,goods)
        self.crawler_jd(depth,goods)

    def saveInfo(self,lst,goods,web):
        d = databse.database()
        d.saveInfo(lst,goods,web)

    def crawler_am(self,depth, goods):
        url_start = 'https://list.tmall.com/search_product.htm?q='+goods
        for i in range(depth):
            try:
                url_each = url_start +'&s='+str((i-1)*60)
                html = self.getHTMLText(url_each)
                lst_am = self.parser_am(html)
                d = database()
                d.saveInfo(lst_am,goods,'am')
                d.closeConn()
            except:
                print('TMALL出现异常')
    def crawler_tb(self,depth, goods):
        url_start = 'https://s.taobao.com/search?q=' + goods
        for i in range(depth):
            try:
                url_each = url_start + '&s=' + str(44*i)
                html = self.getHTMLText(url_each)
                lst_tb = self.parser_tb(html)
                d = database()
                d.saveInfo(lst_tb,goods,'tb')
                d.closeConn()
            except:
                print('tb出现异常') 
    def crawler_jd(self,depth, goods):
        url_start = 'https://search.jd.com/Search?keyword='+goods+'&enc=utf8&page='
        for i in range(depth):
            try:
                url_each = url_start + str(i*2+1)
                html = self.getHTMLText(url_each)
                lst_jd = self.parser_jd(html)
                d = database()
                d.saveInfo(lst_jd,goods,'jd')
                d.closeConn()
            except:
                print('jd出现异常')
