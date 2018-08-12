#########################################################################
	#File Name: gui.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年04月17日 星期二 09时24分55秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
          
from tkinter import *
from tkinter import messagebox
import crawl
import database

class gui(Frame):

    def __init__(self,master=None):
        #爬取参数变量
        self.webvar1 = IntVar()
        self.webvar2 = IntVar()
        self.webvar3 = IntVar()
        self.webvar4 = IntVar()
        self.dp_var = IntVar()
        self.goods_var = StringVar()
        #数据显示参数变量
        self.g_var = StringVar()
        self.min_var = IntVar()
        self.max_var = IntVar()
        self.sort_var = IntVar()
        self.tb_text = Text()
        self.am_text = Text()
        self.jd_text = Text()
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
 
    def crawler(self):
        web_tb = self.webvar1.get()
        web_jd = self.webvar2.get()
        web_am = self.webvar3.get()
        web_all = self.webvar4.get()
        depth = self.dp_var.get()
        goods = self.goods_var.get()
        cr = crawl.crawl()
        if web_all == 1:
            cr.crawler_all(depth,goods)
            messagebox.showinfo(title='result',message='全部爬取完成')
        else:
            if web_jd == 1:
                cr.crawler_jd(depth,goods)
                messagebox.showinfo(title='result',message='jd爬取完成')
            if web_tb == 1:
                cr.crawler_tb(depth,goods)
                messagebox.showinfo(title='result',message='tb爬取完成')
            if web_am == 1: 
                cr.crawler_am(depth,goods)
                messagebox.showinfo(title='result',message='TMALL爬取完成')
    #排序和范围选择
    def show_sub1(self,lst,sort,min_v,max_v):
        if sort == 1:
            lst = sorted(lst, key=lambda x:x[0])
        if max_v != 0:
            lst_tem = lst
            lst = []
            for i in range(len(lst_tem)):
                if (lst_tem[i][0] >= min_v) and (lst_tem[i][0] <= max_v):
                    lst.append(lst_tem[i])
        return lst

    #显示处理完的数据 
    def show_sub2(self,lst,web):
        if len(lst) != 0:
            tem_str = '序号\t价格\t\t\t标题\n'
            count = 0
            if web == 'tb':
                self.tb_text.insert('end',tem_str)
            if web == 'tm':
                self.am_text.insert('end',tem_str)
            if web == 'jd':
                self.jd_text.insert('end',tem_str)
            for i in range(len(lst)):
                count = count + 1
                if web == 'tb':
                    self.tb_text.insert('end',str(count)+'\t')
                    self.tb_text.insert('end',str(lst[i][0])+'\t')
                    self.tb_text.insert('end',str(lst[i][1][:17])+'\n')
                if web == 'tm':
                    self.am_text.insert('end',str(count)+'\t')
                    self.am_text.insert('end',str(lst[i][0])+'\t')
                    self.am_text.insert('end',str(lst[i][1][:17])+'\n')
                if web == 'jd':
                    self.jd_text.insert('end',str(count)+'\t')
                    self.jd_text.insert('end',str(lst[i][0])+'\t')
                    self.jd_text.insert('end',str(lst[i][1][:17])+'\n')
    def showdata(self):
        #变量定义
        goods = self.g_var.get()
        min_v = self.min_var.get()
        max_v = self.max_var.get()
        sort = self.sort_var.get()
        lst_tb = []
        lst_jd = []
        lst_tm = []
        d = database.database()
        
        #淘宝数据显示
        self.tb_text.delete(0.0,'end')
        d.readInfo(lst_tb,goods,'tb')
        lst_tb = self.show_sub1(lst_tb,sort,min_v,max_v)
        self.show_sub2(lst_tb,'tb')

        #天猫数据显示
        self.am_text.delete(0.0,'end')
        d.readInfo(lst_tm,goods,'am')
        lst_tm = self.show_sub1(lst_tm,sort,min_v,max_v)
        self.show_sub2(lst_tm,'tm')

        #京东数据显示
        self.jd_text.delete(0.0,'end')
        d.readInfo(lst_jd,goods,'jd')
        lst_jd = self.show_sub1(lst_jd,sort,min_v,max_v)
        self.show_sub2(lst_jd,'jd')

        d.closeConn()
    def createWidgets(self):
        #爬取参数部分框架划分
        self.ft = Frame(self)
        self.ft.pack(side='top',pady=20,padx=30,fill='both')
        self.f1 = Frame(self.ft)
        self.f1.pack(side='top',anchor='ne',pady=10,fill='both')
        self.f2 = Frame(self.ft,bg='red')
        self.f2.pack(side='top',fill='both')
        self.f11 = Frame(self.f1)
        self.f11.pack(side='left',anchor='ne',fill='both')
        self.f12 = Frame(self.f1)
        self.f12.pack(side='left',anchor='ne',padx=20,fill='both')
        self.f13 = Frame(self.f1)
        self.f13.pack(side='left',anchor='ne',fill='both')
        self.f14 = Frame(self.f1)
        self.f14.pack(side='left',anchor='ne',padx=20,fill='both')
        #数据显示部分框架划分
        self.fb = Frame(self)
        self.fb.pack(side='top',anchor='nw',padx=30)
        #第一行
        self.fb1 = Frame(self.fb)
        self.fb1.pack(side='top',fill='both')
        self.fb11 = Frame(self.fb1)
        self.fb11.pack(side='left')
        self.fb12 = Frame(self.fb1)
        self.fb12.pack(side='left',padx=20)
        self.fb13 = Frame(self.fb1)
        self.fb13.pack(side='left')
        self.fb14 = Frame(self.fb1)
        self.fb14.pack(side='left',padx=20)
        #第二行
        self.fb2 = Frame(self.fb)
        self.fb2.pack(side='top',fill='both',pady=20)
        #第三行
        self.fb3 = Frame(self.fb)
        self.fb3.pack(side='top',fill='both')

        #爬取参数选择
        #网站选择
        Label(self.f11,text='Website:').pack(side='left',padx=0)
        Checkbutton(self.f11,text='Taobao',variable=self.webvar1,onvalue=1,offvalue=0).pack(side='left')
        Checkbutton(self.f11,text='JingDong',variable=self.webvar2,onvalue=1,offvalue=0).pack(side='left')
        Checkbutton(self.f11,text='TMALL',variable=self.webvar3,onvalue=1,offvalue=0).pack(side='left')
        Checkbutton(self.f11,text='ALL',variable=self.webvar4,onvalue=1,offvalue=0).pack(side='left')
        #页面数选择
        Label(self.f12,text='Page:').pack(side='left',padx=10)
        Entry(self.f12,textvariable=self.dp_var,width=5).pack(side='left')
        #商品选择
        Label(self.f13,text='goods:').pack(side='left',padx=10)
        Entry(self.f13,textvariable=self.goods_var,width=10).pack(side='left')

        #确认
        Button(self.f14,text='submit',command=self.crawler).pack(side='left',padx=20)
        #划线
        Canvas(self.f2,bg='white',width=1093,height=3).pack(side='top')

        #数据显示参数选择部分
        #商品选择
        Label(self.fb11,text='goods:').pack(side='left')
        Entry(self.fb11,textvariable=self.g_var,width=5).pack(side='left')
        #价格范围选择
        Label(self.fb12,text='Range:').pack(side='left')
        Entry(self.fb12,width=5,textvariable=self.min_var).pack(side='left',padx=10)
        Entry(self.fb12,width=5,textvariable=self.max_var).pack(side='left')
        #排序
        Checkbutton(self.fb13,text='Sort',variable=self.sort_var,onvalue=1,offvalue=0).pack(side='left')
        #确认
        Button(self.fb14,text='confirm',command=self.showdata).pack(side='left')

        #网站名
        Label(self.fb2,text='Taobao').pack(side='left',padx=150)
        Label(self.fb2,text='TMALL').pack(side='left',padx=170)
        Label(self.fb2,text='JingDong').pack(side='left',padx=150)

        #数据显示框
        self.tb_text = Text(self.fb3,width=50,height=30)
        self.tb_text.pack(side='left')
        self.am_text = Text(self.fb3,width=50,height=30)
        self.am_text.pack(side='left',padx=10)
        self.jd_text = Text(self.fb3,width=50,height=30)
        self.jd_text.pack(side='left')

if __name__ == '__main__':
    window = Tk()
    window.title('商品比价')
    window.geometry('1150x700')
    g = gui(master=window)
    g.mainloop()
