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
          
import tkinter as tk
import tkinter.messagebox
import crawl
import re
import os
import database

window = tk.Tk()
window.title('商品比价')
window.geometry('1150x700')

def crawler():
    web_tb = web_var1.get()
    web_jd = web_var2.get()
    web_am = web_var3.get()
    web_all = web_var4.get()
    depth = dp_var.get()
    goods = goods_var.get()
    if web_all == 1:
        crawl.crawler_all(depth,goods)
        tk.messagebox.showinfo(title='result',message='全部爬取完成')
    else:
        if web_jd == 1:
            crawl.crawler_jd(depth,goods)
            tk.messagebox.showinfo(title='result',message='jd爬取完成')
        if web_tb == 1:
            crawl.crawler_tb(depth,goods)
            tk.messagebox.showinfo(title='result',message='tb爬取完成')
        if web_am == 1: 
            crawl.crawler_am(depth,goods)
            tk.messagebox.showinfo(title='result',message='TMALL爬取完成')
    
#框架划分
frm_t = tk.Frame(window,width=1000,height=300).pack()
frm_b = tk.Frame(window,width=1000,height=600).pack()
frm_b_t = tk.Frame(frm_b,width=1000,height=100).pack()
frm_b_b = tk.Frame(frm_b,width=1000,height=500).pack()

#爬取参数选择部分
#网站选择
tk.Label(frm_t,text='Website:').place(x=30,y=30)
web_var1 = tk.IntVar()
c1 = tk.Checkbutton(frm_t,text='Taobao',variable=web_var1,onvalue=1,offvalue=0)
c1.place(x=90,y=30)
web_var2 = tk.IntVar()
c2 = tk.Checkbutton(frm_t,text='Jingdong',variable=web_var2,onvalue=1,offvalue=0)
c2.place(x=170,y=30)
web_var3 = tk.IntVar()
c3 = tk.Checkbutton(frm_t,text='TMALL',variable=web_var3,onvalue=1,offvalue=0)
c3.place(x=260,y=30)
web_var4 = tk.IntVar()
c4 = tk.Checkbutton(frm_t,text='All',variable=web_var4,onvalue=1,offvalue=0)
c4.place(x=340,y=30)

#页面数选择
tk.Label(frm_t,text='depth:').place(x=420,y=30)
dp_var = tk.IntVar()
dp_en = tk.Entry(frm_t,textvariable=dp_var,width=3)
dp_en.place(x=470,y=30)

#商品选择
tk.Label(frm_t,text='goods:').place(x=530,y=30)
goods_var = tk.StringVar()
goods_en = tk.Entry(frm_t,textvariable=goods_var,width=10)
goods_en.place(x=580,y=30)

#确认
comfirm1 = tk.Button(frm_t,text='submit',command=crawler)
comfirm1.place(x=680,y=25)

#划线
canvas = tk.Canvas(frm_t,bg='white',width=1093,height=3)
canvas.place(x=30,y=65)


#数据显示参数选择部分
#商品选择
tk.Label(frm_b_t,text='goods:').place(x=30,y=90)
g_var = tk.StringVar()
g_en = tk.Entry(frm_b_t,textvariable=g_var,width=5)
g_en.place(x=80,y=90)
#价格范围选择
tk.Label(frm_b_t,text='Range:').place(x=130,y=90)
min_var = tk.IntVar()
min_en = tk.Entry(frm_b_t,width=5,textvariable=min_var)
min_en.place(x=180,y=90)
max_var = tk.IntVar()
max_en = tk.Entry(frm_b_t,width=5,textvariable=max_var)
max_en.place(x=230,y=90)
#排序
sort_var = tk.IntVar()
ch1 = tk.Checkbutton(frm_b_t,text='Sort',variable=sort_var,onvalue=1,offvalue=0)
ch1.place(x=280,y=90)

