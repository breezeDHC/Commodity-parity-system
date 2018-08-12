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
          
import sqlite3
#保存解析后的信息
class database(object):
    def __init__(self):
        self.path = './info.db'
        self.conn = sqlite3.connect(self.path)

    def saveInfo(self, lst, goods, website):
        table_n = ''
        if website == 'tb':
            table_n = 'tb_'+goods
        if website == 'jd':
            table_n = 'jd_'+goods
        if website == 'am':
            table_n = 'tm_'+goods
        try:
            self.conn.execute('''CREATE TABLE '%s'
                        (ID INT PRIMARY KEY NOT NULL,
                        PRICE REAL NOT NULL,
                        NAME TEXT NOT NULL);''' % (table_n))
            for i in range(len(lst)):
                self.conn.execute('INSERT INTO "%s" (ID,PRICE,NAME) VALUES("%d","%d","%s")' % (table_n,(i+1),float(lst[i][0]),lst[i][1]))
        except:
            print('数据存储错误')
        self.conn.commit()
    #读取信息
    def readInfo(self, lst,goods, website):
        table_n = ''
        if website == 'tb':
            table_n = 'tb_'+goods
        if website == 'jd':
            table_n = 'jd_'+goods
        if website == 'am':
            table_n = 'tm_'+goods
        try:
            cur = self.conn.execute('SELECT PRICE,NAME FROM "%s"' % (table_n))
            for x in cur:
                lst.append([x[0],x[1]])
        except:
            pass
    def closeConn(self):
        self.conn.close()
if __name__ == '__main__':
    d = database()
    ll = [['12','fd'],['65','hg']]
    llo = []
    d.saveInfo(ll,'r','jd')
    d.readInfo(llo,'r','jd')
    print(llo)
