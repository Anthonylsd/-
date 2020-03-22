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
import pyperclip
import os
from tkinter.messagebox import *

class App(Frame):
    def __init__(self):
        super().__init__()
        self.site = StringVar()
        self.leixing = StringVar()
        self.list = []
        self.url = ''
        self.pack()
        self.cform()    
    def cform(self):
        Label(self,text="请选择类型：", font=("微软雅黑", 12), fg='black').grid(row = 0, column = 0, rowspan = 1,  sticky=E)
        ttk.Combobox(self, width = 25, values = ('敏感url','敏感文件','备用'), textvariable = self.leixing).grid(row = 0, column = 1, rowspan = 1, sticky=W)
        
        Label(self,text="请输入网站域名：", font=("微软雅黑", 20), fg='blue').grid(row = 1, column = 1, rowspan = 1, sticky=W)

#输入框
        Entry(self, borderwidth = 3, width=55, font=("微软雅黑", 15), textvariable = self.site).grid(row = 1, column = 2, rowspan = 1, sticky=W)

#两个按钮
        Button(self, text = '搜索', font=("微软雅黑", 16), fg='green', command=self.search).grid(row = 1, column = 3, rowspan = 1)
        Button(self, text = '自定义搜索', font=("微软雅黑", 16), fg='green', command=self.zidingyi).grid(row = 1, column = 4, rowspan = 1)
        
        Button(self, text = '保存数据到本地', font=("微软雅黑", 12), fg='red', command = self.save).grid(row = 2, column = 4, rowspan = 1, sticky=E)
        
        #test
        

        
        
        
        
        
    def getf(self):
        self.file = self.filetype()
    
    def getu(self):
        self.url = self.inurl()
    
    def zidingyi(self):
        self.destroy()
        Customize()
    
    def search(self):
        print(self.leixing.get())
        if self.leixing.get() == '':
            showinfo('警示', '请在右上角选择搜索类型')
            return
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
        save = chaxun #后面保存使用
        if self.leixing.get() == '敏感url':
            chaxun = chaxun + " " + url
        else:
             chaxun = chaxun + " " + ext
             
        #百度独有的url
        url = "https://www.baidu.com/s?wd=site%3A" + chaxun  + "&ie=utf-8"
        print(url)
            
        req = requests.get(url, headers=headers).content
        soup = BeautifulSoup(req, 'lxml')
        tagh3 = soup.find_all('h3')
        url_list = []
        for i in tagh3:
            url = i.find('a').get('href')
            real_url = requests.get(url, headers = headers, allow_redirects=False)
            print(real_url.headers['Location'])
            url_list.append(real_url.headers['Location'])
        
        if len(url_list) == 0:
            showinfo('警示','找不到相关网页')
            self.destroy()
            App()
            return
        
        Label(self,text="为您找到以下内容:", font=("微软雅黑", 16), fg='SlateGray').grid(row = 2, column = 2, rowspan = 1)
        num_url = len(url_list)
        
        self.list = url_list
        self.url = save
        
        for u in range(num_url):
            Label(self,text="{}.".format(u+1), font=("微软雅黑", 16), fg='black').grid(row = u+3, column = 1, sticky=E)
            e = Text(self, width=50, height=1, font=("微软雅黑", 16))
            e.grid(row = u+3, column = 2, sticky=W)
            e.insert(END,url_list[u])
        #存在数据的话，显示复制按钮
        
    #复制数据
    def copy(self,text):
        pyperclip.copy(text)
        
    #保存数据到本地
    def save(self):
        if(self.url == '' or not self.list):
            showinfo('警示','无数据可保存')
            return
        print('保存中...')
        b = 0
        if os.path.exists('./results.txt'):
            b = 1
            print(b)
        file = open('./results.txt','a+')
        if b == 1:
            file.write('\n'+str(self.url)+":"+'\n')
        else:
            file.write(str(self.url)+":"+'\n')
        for u in self.list:
            file.write(str(u)+'\n')
        file.close()
        showinfo('提示','保存成功')
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
        
#自定义搜索的界面
class Customize(Frame):
    def __init__(self):
        super().__init__()
        self.site = StringVar()
        self.leixing = StringVar()
        self.list = []
        self.url = ''
        self.pack()
        self.sform()    
    
    def sform(self):
        Button(self, text = '<---', font=("微软雅黑", 16), fg='green', command=self.back).grid(row = 1, column = 0, rowspan = 1, sticky=W)
#输入框
        Entry(self, borderwidth = 3, width=55, font=("微软雅黑", 15), textvariable = self.site).grid(row = 1, column = 1, rowspan = 1, sticky=E)

#按钮
        Button(self, text = '搜索', font=("微软雅黑", 16), fg='green', command=self.search).grid(row = 1, column = 2, rowspan = 1)
        Button(self, text = '保存数据到本地', font=("微软雅黑", 12), fg='red', command = self.save).grid(row = 2, column = 2, rowspan = 1, sticky=E)
    
    def save(self):
        if(self.url == '' or not self.list):
            showinfo('警示','无数据可保存')
            return
        print('保存中...')
        b = 0
        if os.path.exists('./results.txt'):
            b = 1
            print(b)
        file = open('./results.txt','a+')
        if b == 1:
            file.write('\n'+str(self.url)+":"+'\n')
        else:
            file.write(str(self.url)+":"+'\n')
        for u in self.list:
            file.write(str(u)+'\n')
        file.close()
        showinfo('提示','保存成功')
        
    #复制数据
    def copy(self,text):
        pyperclip.copy(text)
        
    def back(self):
        self.destroy()
        App()
    
    def search(self):
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
        url = "https://www.baidu.com/s?wd=" + chaxun  + "&ie=utf-8"
        req = requests.get(url, headers=headers).content
        soup = BeautifulSoup(req, 'lxml')
        tagh3 = soup.find_all('h3')
        url_list = []
        for i in tagh3:
            url = i.find('a').get('href')
            real_url = requests.get(url, headers = headers, allow_redirects=False)
            print(real_url.headers['Location'])
            url_list.append(real_url.headers['Location'])
        
        Label(self,text="为您找到以下内容:", font=("微软雅黑", 16), fg='SlateGray').grid(row = 2, column = 1, rowspan = 1)
        num_url = len(url_list)
        
        if len(url_list) == 0:
            showinfo('警示','找不到相关网页')
            self.destroy()
            Customize()
            return 
        
        self.list = url_list
        self.url = chaxun
        
        for u in range(num_url):
            Label(self,text="{}.".format(u+1), font=("微软雅黑", 16), fg='black').grid(row = u+3, column = 0, sticky=E)
            e = Text(self, width=50, height=1, font=("微软雅黑", 16))
            e.grid(row = u+3, column = 1, sticky=W)
            e.insert(END,url_list[u])
        
        
        
root = Tk()
root.title('实用小工具')
width = 1200
height = 800
sw = root.winfo_screenwidth()  
sh= root.winfo_screenheight() 
juzhong = '%dx%d+%d+%d' % (width, height, (sw-width)/2, (sh-height)/2)
root.geometry(juzhong)    # 居中对齐
page1 = App()
root.mainloop()

    
        
     
            

    
 
    


    





    
    
    
    
    