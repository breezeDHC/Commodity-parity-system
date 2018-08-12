#########################################################################
	#File Name: main.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年05月07日 星期一 12时45分31秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
          
import gui
from tkinter import *

window = Tk()
window.title('商品比价系统')
window.geometry('1150x700')
g = gui.gui(master=window)
g.mainloop()