#数据保存以文件的方法时显示数据
#def show_sub1(path,sort,min_v,max_v):
#    with open(path,'r') as f:
#        pri = []
#        nam = []
#        ll = []
#        str_read = f.read()
#        lst = re.findall(r'<td>.*?</td>',str_read)[3:]
#        for i in range(len(lst)):
#            if i%3 == 1:
#                ll.append([float(lst[i][4:-5]),lst[i+1][4:-5]])
#        if sort == 1:
#            ll = sorted(ll,key=lambda x:x[0])
#        if max_v != 0:
#            li = ll
#            ll = []
#            for i in range(len(li)):
#                if (li[i][0] >= min_v) and (li[i][0] <= max_v):
#                    ll.append(li[i])
#        return ll
#
#显示数据
#def showdata():
#    goods = g_var.get()
#    min_v = min_var.get()
#    max_v = max_var.get()
#    sort = sort_var.get()
#    #淘宝数据显示
#    tb_text.delete(0.0,'end')
#    path_tb = './tb_'+goods+'.html'
#    if os.path.exists(path_tb):
#        lst_tb = show_sub1(path_tb,sort,min_v,max_v)
#        show_sub2(lst_tb,'tb')
#    else:
#        tk.messagebox.showinfo('error','tb商品'+goods+'信息不存在')
#    #天猫数据显示 
#    am_text.delete(0.0,'end')
#    path_tm = './tmall_'+goods+'.html'
#    if os.path.exists(path_tm):
#        lst_tm = show_sub1(path_tm,sort,min_v,max_v)
#        show_sub2(lst_tm,'tm')
#    else:
#        tk.messagebox.showinfo('error','tm商品'+goods+'信息不存在')
#    #京东数据显示
#    jd_text.delete(0.0,'end')
#    path_jd = './jd_'+goods+'.html'
#    if os.path.exists(path_jd):
#        lst_jd = show_sub1(path_jd,sort,min_v,max_v)
#        show_sub2(lst_jd,'jd')
#    else:
#        tk.messagebox.showinfo('error','jd商品'+goods+'信息不存在')


#排序和范围选择
def show_sub1(lst,sort,min_v,max_v):
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
def show_sub2(lst,web):
    tem_str = '序号\t价格\t\t\t标题\n'
    count = 0
    if web == 'tb':
        tb_text.insert('end',tem_str)
    if web == 'tm':
        am_text.insert('end',tem_str)
    if web == 'jd':
        jd_text.insert('end',tem_str)
    for i in range(len(lst)):
        count = count + 1
        if web == 'tb':
            tb_text.insert('end',str(count)+'\t')
            tb_text.insert('end',str(lst[i][0])+'\t')
            tb_text.insert('end',str(lst[i][1][:19])+'\n')
        if web == 'tm':
            am_text.insert('end',str(count)+'\t')
            am_text.insert('end',str(lst[i][0])+'\t')
            am_text.insert('end',str(lst[i][1][:19])+'\n')
        if web == 'jd':
            jd_text.insert('end',str(count)+'\t')
            jd_text.insert('end',str(lst[i][0])+'\t')
            jd_text.insert('end',str(lst[i][1][:19])+'\n')
def showdata():
    goods = g_var.get()
    min_v = min_var.get()
    max_v = max_var.get()
    sort = sort_var.get()
    lst_tb = []
    lst_jd = []
    lst_tm = []
    #淘宝数据显示
    #show_tb(goods,min_v,max_v,sort)
    tb_text.delete(0.0,'end')
    database.readInfo(lst_tb,goods,'tb')
    lst_tb = show_sub1(lst_tb,sort,min_v,max_v)
    show_sub2(lst_tb,'tb')
    #天猫数据显示
    #show_tm(goods,min_v,max_v,sort)
    am_text.delete(0.0,'end')
    database.readInfo(lst_tm,goods,'am')
    lst_tm = show_sub1(lst_tm,sort,min_v,max_v)
    show_sub2(lst_tm,'tm')
    #京东数据显示
    #show_jd(goods,min_v,max_v,sort)
    jd_text.delete(0.0,'end')
    database.readInfo(lst_jd,goods,'jd')
    lst_jd = show_sub1(lst_jd,sort,min_v,max_v)
    show_sub2(lst_jd,'jd')

confirm2 = tk.Button(frm_b_t,text='confirm',command=showdata)
confirm2.place(x=350,y=85)

#数据显示部分
#网站名
tk.Label(frm_b_b,text='Taobao').place(x=180,y=130)
tk.Label(frm_b_b,text='Jingdong').place(x=540,y=130)
tk.Label(frm_b_b,text='TMALL').place(x=930,y=130)
#滚动条
#s1 = tk.Scrollbar(frm_b_b)
#s2 = tk.Scrollbar(frm_b_b)
#s3 = tk.Scrollbar(frm_b_b)
#文本框
tb_text = tk.Text(frm_b_b,width=50,height=30)
tb_text.place(x=30,y=165)
jd_text = tk.Text(frm_b_b,width=50,height=30)
jd_text.place(x=400,y=165)
am_text = tk.Text(frm_b_b,width=50,height=30)
am_text.place(x=770,y=165)

window.mainloop()

if __name__ == '__main__':
    lst = [[1,'444'],[234,'sdf'],[45,'cvv'],[23,'ssd']]
    show_sub1(lst,1,0,100)
    print(lst)


