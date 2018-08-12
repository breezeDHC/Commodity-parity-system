#########################################################################
	#File Name: database.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年04月18日 星期三 10时37分27秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
          
import tkinter as tk
import sqlite3
#保存解析后的信息
def saveInfo(lst, goods,website):
    table_n = ''
    conn = sqlite3.connect('savedinfo.db')
    if website == 'tb':
        table_n = 'tb_'+goods
    if website == 'jd':
        table_n = 'jd_'+goods
    if website == 'am':
        table_n = 'tm_'+goods
    try:
        conn.execute('''CREATE TABLE '%s'
                        (ID INT PRIMARY KEY NOT NULL,
                        PRICE REAL NOT NULL,
                        NAME TEXT NOT NULL);''' % (table_n))
        for i in range(len(lst)):
            conn.execute('INSERT INTO "%s" (ID,PRICE,NAME) VALUES("%d","%d","%s")' % (table_n,(i+1),float(lst[i][0]),lst[i][1]))
    except:
        pass
    conn.commit()
    conn.close()
#读取信息
def readInfo(lst,goods,website):
    table_n = ''
    if website == 'tb':
        table_n = 'tb_'+goods
    if website == 'jd':
        table_n = 'jd_'+goods
    if website == 'am':
        table_n = 'tm_'+goods
    conn = sqlite3.connect('savedinfo.db')
    try:
        cur = conn.execute('SELECT PRICE,NAME FROM "%s"' % (table_n))
        for x in cur:
            lst.append([x[0],x[1]])
    except:
        pass
    conn.close()
    return lst
#test
if __name__ == '__main__':
    lst_tb = [[15,'232'],[24,'sds']]
    ll_tb = []
    lst_tm = [[17,'2s32'],[20,'sdffs']]
    ll_tm = []
    lst_jd = [[18,'23bb2'],[29,'sdaas']]
    ll_jd = []
    saveInfo(lst_tb,'书包','tb')
    saveInfo(lst_tm,'书包','am')
    saveInfo(lst_jd,'书包','jd')
    readInfo(ll_tm,'书包','am')
    readInfo(ll_tb,'书包','tb')
    readInfo(ll_jd,'书包','jd')
    print(ll_tm)
    print(ll_tb)
    print(ll_jd)
