# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:52:47 2020

@author: Administrator
"""
#filetype(百度)
from bs4 import BeautifulSoup
import requests
#界面代码部分
import tkinter as tk 
from tkinter import ttk
from tkinter import *

class App(Frame):
    def __init__(self):
        super().__init__()
        self.site = StringVar()
        self.leixing = StringVar()
        self.pack()
        self.cform()    
    def cform(self):
        ttk.Combobox(self, width = 19, values = (1,2,3), textvariable = self.leixing).grid(row = 0, column = 1, rowspan = 1)
        
        Label(self,text="请输入网站域名：", font=("微软雅黑", 15), fg='blue').grid(row = 1, column = 1, rowspan = 1)

#输入框
        Entry(self, borderwidth = 3, width=50, textvariable = self.site).grid(row = 1, column = 2, rowspan = 1)

#两个按钮
        Button(self, text = '搜索', font=("微软雅黑", 10), fg='green', command=self.search).grid(row = 1, column = 3, rowspan = 1)
        Button(self, text = '高级搜索', font=("微软雅黑", 10), fg='green').grid(row = 1, column = 4, rowspan = 1)
    def getf(self):
        self.file = self.filetype()
    
    def getu(self):
        self.url = self.inurl()
    
    def search(self):
        print(1111)
        print(self.leixing.get())
        url = self.inurl()
        ext = self.filetype()
        print(url)
        headers = {
       'Accept': '*/*',
       'is_xhr': '1',
       'X-Requested-With': 'XMLHttpRequest',
       'is_referer': 'https://www.baidu.com/',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
       #'Referer': 'https://www.baidu.com/s?wd=site%3Abjzhuoda.com&rsv_spt=1&rsv_iqid=0x98bc8069000c11d6&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&rsv_sug3=24&rsv_sug1=11&rsv_sug7=101&inputT=10603&rsv_sug4=11034',
       'Accept-Encoding': 'gzip, deflate',
       'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        chaxun = self.site.get()
        if self.leixing.get() == '1':
            chaxun = chaxun + " " + url
        else:
             chaxun = chaxun + " " + ext
             
        #百度独有的url
        url = "https://www.baidu.com/s?wd=site%3A" + chaxun  + "&ie=utf-8"
        print(url)
            
        req = requests.get(url, headers=headers).content
        soup = BeautifulSoup(req, 'lxml')
        tagh3 = soup.find_all('h3')
        for i in tagh3:
            url = i.find('a').get('href')
            real_url = requests.get(url, headers = headers, allow_redirects=False)
            print(real_url.headers['Location'])

    #默认文件类型读取
    def filetype(self):
        ext = 'filetype:'
        with open('./fileExt.txt') as lines:
            tem = lines.readlines()
            f = '('
            for i in tem:
                f = f + str(i).strip('\n') + '|'
            f =  f[:-1]+ ')'
            ext = ext + f
        return ext

#默认inurl
    def inurl(self):
        inurl = 'inurl:'
        with open('./inurl.txt') as lines:
            tem = lines.readlines()
            f = '('
            for i in tem:
                f = f + str(i).strip('\n') + '|'
            f =  f[:-1]+ ')'
            inurl = inurl + f
        return inurl
        
    
    
    
    
root = Tk()
root.title('使用小工具')
width = 1200
height = 800
sw = root.winfo_screenwidth()  
sh= root.winfo_screenheight() 
juzhong = '%dx%d+%d+%d' % (width, height, (sw-width)/2, (sh-height)/2)
root.geometry(juzhong)    # 居中对齐
page1 = App()
root.mainloop()

    
        
     
            

    
 
    


    





    
    
    
    
    